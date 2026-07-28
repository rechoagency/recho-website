# Google Ads Landing Pages - Implementation Summary

## Overview
Created 4 landing pages for RECHO's Google Ads campaigns, following the wireframe specifications and build package requirements.

## Landing Pages Created

### 1. Reddit GEO Landing Page
**URL:** `/reddit-geo.html`
**Purpose:** Target searches for "Reddit GEO", "generative engine optimization", "AI visibility"

**Key Features:**
- ✅ H1: "Reddit GEO — earn your brand's place in AI answers"
- ✅ Subhead includes "generative engine optimization" and "AI visibility"
- ✅ H2 section: "Reddit SEO & GEO"
- ✅ EchoMind mentioned for measurement tracking
- ✅ URL slug: `/reddit-geo`
- ✅ Title tag: "Reddit GEO — Generative Engine Optimization & AI Visibility | RECHO"
- ✅ Meta robots: `noindex, follow` (Google Ads only, not organic)

### 2. Reddit Marketing Agency Landing Page
**URL:** `/reddit-marketing-agency.html`
**Purpose:** Target searches for "reddit marketing agency"

**Key Features:**
- ✅ H1: "The Reddit **marketing** agency for brands with a reputation to protect"
- ✅ Full-service messaging (organic + paid + AI visibility)
- ✅ All three service pillars prominently featured
- ✅ Title tag: "Reddit Marketing Agency — Full-Service Organic & Paid Reddit Marketing | RECHO"
- ✅ Meta robots: `noindex, follow`

### 3. Reddit Advertising Agency Landing Page
**URL:** `/reddit-advertising-agency.html`
**Purpose:** Target searches for "reddit advertising agency", "reddit ads agency"

**Key Features:**
- ✅ H1: "The Reddit **advertising** agency for brands with a reputation to protect"
- ✅ Advertising service featured first in services section
- ✅ Full-funnel Reddit Ads management messaging
- ✅ Title tag: "Reddit Advertising Agency — Full-Funnel Reddit Ads Management | RECHO"
- ✅ Meta robots: `noindex, follow`

### 4. Thank You Page
**URL:** `/thank-you.html`
**Purpose:** Conversion confirmation after form submission

**Key Features:**
- ✅ Simple, clean confirmation message
- ✅ "A member of the RECHO team will reach out shortly to book your strategy call"
- ✅ What happens next section
- ✅ Links to Code of Conduct, Blog, and Services
- ✅ Google Ads conversion tracking placeholder
- ✅ Meta robots: `noindex, follow`

## Form Integration

### Formspree Setup
- **Form endpoint:** `https://formspree.io/f/mpwowyrn` (existing endpoint)
- **Method:** POST
- **Redirect:** All forms redirect to `/thank-you.html` on successful submission
- **Error handling:** Alert with fallback email `sales@recho.co`

### Form IDs
- Reddit GEO: `#geo-form`
- Reddit Marketing Agency: `#marketing-form`
- Reddit Advertising Agency: `#advertising-form`

### Hidden Fields
Each form includes:
- `_subject`: Unique subject line per landing page
- `page`: Page identifier for tracking

### Form Fields
1. Full name (required)
2. Work email (required)
3. Company (required)
4. What are you exploring? (required dropdown)
5. What prompted your search? (optional textarea)

## Global Footer Integration

**Orphan Page Links Added to Footer "Company" Section:**
The three landing pages are now linked in the footer of all main site pages:
- index.html ✅
- services.html ✅
- blog.html ✅
- contact.html ✅
- faq.html ✅
- technology.html ✅

**Footer Link Styling:**
- Styled as gray text with smaller font size
- Hover state changes to RECHO orange
- Links positioned after "Book a Call" in Company section

## Sitemap Updates

Added to `sitemap.xml`:
```xml
<!-- Google Ads Landing Pages (noindex) -->
<url>
  <loc>https://recho.co/reddit-geo</loc>
  <lastmod>2026-07-28</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.5</priority>
</url>
<url>
  <loc>https://recho.co/reddit-marketing-agency</loc>
  <lastmod>2026-07-28</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.5</priority>
</url>
<url>
  <loc>https://recho.co/reddit-advertising-agency</loc>
  <lastmod>2026-07-28</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.5</priority>
</url>
```

