/**
 * utm-tracking.js — RECHO attribution capture (v2)
 * Sender Digital · July 2026 · replaces the previous /js/utm-tracking.js
 *
 * Drop-in replacement. Same filename, no dependencies, safe to load on every page.
 *
 * What it does:
 *  1. On every page load, reads tracking parameters from the URL:
 *     utm_source, utm_medium, utm_campaign, utm_term, utm_content, utm_id,
 *     gclid, gbraid, wbraid, msclkid — plus the referrer and entry page.
 *  2. Persists them in first-party cookies on .recho.co (90 days):
 *     - FIRST TOUCH  (sd_ft): written once, never overwritten.
 *     - LAST TOUCH   (sd_lt): updated whenever a visit arrives with new
 *       tracking parameters.
 *  3. Fills hidden fields on every form that posts to Formspree — creating
 *     the inputs if the form doesn't have them, so no form markup changes
 *     are ever needed.
 *  4. Guards against double-loading (the tag may appear twice on /contact).
 *  5. Pushes the captured values to the dataLayer so Tag Manager reuses the
 *     exact same values instead of computing its own.
 *
 * Legacy compatibility: if a form already has hidden inputs named
 * utm_source / utm_medium / utm_campaign / utm_term / utm_content (the old
 * script's fields), they keep being filled (with last-touch values), so
 * existing email notifications look the same as before.
 */
