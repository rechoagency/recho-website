# RECHO Site Setup Guide

## ✅ Changes Made (Oct 24, 2025)

### 1. Blog Page Cleanup
- ✅ Removed WordPress placeholder section
- ✅ Removed 2 fake blog posts (kept only 4 real posts)
- ✅ Added working search functionality
- ✅ Removed "Load More" button

### 2. Contact Form Setup
- ✅ Removed WordPress integration notice
- ✅ Configured for Formspree (needs your email setup)

### 3. SEO Updates
- ✅ Updated sitemap.xml with all 4 blog posts
- ✅ All internal links verified

---

## 🔧 POST-DEPLOYMENT SETUP REQUIRED

### STEP 1: Set Up Formspree (Contact Form)

1. **Go to:** https://formspree.io/
2. **Sign up** for free account
3. **Create a new form**
4. **Copy your form endpoint** (looks like: `https://formspree.io/f/abc123xyz`)
5. **Update contact.html line 197:**
   - Find: `action="https://formspree.io/f/YOUR_FORM_ID"`
   - Replace `YOUR_FORM_ID` with your actual Formspree form ID
6. **Redeploy** to Cloudflare Pages

### STEP 2: Add Google Analytics

1. **Get your GA4 Measurement ID** from Google Analytics
2. **Add this code** before `</head>` tag in ALL HTML files:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace `G-XXXXXXXXXX` with your actual Measurement ID.

---

## 📊 Verify After Going Live

### Check These URLs:
- ✅ https://recho.co/robots.txt (should show sitemap link)
- ✅ https://recho.co/sitemap.xml (should list all pages + blog posts)
- ✅ https://recho.co/llms.txt (should show site info for AI crawlers)

### Test Contact Form:
1. Fill out form on https://recho.co/contact.html
2. Submit
3. Check your email for Formspree notification

### Test Blog Search:
1. Go to https://recho.co/blog.html
2. Type keywords in search bar
3. Press Enter or click search button
4. Articles should filter in real-time

---

## 📝 How to Add New Blog Posts

### Quick Method (HTML Template):

1. **Copy an existing blog post file:**
   ```bash
   cp blog-post-1.html blog-post-5.html
   ```

2. **Edit the new file** and update:
   - Title and meta description in `<head>`
   - Heading, category, date
   - Article content
   - Schema markup at bottom

3. **Add card to blog.html** (around line 300):
   ```html
   <article class="blog-card bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
       <div class="bg-gradient-to-br from-recho-orange to-red-600 h-48 flex items-center justify-center">
           <i class="fas fa-users text-white text-5xl"></i>
       </div>
       <div class="p-6">
           <div class="flex items-center gap-2 mb-3">
               <span class="px-3 py-1 bg-green-100 text-green-700 text-xs rounded-full font-semibold">Category</span>
               <span class="text-gray-500 text-xs">Date</span>
           </div>
           <h3 class="text-xl font-bold text-gray-800 mb-3">Your Blog Post Title</h3>
           <p class="text-gray-600 text-sm mb-4 leading-relaxed">
               Short description of your blog post...
           </p>
           <div class="flex items-center justify-between w-full">
               <div class="flex items-center gap-2 text-gray-500 text-xs">
                   <i class="fas fa-clock"></i>
                   <span>X min read</span>
               </div>
               <a href="blog-post-5.html" class="text-recho-orange font-semibold text-sm hover:underline">Read Article</a>
           </div>
       </div>
   </article>
   ```

4. **Update sitemap.xml:**
   ```xml
   <url>
       <loc>https://www.recho.co/blog-post-5.html</loc>
       <lastmod>2025-01-XX</lastmod>
       <changefreq>monthly</changefreq>
       <priority>0.7</priority>
   </url>
   ```

5. **Redeploy to Cloudflare Pages:**
   ```bash
   cd /home/user/webapp
   export CLOUDFLARE_API_TOKEN="your_token"
   npx wrangler pages deploy . --project-name recho-co --branch main
   ```

---

## 🎯 Current Site Status

### ✅ Complete & Working:
- All 10 pages (Home, Services, Technology, FAQ, Blog, Contact, 4 blog posts)
- 17+ Schema markups
- SEO optimized (meta tags, descriptions, headings)
- Responsive design
- Working search on blog page
- robots.txt, sitemap.xml, llms.txt

### ⏳ Needs Setup After Deployment:
- Formspree contact form (replace YOUR_FORM_ID)
- Google Analytics tracking code
- Google Search Console verification

### 📂 File Structure:
```
webapp/
├── index.html              # Homepage
├── services.html           # Services page
├── technology.html         # Technology page
├── faq.html                # FAQ page
├── blog.html               # Blog index (4 posts)
├── contact.html            # Contact page (Formspree form)
├── blog-post-1.html        # Community Management
├── blog-post-2.html        # Subreddit Strategy  
├── blog-post-3.html        # Reddit CPC
├── blog-post-4.html        # Platform Updates
├── robots.txt              # SEO crawler instructions
├── sitemap.xml             # XML sitemap (includes all pages + blog posts)
├── llms.txt                # AI crawler instructions
├── css/
│   └── style.css           # Custom styles + animations
├── js/
│   └── main.js             # JavaScript (mobile menu, counters, etc.)
└── images/
    ├── recho-logo-corrected.png
    ├── recho-logo-white.png
    ├── recho-favicon.png
    └── echomind-icon.png
```

---

## 🚀 Next Steps

1. **Deploy clean version** to Cloudflare Pages
2. **Set up Formspree** contact form
3. **Add Google Analytics** tracking code
4. **Connect domain** recho.co
5. **Verify** in Google Search Console
6. **Test everything** works

---

**Questions? Issues? Contact your developer for support!** 🎯
