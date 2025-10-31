# 📊 GA4 Custom Event Tracking - Complete Guide

**Date:** January 15, 2025  
**Status:** ✅ Deployed and Live  
**Script:** `/js/ga4-events.js`

---

## 🎯 **Custom Events Now Tracking:**

### **1. Email Link Clicks** 📧
**Tracks:** Clicks on sales@recho.co email links

**Event Name:** `email_click`

**Parameters:**
- `event_category`: "Contact"
- `event_label`: "sales@recho.co"
- `email_address`: "sales@recho.co"
- `location`: Page URL where clicked

**Where to find in GA4:**
- Reports → Engagement → Events → `email_click`

**Use case:** See which pages drive the most email inquiries

---

### **2. Social Share Buttons** 🔗
**Tracks:** All 4 share buttons on blog posts (LinkedIn, Twitter, Reddit, Email)

**Event Name:** `share`

**Parameters:**
- `method`: "LinkedIn", "Twitter", "Reddit", or "Email"
- `content_type`: "article"
- `item_id`: Blog post URL
- `article_title`: Blog post title

**Where to find in GA4:**
- Reports → Engagement → Events → `share`
- Can filter by `method` parameter to see which platform is most popular

**Use case:** 
- See which articles get shared most
- Identify which social platform your audience prefers
- Measure content virality

---

### **3. Blog Search Queries** 🔍
**Tracks:** Search terms entered in blog page search bar

**Event Name:** `search`

**Parameters:**
- `search_term`: What user typed (e.g., "Reddit CPC", "community building")
- `search_location`: "blog_page"

**Triggers when:**
- User clicks search button
- User presses Enter in search field

**Where to find in GA4:**
- Reports → Engagement → Events → `search`
- Click on `search_term` parameter to see all search queries

**Use case:**
- Discover what topics users want to read about
- Identify content gaps
- Create new blog posts based on popular searches
- Improve search functionality

**How to analyze:**
1. GA4 → Reports → Engagement → Events
2. Click on `search` event
3. Click "View search_term" parameter
4. Sort by count to see most popular searches

---

### **4. "Book a Call" CTA Clicks** 📞
**Tracks:** All Call-to-Action buttons (Book a Call, Contact Us, Schedule, etc.)

**Event Name:** `cta_click`

**Parameters:**
- `event_category`: "Engagement"
- `event_label`: Button text (e.g., "Book a Call", "Schedule My Free Strategy Call")
- `cta_location`: Page URL where button was clicked
- `cta_type`: "Book a Call"

**Where to find in GA4:**
- Reports → Engagement → Events → `cta_click`

**Use case:**
- Measure conversion funnel
- See which pages drive the most CTA clicks
- A/B test button placement and copy

---

### **5. Blog Card Clicks** 📝
**Tracks:** Clicks on blog post cards/thumbnails

**Event Name:** `blog_click`

**Parameters:**
- `event_category`: "Content"
- `event_label`: Blog post title
- `blog_url`: Blog post URL
- `click_location`: Page where card was clicked

**Where to find in GA4:**
- Reports → Engagement → Events → `blog_click`

**Use case:**
- See which blog posts attract the most clicks
- Measure effectiveness of blog thumbnails
- Understand content discovery patterns

---

### **6. External Link Clicks** 🌐
**Tracks:** Clicks on external links (LinkedIn profile, etc.)

**Event Name:** `external_link_click`

**Parameters:**
- `event_category`: "Outbound"
- `event_label`: Destination domain (e.g., "linkedin.com")
- `link_text`: Link text or aria-label
- `link_url`: Full destination URL
- `from_page`: Page where link was clicked

**Where to find in GA4:**
- Reports → Engagement → Events → `external_link_click`

**Use case:**
- Track clicks to your LinkedIn profile
- Measure traffic sent to partner sites
- Identify most popular external resources

---

