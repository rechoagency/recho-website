# Blog Post Schema Template for RECHO

## Required Schema Markup for ALL Blog Posts

Every blog post MUST include these 3 schema types before `</body>`:

---

### 1. Article/BlogPosting Schema

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://www.recho.co/blog/YOUR-POST-URL.html"
  },
  "headline": "Your Blog Post Title Here",
  "description": "Your meta description (150-160 chars)",
  "image": "https://www.recho.co/images/recho-logo.png",
  "author": {
    "@type": "Organization",
    "name": "RECHO",
    "url": "https://www.recho.co"
  },
  "publisher": {
    "@type": "Organization",
    "name": "RECHO",
    "logo": {
      "@type": "ImageObject",
      "url": "https://www.recho.co/images/recho-logo.png"
    }
  },
  "datePublished": "2025-01-15T09:00:00-05:00",
  "dateModified": "2025-01-15T09:00:00-05:00",
  "articleSection": "Reddit Marketing",
  "keywords": "keyword1, keyword2, keyword3",
  "articleBody": "First 150 words of your article...",
  "about": [
    {
      "@type": "Thing",
      "name": "Main Topic 1"
    },
    {
      "@type": "Thing",
      "name": "Main Topic 2"
    }
  ]
}
</script>
```

**CRITICAL REQUIREMENTS:**
- ✅ **datePublished MUST include timezone**: `YYYY-MM-DDTHH:MM:SS-05:00` format
- ✅ **dateModified MUST include timezone**: Same format as datePublished
- ✅ **@id MUST be full URL** including https://www.recho.co/blog/
- ✅ **DO NOT include "mentions"** field (causes validation errors)

---

### 2. BreadcrumbList Schema

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.recho.co/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://www.recho.co/blog.html"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Your Article Title",
      "item": "https://www.recho.co/blog/YOUR-POST-URL.html"
    }
  ]
}
</script>
```

**CRITICAL REQUIREMENTS:**
- ✅ **Only 3 levels**: Home → Blog → Article
- ✅ **NO category level** (no `blog.html#category`)
- ✅ **Full URLs** with https://

---

### 3. FAQPage Schema (If article has Q&A)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Your question here?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Your answer here."
      }
    },
    {
      "@type": "Question",
      "name": "Another question?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Another answer."
      }
    }
  ]
}
</script>
```

**OPTIONAL** - Only include if your article has FAQ-style content.

---

## Quick Checklist for New Blog Posts:

- [ ] Update `@id` with actual blog post URL
- [ ] Update `headline` with article title
- [ ] Update `description` with meta description
- [ ] Set `datePublished` with **timezone** (format: `2025-01-15T09:00:00-05:00`)
- [ ] Set `dateModified` with **timezone**
- [ ] Update `keywords` with relevant keywords
- [ ] Add first 150 words to `articleBody`
- [ ] Update breadcrumb item name (position 3) with article title
- [ ] Update breadcrumb item URL (position 3) with full article URL
- [ ] Add FAQPage schema if article has Q&A content
- [ ] Validate at https://search.google.com/test/rich-results

---

## Common Mistakes to Avoid:

❌ **DON'T** use dates without timezone: `"2025-01-15"`  
✅ **DO** use dates with timezone: `"2025-01-15T09:00:00-05:00"`

❌ **DON'T** include category in breadcrumb: `blog.html#category`  
✅ **DO** use clean 3-level breadcrumb: Home → Blog → Article

❌ **DON'T** add "mentions" field with SoftwareApplication  
✅ **DO** keep schema clean and simple

❌ **DON'T** use relative URLs in @id  
✅ **DO** use full URLs: `https://www.recho.co/blog/...`

---

## Validation:

After creating a new blog post, ALWAYS test at:
**https://search.google.com/test/rich-results**

Expected results:
- ✅ Article schema (valid)
- ✅ BreadcrumbList schema (valid)
- ✅ FAQPage schema (if included, valid)
- ✅ No errors or critical issues

---

## Example Blog Post Files:

Reference these existing posts as templates:
- `/home/user/webapp/blog/how-to-build-an-engaged-reddit-community.html`
- `/home/user/webapp/blog/why-your-reddit-strategy-is-failing.html`

Copy the schema blocks from these files when creating new posts!