(function () {
  'use strict';

  // ---- double-load guard (this tag can legitimately appear twice) --------
  if (window.__sdUtmTrackingLoaded) return;
  window.__sdUtmTrackingLoaded = true;

  var COOKIE_FIRST = 'sd_ft';
  var COOKIE_LAST = 'sd_lt';
  var COOKIE_DAYS = 90;
  var COOKIE_DOMAIN = 'recho.co'; // cookies set on .recho.co so apex + www share them
  var PARAMS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term',
    'utm_content', 'utm_id', 'gclid', 'gbraid', 'wbraid', 'msclkid'];

  // ---- tiny cookie helpers ----------------------------------------------
  function setCookie(name, value) {
    var expires = new Date(Date.now() + COOKIE_DAYS * 864e5).toUTCString();
    var base = name + '=' + encodeURIComponent(value) +
      '; expires=' + expires + '; path=/; SameSite=Lax';
    if (location.protocol === 'https:') base += '; Secure';
    var host = location.hostname;
    if (host === COOKIE_DOMAIN || host.slice(-(COOKIE_DOMAIN.length + 1)) === '.' + COOKIE_DOMAIN) {
      document.cookie = base + '; domain=.' + COOKIE_DOMAIN;
    } else {
      document.cookie = base; // preview / local hosts: host-only cookie
    }
  }

  function getCookie(name) {
    var m = document.cookie.match(new RegExp('(?:^|;\\s*)' + name + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : null;
  }

  function readJsonCookie(name) {
    try { return JSON.parse(getCookie(name) || 'null'); } catch (e) { return null; }
  }

  // ---- capture -----------------------------------------------------------
  function currentParams() {
    var out = {};
    var found = false;
    var qs;
    try { qs = new URLSearchParams(location.search); } catch (e) { return { found: false, values: out }; }
    for (var i = 0; i < PARAMS.length; i++) {
      var v = qs.get(PARAMS[i]);
      if (v) { out[PARAMS[i]] = v; found = true; }
    }
    return { found: found, values: out };
  }

  function externalReferrer() {
    var ref = document.referrer || '';
    if (!ref) return '';
    try {
      var host = new URL(ref).hostname;
      if (host === location.hostname) return '';
      if (host === COOKIE_DOMAIN || host.slice(-(COOKIE_DOMAIN.length + 1)) === '.' + COOKIE_DOMAIN) return '';
      return ref;
    } catch (e) { return ''; }
  }

  var caught = currentParams();
  var nowIso = new Date().toISOString();
  var pageUrl = location.href.split('#')[0];

  // FIRST TOUCH — write once, then only refresh the expiry, never the values.
  var first = readJsonCookie(COOKIE_FIRST);
  if (!first) {
    first = {};
    for (var k in caught.values) first[k] = caught.values[k];
    first.referrer = externalReferrer();
    first.landing_page = pageUrl;
    first.timestamp = nowIso;
  }
  setCookie(COOKIE_FIRST, JSON.stringify(first)); // (re)set → rolling 90-day window

  // LAST TOUCH — update only when this visit carries new tracking params.
  var last = readJsonCookie(COOKIE_LAST);
  if (caught.found) {
    last = {};
    for (var k2 in caught.values) last[k2] = caught.values[k2];
    last.landing_page = pageUrl;
    last.timestamp = nowIso;
    setCookie(COOKIE_LAST, JSON.stringify(last));
  } else if (last) {
    setCookie(COOKIE_LAST, JSON.stringify(last)); // refresh expiry
  }
  if (!last) last = {};

  // ---- assemble the field set every Formspree form should carry ----------
  function fieldSet() {
    var f = {};
    // first touch
    f.utm_source_first = first.utm_source || '';
    f.utm_medium_first = first.utm_medium || '';
    f.utm_campaign_first = first.utm_campaign || '';
    f.utm_term_first = first.utm_term || '';
    f.utm_content_first = first.utm_content || '';
    f.landing_page_first = first.landing_page || '';
    f.referrer_first = first.referrer || '';
    f.first_touch_timestamp = first.timestamp || '';
    // last touch
    f.utm_source_last = last.utm_source || '';
    f.utm_medium_last = last.utm_medium || '';
    f.utm_campaign_last = last.utm_campaign || '';
    f.utm_term_last = last.utm_term || '';
    f.utm_content_last = last.utm_content || '';
    f.landing_page_last = last.landing_page || '';
    // click ids: most recent wins; fall back to first touch
    f.gclid = last.gclid || first.gclid || '';
    f.gbraid = last.gbraid || first.gbraid || '';
    f.wbraid = last.wbraid || first.wbraid || '';
    f.msclkid = last.msclkid || first.msclkid || '';
    // context
    f.form_page = pageUrl;
    return f;
  }

  // legacy names the old script filled — kept so nothing downstream changes
  var LEGACY = {
    utm_source: 'utm_source_last', utm_medium: 'utm_medium_last',
    utm_campaign: 'utm_campaign_last', utm_term: 'utm_term_last',
    utm_content: 'utm_content_last'
  };

  function isFormspreeForm(form) {
    var action = form.getAttribute('action') || '';
    return action.indexOf('formspree.io') !== -1;
  }

  function upsertHidden(form, name, value) {
    var input = form.querySelector('input[name="' + name + '"]');
    if (!input) {
      input = document.createElement('input');
      input.type = 'hidden';
      input.name = name;
      form.appendChild(input);
    }
    // Never blank a field something else already filled.
    if (value || !input.value) input.value = value;
  }

  function fillForms() {
    var fields = fieldSet();
    var forms = document.querySelectorAll('form');
    for (var i = 0; i < forms.length; i++) {
      var form = forms[i];
      if (!isFormspreeForm(form)) continue;
      for (var name in fields) upsertHidden(form, name, fields[name]);
      for (var legacy in LEGACY) {
        // only fill legacy fields that already exist in the markup
        var existing = form.querySelector('input[name="' + legacy + '"]');
        if (existing && fields[LEGACY[legacy]]) existing.value = fields[LEGACY[legacy]];
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fillForms);
  } else {
    fillForms();
  }

  // ---- share with Tag Manager -------------------------------------------
  // GTM reads these instead of computing its own, so both layers always
  // agree. (GTM's submit-time write remains the final word by design.)
  window.SD_TRACKING = { first: first, last: last, fields: fieldSet() };
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({ event: 'sd_tracking_ready', sd_tracking: window.SD_TRACKING.fields });
})();
