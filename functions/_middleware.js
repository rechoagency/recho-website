// Injects Google Tag Manager + site-wide UTM capture into every HTML page at
// the edge, so individual pages never carry hand-edited GTM tags (the ONE
// source for GTM on this site -- do not also paste GTM snippets into pages).
//
// Routing: _routes.json sends only page URLs through this function; excluded
// asset routes are served directly by Pages and keep their _headers rules.
// Responses served through this function do NOT get _headers applied
// (Cloudflare Pages limitation) -- security/caching headers for HTML are
// restored by a Cloudflare Transform Rule configured separately. Do not
// deploy to production until that rule exists.

const GTM_ID = 'GTM-5B67MTB8';

// Standard GTM head snippet (verbatim, incl. line breaks), then UTM capture.
const HEAD = `<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','${GTM_ID}');</script>
<script src="/js/utm-tracking.js" defer></script>`;

const BODY = `<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=${GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>`;

export async function onRequest(context) {
  const response = await context.next();

  // Rewrite only real HTML documents (e.g. "text/html; charset=utf-8").
  // Redirects, 304s, and non-HTML files pass through untouched.
  const contentType = (response.headers.get('content-type') || '').toLowerCase();
  if (!contentType.includes('text/html')) {
    return response;
  }

  try {
    return new HTMLRewriter()
      .on('head', { element(e) { e.prepend(HEAD, { html: true }); } })
      .on('body', { element(e) { e.prepend(BODY, { html: true }); } })
      .transform(response);
  } catch {
    // Setup-time failure: serve the page without analytics rather than a 500.
    return response;
  }
}