### **7. Form Submissions** ✅ (Already set up)
**Event Name:** `form_submission`

**Parameters:**
- `event_category`: "Contact"
- `event_label`: "Contact Form"
- `value`: 1

**Where to find in GA4:**
- Reports → Engagement → Events → `form_submission`
- Mark as conversion: Admin → Events → Toggle "Mark as conversion"

---

## 📊 **How to View Events in GA4**

### **Real-Time Monitoring:**
1. Go to: https://analytics.google.com/
2. Select: RECHO Website (G-HPND9L4EB9)
3. Click: **Reports** → **Realtime**
4. Scroll to: **Event count by Event name**
5. Perform actions on your site (click email, share button, search, etc.)
6. **Watch events appear in real-time!** 🎯

### **Historical Event Data:**
1. **Reports** → **Engagement** → **Events**
2. See all events with counts and user engagement
3. Click on any event to see parameters and details

### **Event-Specific Analysis:**
1. **Reports** → **Engagement** → **Events**
2. Click on event name (e.g., `search`)
3. Click on parameter (e.g., `search_term`)
4. Sort by count to see most popular values

---

## 🔍 **Analyzing Blog Search Data**

**See what users are searching for:**

1. **GA4** → **Reports** → **Engagement** → **Events**
2. Click on **`search`** event
3. Click **"View search_term breakdown"**
4. You'll see table like:
   ```
   search_term              Count   Users
   "Reddit CPC"             45      38
   "community building"     32      29
   "Reddit ads"             28      24
   "subreddit strategy"     15      14
   ```

**Use this data to:**
- ✅ Create blog posts about popular search terms
- ✅ Improve existing content for common queries
- ✅ Understand user intent and pain points
- ✅ Optimize SEO for trending topics

---

## 🎯 **Setting Up Conversion Goals**

**Mark important events as conversions:**

1. **GA4 Admin** → **Events**
2. Find event: `form_submission`, `cta_click`, or `email_click`
3. Toggle **"Mark as conversion"** to ON
4. Event now appears in **Conversions** reports

**Recommended conversions:**
- ✅ `form_submission` - Primary conversion
- ✅ `cta_click` - Engagement conversion
- ✅ `email_click` - Contact intent conversion

---

## 📈 **Custom Reports You Can Create**

### **1. Content Performance Report**
**Question:** Which blog posts drive the most engagement?

**Events to compare:**
- `blog_click` - Which posts get clicked
- `share` - Which posts get shared
- Page views - Which posts get visited

### **2. Conversion Funnel Report**
**Question:** How do users move toward conversion?

**Funnel stages:**
1. Page view (any page)
2. `blog_click` or content engagement
3. `cta_click` (Book a Call)
4. `email_click` or `form_submission` (Conversion)

### **3. Search Intent Report**
**Question:** What are users looking for?

**Analysis:**
- Group `search_term` by topic
- Count frequency of searches
- Cross-reference with existing blog posts
- Identify content gaps

### **4. Social Sharing Report**
**Question:** Which content gets shared and on what platforms?

**Metrics:**
- `share` events by `method` parameter
- Which articles get shared most
- Platform preference (LinkedIn vs. Twitter vs. Reddit)

---

## 🧪 **Testing Your Events**

### **Test Checklist:**

**Email Links:**
- [ ] Click sales@recho.co link
- [ ] Check Real-Time for `email_click` event

**Share Buttons (on any blog post):**
- [ ] Click LinkedIn share button
- [ ] Click Twitter share button
- [ ] Click Reddit share button
- [ ] Click Email share button
- [ ] Check Real-Time for `share` events

**Blog Search:**
- [ ] Go to blog page
- [ ] Type search query (e.g., "Reddit ads")
- [ ] Click search button or press Enter
- [ ] Check Real-Time for `search` event with your search term

**CTA Buttons:**
- [ ] Click any "Book a Call" button
- [ ] Check Real-Time for `cta_click` event

