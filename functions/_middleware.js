// Injects Google Tag Manager + site-wide UTM capture into every HTML page at
// the edge, so individual pages never carry hand-edited GTM tags (the ONE
// source for GTM on this site -- do not also paste GTM snippets into pages).
//
// Routing: _routes.json sends only page URLs through this function; excluded
// asset routes are served directly by Pages and keep their _headers rules.
// Responses served through this function do NOT get _headers applied
// (Cloudflare Pages limitation), so this middleware sets those headers itself
// (SECURITY_HEADERS below). Content-Security-Policy is the one deliberate
// exception: it is owned by a Cloudflare Response Header Transform Rule on the
// recho.co zone (Rules > Transform Rules) so a single rule covers every
// response path -- do not add a CSP here or in _headers.

const GTM_ID = 'GTM-5B67MTB8';

// Standard GTM head snippet (verbatim, incl. line breaks), then UTM capture.
// utm-tracking.js is cached immutable for a year (_headers /js/*) -- bump the
// ?v= query whenever js/utm-tracking.js changes so browsers refetch it.
const HEAD = `<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','${GTM_ID}');</script>
<script src="/js/utm-tracking.js?v=2" defer></script>`;

const BODY = `<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=${GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>`;

// Mirror of the /* block in _headers, minus Content-Security-Policy (see the
// header comment). Keep these values in lockstep with _headers.
const SECURITY_HEADERS = {
  'X-Frame-Options': 'DENY',
  'X-Content-Type-Options': 'nosniff',
  'X-XSS-Protection': '1; mode=block',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'geolocation=(), microphone=(), camera=(), payment=()',
  'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload',
  'X-Robots-Tag': 'index, follow',
  'Cache-Control': 'public, max-age=3600',
};

function withSecurityHeaders(response) {
  try {
    // Headers on context.next() responses are immutable; clone to set ours.
    const out = new Response(response.body, response);
    for (const [name, value] of Object.entries(SECURITY_HEADERS)) {
      out.headers.set(name, value);
    }
    return out;
  } catch {
    // Never let header decoration take the page down.
    return response;
  }
}

export async function onRequest(context) {
  const response = await context.next();

  // Rewrite only real HTML documents (e.g. "text/html; charset=utf-8").
  // Redirects, 304s, and non-HTML files pass through with headers only.
  const contentType = (response.headers.get('content-type') || '').toLowerCase();
  if (!contentType.includes('text/html')) {
    return withSecurityHeaders(response);
  }

  try {
    return withSecurityHeaders(
      new HTMLRewriter()
        .on('head', { element(e) { e.prepend(HEAD, { html: true }); } })
        .on('body', { element(e) { e.prepend(BODY, { html: true }); } })
        .transform(response)
    );
  } catch {
    // Setup-time failure: serve the page without analytics rather than a 500.
    return withSecurityHeaders(response);
  }
}