## SEO & Keyword Optimization

### Reddit GEO Page
**Primary Keywords:**
- Reddit GEO (in URL, title, H1, body)
- Generative engine optimization (in meta, subhead, body)
- AI visibility (in meta, subhead, body)

**Secondary Keywords:**
- Reddit SEO (in H2, body)
- AI citations
- ChatGPT
- Google AI Overviews
- EchoMind

### Reddit Marketing Agency Page
**Primary Keywords:**
- Reddit marketing agency (in URL, title, H1, body)
- Reddit marketing (throughout)

**Secondary Keywords:**
- Organic community building
- Reddit advertising
- AI visibility
- Full-service Reddit agency

### Reddit Advertising Agency Page
**Primary Keywords:**
- Reddit advertising agency (in URL, title, H1, body)
- Reddit ads agency (alt phrasing)
- Reddit advertising (throughout)

**Secondary Keywords:**
- Reddit Ads management
- Full-funnel advertising
- Reddit campaigns

## Design Consistency

All landing pages share:
- ✅ RECHO brand colors (orange #E6462F, blue #1E40AF, cream #FFF5F3)
- ✅ Poppins font family (via Google Fonts)
- ✅ Tailwind CSS framework
- ✅ Font Awesome icons
- ✅ Consistent header (slim, minimal navigation)
- ✅ Consistent footer (Privacy Policy, Code of Conduct, Copyright)
- ✅ Mobile-responsive design
- ✅ Sticky form on desktop
- ✅ Smooth scroll anchor links

## Wireframe Compliance

Based on `recho-landing-page-wireframe_1.html`:
- ✅ Slim header with zero exits (only Code of Conduct link opens in new tab)
- ✅ Message-matched hero with noun swaps per variant (marketing/advertising)
- ✅ Single form per page with all CTAs anchoring to it
- ✅ Hidden fields for GCLID + UTM tracking (ready for implementation)
- ✅ Empathy block: "Reddit doesn't hate brands. It hates bad marketing."
- ✅ Sourced stats with citations (Ahrefs, Semrush)
- ✅ Three service pillars
- ✅ "What we will never do" panel with Code of Conduct link
- ✅ "From first call to live on Reddit" 3-step process
- ✅ FAQ accordion (7 questions)
- ✅ Final CTA band
- ✅ Minimal footer

## robots.txt Consideration

**IMPORTANT:** All landing pages use `noindex, follow` meta tags, but ensure `robots.txt` does NOT disallow:
```
User-agent: AdsBot-Google
Disallow:
```

Blocking AdsBot-Google will tank Quality Score regardless of landing page quality.

## Next Steps for Google Ads Setup

1. **UTM Parameter Setup:**
   - Add UTM tracking parameters to ad URLs
   - Example: `?utm_source=google&utm_medium=cpc&utm_campaign=reddit-geo&gclid={gclid}`

2. **Conversion Tracking:**
   - Replace placeholder in `thank-you.html` with actual Google Ads conversion tracking code
   - Set up conversion action in Google Ads account

3. **Quality Score Optimization:**
   - Verify robots.txt allows AdsBot-Google
   - Test page load speed (all pages under 3 seconds recommended)
   - Verify mobile responsiveness
   - Check form functionality on all devices

4. **A/B Testing Considerations:**
   - Test hero copy variations
   - Test CTA button text variations
   - Test form field order
   - Test with/without trust badges

## Files Modified

**New Files:**
- `reddit-geo.html` (29KB)
- `reddit-marketing-agency.html` (30KB)
- `reddit-advertising-agency.html` (30KB)
- `thank-you.html` (8.2KB)
- `add_footer_links.py` (automation script)

**Modified Files:**
- `index.html` (footer links added)
- `services.html` (footer links added)
- `blog.html` (footer links added)
- `contact.html` (footer links added)
- `faq.html` (footer links added)
- `technology.html` (footer links added)
- `sitemap.xml` (3 new URLs added)

## Git Commit

**Commit hash:** `5a8b0ee`
**Branch:** `main`
**Status:** ✅ Pushed to GitHub

---

**Implementation Date:** July 28, 2026
**Developer:** Claude (Genspark Code Assistant)
**Total Files Created:** 5
**Total Files Modified:** 7
**Total Lines Added:** 1,730