**Blog Cards:**
- [ ] Click any blog post card/thumbnail
- [ ] Check Real-Time for `blog_click` event

**Expected Result:** All events appear in Real-Time report within 5-10 seconds! ✅

---

## 🚀 **Deployment Details**

**Files Changed:**
- ✅ Created: `/js/ga4-events.js` (new tracking script)
- ✅ Updated: All 10 pages (index, services, technology, faq, blog, contact, 4 blog posts)
- ✅ Git commit: 13c7580
- ✅ Pushed to GitHub main branch
- ✅ Deployed via Cloudflare Pages

**Script automatically loads on:**
- All main pages
- All blog posts
- Contact form page

**No additional setup required - tracking starts immediately!** 🎯

---

## 📊 **Expected Data Volume**

**Within 24 hours, you should see:**
- ✅ Email clicks: 5-10 events
- ✅ Share buttons: 2-5 events
- ✅ Blog searches: 3-8 events
- ✅ CTA clicks: 10-20 events
- ✅ Blog card clicks: 15-30 events
- ✅ Form submissions: 1-3 events

**After 7 days:**
- ✅ Enough data to identify trends
- ✅ Popular search terms revealed
- ✅ Most-shared content identified
- ✅ Conversion patterns emerging

---

## 💡 **Pro Tips**

### **1. Create Custom Exploration Reports**
- GA4 → Explore → Create custom report
- Combine multiple events for deeper insights
- Export data for analysis

### **2. Set Up Alerts**
- Get notified when specific events spike
- Monitor form submission drops
- Track unusual search patterns

### **3. Segment by Traffic Source**
- See how different traffic sources behave
- Compare organic vs. paid vs. social
- Optimize for highest-converting sources

### **4. A/B Test Using Event Data**
- Test different CTA button text
- Try different blog thumbnails
- Experiment with share button placement

---

## 🆘 **Troubleshooting**

### **Events not showing up?**

**Check:**
1. **Browser console** - Should see: "GA4 Custom Event Tracking Initialized ✅"
2. **Ad blocker disabled?** - Turn off for testing
3. **Clear cache** - Ctrl+Shift+R (or Cmd+Shift+R)
4. **Wait 2-5 minutes** - Events process with slight delay

### **Search events not firing?**

**Verify:**
1. You're on the **blog page** (not blog post)
2. You typed something in search input
3. You clicked search button OR pressed Enter
4. Check browser console for: "GA4 Event: Blog search tracked"

### **Share buttons not tracking?**

**Confirm:**
1. You're on a **blog post page** (not blog listing page)
2. Scroll to bottom to find share buttons
3. Click a share button
4. Check browser console for: "GA4 Event: [Platform] share tracked"

---

## ✅ **Summary**

**What's Now Tracking:**
- ✅ Email clicks (sales@recho.co)
- ✅ Social shares (4 platforms)
- ✅ Blog searches (with search terms)
- ✅ CTA button clicks
- ✅ Blog card clicks
- ✅ External link clicks
- ✅ Form submissions (already set up)

**Total Custom Events:** 7 event types

**Where to See Data:**
- Real-Time: https://analytics.google.com/ → Reports → Realtime
- Events Report: Reports → Engagement → Events

**Deployment Status:**
- ✅ Code deployed to production
- ✅ Tracking active on all pages
- ✅ Ready to collect data

**Next Steps:**
1. ✅ Test events in Real-Time report (do this now!)
2. ✅ Mark `form_submission` as conversion
3. ⏳ Wait 24-48 hours for meaningful data
4. 📊 Analyze search terms and create content

---

## 🎉 **You're All Set!**

**Your website now tracks:**
- Every user interaction that matters
- Search intent and content gaps
- Social sharing behavior
- Conversion funnel actions

**Go test it out!** Visit your site, click around, and watch the events flow into GA4 Real-Time! 🚀
