# 📧 Email Spam Diagnostic Guide for RECHO.CO

**Date**: March 4, 2026  
**Emails Affected**: jonnywaite@recho.co, jonny@recho.co

---

## ✅ Current Email Authentication Status

### DNS Records Verification (Already Perfect ✓)

```
SPF Record: v=spf1 include:_spf.google.com ~all
Status: ✅ PASS - Correctly configured

DKIM Record: google._domainkey.recho.co
Key: 2048-bit RSA (strong encryption)
Status: ✅ PASS - Active and verified

DMARC Record: v=DMARC1; p=quarantine; adkim=r; aspf=r
Reports: dmarc_rua@onsecureserver.net
Status: ✅ PASS - Monitoring active

MX Records: Google Workspace (5 servers)
Primary: aspmx.l.google.com
Status: ✅ PASS - Enterprise-grade
```

**Overall Email Authentication Grade: A-**

---

## ⚠️ Why Emails Might Go to Spam (Common Causes)

### 1. **Domain Reputation (Age) - MOST LIKELY CAUSE**

**Problem**: `recho.co` is a relatively new domain

**How Email Filters Work**:
- New domains (< 6 months) = Higher spam risk score
- No sending history = No trust signals
- First 30-90 days = "Probation period" by major email providers

**Impact on Your Emails**:
- Gmail: May land in Promotions or Spam initially
- Outlook/Office 365: Stricter filtering for new domains
- Corporate Email: Often blocked or quarantined automatically
- Yahoo: May require manual "Not Spam" marking

**Solution Timeline**:
- Week 1-2: 60-70% spam folder placement (expected for new domains)
- Week 3-4: 40-50% spam folder (improving)
- Month 2: 20-30% spam folder (good progress)
- Month 3+: 5-10% spam folder (normal industry rate)

**Accelerated Reputation Building**:
```
Week 1: Send 5-10 emails/day
  ✓ Only to people who expect your email
  ✓ Personalized content
  ✓ Professional tone
  ✓ Ask recipients to reply

Week 2: 15-25 emails/day
  ✓ Continue personalization
  ✓ Track open rates
  ✓ Request "Add to Contacts"

Week 3-4: 30-50 emails/day
  ✓ Maintain high engagement
  ✓ Monitor bounce rates (keep < 2%)
  ✓ Remove hard bounces immediately

Month 2+: Normal volume (50-150/day)
  ✓ Established reputation
  ✓ Better deliverability
```

---

### 2. **Email Content Triggers**

**❌ SPAM TRIGGER WORDS TO AVOID:**

**High Risk** (avoid completely):
- FREE, Free, free, no cost
- ACT NOW, URGENT, HURRY
- WINNER, YOU'VE WON, CONGRATULATIONS
- $$$, $$, Make Money, Get Paid
- Click Here, Click Below
- Limited Time, Expires Today
- 100% Free, No Obligations
- Dear Friend, Dear Customer

**Medium Risk** (use cautiously):
- Guarantee, Guaranteed
- Risk-Free, No Risk
- Amazing, Incredible
- Opportunity, Special Promotion
- Call Now, Order Now
- Join Millions, Thousands of users
- Best Price, Lowest Price

**✅ SAFE ALTERNATIVES:**

Instead of: "FREE trial - Act now!"
Use: "Try RECHO for 14 days"

Instead of: "URGENT: Limited time offer!!!"
Use: "Special Reddit marketing consultation"

Instead of: "Click here to make $$$"
Use: "Learn about our pricing"

Instead of: "You've been selected!"
Use: "Following up on our conversation"

---

### 3. **Email Format Issues**

**❌ FORMATTING THAT TRIGGERS FILTERS:**

1. **All Image Emails**:
   - Problem: Email is mostly/entirely images with little text
   - Why: Spammers hide text in images to bypass filters
   - Solution: Use 60-70% text, 30-40% images

2. **Excessive Links**:
   - Problem: More than 5 links in one email
   - Why: Link farms and phishing
   - Solution: Limit to 2-3 links for cold outreach

3. **URL Shorteners**:
   - Problem: bit.ly, tinyurl.com, etc.
   - Why: Hide actual destination
   - Solution: Use full URLs (https://www.recho.co/services)

4. **Suspicious Attachments**:
   - Problem: .exe, .zip, .rar files
   - Why: Malware risk
   - Solution: Use .pdf only, or link to documents

5. **ALL CAPS SUBJECT LINES**:
   - Problem: "CHECK THIS OUT NOW"
   - Why: Shouting = spam
   - Solution: "Reddit marketing insights for [Company]"

6. **Too Many Exclamation Marks**:
   - Problem: "Great opportunity!!!"
   - Why: Excessive enthusiasm = spam
   - Solution: Use period or single ! if absolutely needed

7. **Colored/Styled Text Overuse**:
   - Problem: Multiple font colors, sizes, backgrounds
   - Why: Looks unprofessional
   - Solution: Simple HTML, professional formatting

---

### 4. **Sending Behavior Patterns**

**❌ RED FLAGS THAT TRIGGER SPAM:**

1. **Blast Sending**:
   - Sending 100+ emails in 1 hour from new domain
   - Solution: Spread over days/weeks

2. **High Bounce Rate**:
   - > 5% bounces (invalid addresses)
   - Solution: Verify emails before sending

3. **Low Engagement**:
   - 0% open rate, 0% click rate, 0% replies
   - Solution: Send to engaged recipients only

4. **Purchased Lists**:
   - Emailing people who never heard of you
   - Solution: Build organic list (website forms, LinkedIn)

5. **Rapid Volume Increase**:
   - Day 1: 10 emails → Day 2: 500 emails
   - Solution: Gradual 20-30% weekly increase

---

### 5. **Technical Email Issues**

**❌ PROBLEMS THAT HURT DELIVERABILITY:**

1. **Missing Reply-To Header**:
   - Problem: No way for recipient to reply
   - Solution: Always include Reply-To: jonnywaite@recho.co

2. **Generic From Name**:
   - Problem: "noreply@domain.com" or "info@domain.com"
   - Solution: "Jonny Waite" <jonnywaite@recho.co>

3. **Broken Unsubscribe**:
   - Problem: No unsubscribe for marketing emails (required by law)
   - Solution: Include working unsubscribe link

4. **Mixed Content**:
   - Problem: HTTPS links in HTML email with HTTP images
   - Solution: Use all HTTPS resources

5. **Invalid HTML**:
   - Problem: Broken tags, missing closing tags
   - Solution: Validate HTML before sending

---

## 🧪 DIAGNOSTIC TESTS YOU MUST RUN

### Test 1: Mail-Tester.com (CRITICAL - Run This NOW)

**From jonnywaite@recho.co:**

1. Visit: https://www.mail-tester.com
2. Copy unique test address: `test-xxxxx@srv1.mail-tester.com`
3. Send this email:

```
To: [mail-tester address]
From: jonnywaite@recho.co
Subject: RECHO - Reddit Marketing Services Introduction

Hi,

I'm Jonny from RECHO, a Reddit marketing agency helping B2B brands reach 400M+ engaged users.

We specialize in:
• Reddit Paid Advertising (CPM starting at $0.50)
• Community Management
• Brand Monitoring & Social Listening

I'd love to schedule a quick 15-minute call to discuss how we can help your brand.

Would you be available this week?

Best regards,
Jonny Waite
RECHO - Reddit Marketing Agency
https://www.recho.co
delivery@recho.co
```

4. Click "Then check your score"
5. **Target Score**: 8/10 or higher

**What Each Score Means**:
- **9-10/10**: Excellent - Should reach inbox
- **8-9/10**: Good - Mostly inbox, some promotions tab
- **6-8/10**: Fair - Mix of inbox and spam
- **< 6/10**: Poor - Likely spam folder

**If Score < 8/10, Check For**:
- Blacklists (should be 0/100)
- SPF/DKIM/DMARC failures (should all pass)
- Content issues (spam trigger words)
- HTML formatting problems

---

### Test 2: MXToolbox Blacklist Check

**Check if domain or IPs are blacklisted:**

1. Visit: https://mxtoolbox.com/blacklists.aspx
2. Enter: `recho.co`
3. Click "Blacklist Check"

**Expected Result**: 0 blacklists (green checkmarks)

**If Blacklisted**:
- Note which blacklist(s)
- Visit blacklist website
- Submit delisting request
- Common blacklists:
  - Spamhaus (strictest)
  - SORBS
  - SpamCop
  - Barracuda

**Delisting Timeline**: 24-72 hours after request

---

### Test 3: Spamhaus Check

1. Visit: https://check.spamhaus.org
2. Enter: `recho.co`
3. Also check: Your sending IP (if known)

**Expected**: "Not listed in any Spamhaus blocklist"

**If Listed**:
- Review reason for listing
- Submit support ticket: https://www.spamhaus.org/lookup/
- Provide evidence of legitimate business

---

### Test 4: Multi-Provider Delivery Test

**Send test email from jonnywaite@recho.co to:**

1. **Gmail** (your personal): `____@gmail.com`
   - Check: Inbox, Promotions, Spam
   - Expected: Promotions or Inbox (for new domain)

2. **Outlook/Office 365**: Test account or colleague
   - Check: Inbox, Junk
   - Expected: May go to Junk initially (strict for new domains)

3. **Yahoo Mail**: Test account
   - Check: Inbox, Bulk
   - Expected: 50/50 chance (Yahoo is strict)

4. **Corporate Email**: A client or colleague's work email
   - Check: Inbox, Spam, Quarantine
   - Expected: May be quarantined (corporate filters strictest)

**Document Results**:
```
Gmail: [Inbox/Promotions/Spam]
Outlook: [Inbox/Junk]
Yahoo: [Inbox/Bulk]
Corporate: [Inbox/Spam/Quarantined]
```

---

### Test 5: Google Postmaster Tools Setup

**Monitor Gmail-specific deliverability:**

1. Visit: https://postmaster.google.com
2. Sign in with Google Workspace admin
3. Click "Add domain"
4. Enter: `recho.co`
5. Verify ownership:
   - Add TXT record: `google-site-verification=xxxxx`
   - Or use existing Google Workspace verification

**Wait 24-48 hours for data**

**Metrics to Monitor**:
- **Domain Reputation**: High/Medium/Low/Bad
  - Target: High
  - New domains start at Medium
- **IP Reputation**: High/Medium/Low/Bad
  - Google Workspace IPs: Should be High
- **Spam Rate**: Percentage marked as spam
  - Target: < 0.1%
  - Acceptable: < 0.3%
- **Feedback Loop**: User complaints
  - Target: 0 complaints

---

### Test 6: Formspree Delivery Verification

**Check if contact form submissions are being delivered:**

1. **Login to Formspree**: https://formspree.io
2. Navigate to: Forms → `mpwowyrn`
3. Check **Submissions** tab:
   - Are submissions being logged? ✅
   - Any delivery failures? ❌
   - Delivery status for each submission?

4. **Send test form submission**:
   - Visit: https://www.recho.co/contact
   - Fill with test data
   - Submit
   - Check arrival at: `jonnwaite@recho.co` AND `jonny@recho.co`
   - Check Formspree dashboard for delivery status

**Formspree Common Issues**:
- Free tier limit: 50 submissions/month
- Emails sent from: `noreply@formspree.io` (may need whitelisting)
- Some corporate filters block third-party form services

**Solution if Blocked**:
1. Whitelist `noreply@formspree.io` in your email settings
2. Add custom email forwarding in Formspree (paid feature)
3. Check Formspree delivery logs for specific errors

---

## 🎯 COMPREHENSIVE EMAIL AUDIT CHECKLIST

### A. Authentication & DNS (Already Perfect ✅)
- [x] SPF record configured
- [x] DKIM signing active
- [x] DMARC policy set
- [x] MX records pointing to Google Workspace
- [x] Reverse DNS matches
- [x] Domain verified in Google Workspace

### B. Reputation & Blacklists (Need to Check)
- [ ] Run MXToolbox blacklist check (https://mxtoolbox.com/blacklists.aspx)
- [ ] Check Spamhaus (https://check.spamhaus.org)
- [ ] Check SORBS (http://www.sorbs.net/lookup.shtml)
- [ ] Check Barracuda (https://www.barracudacentral.org/lookups)
- [ ] Set up Google Postmaster Tools
- [ ] Review DMARC aggregate reports

### C. Content Quality (Review Your Emails)
- [ ] Check for spam trigger words
- [ ] Verify professional tone
- [ ] Ensure proper text-to-image ratio (60/40)
- [ ] Limit links to 2-3 per email
- [ ] Use full URLs (no shorteners)
- [ ] Include clear signature
- [ ] Professional subject lines only

### D. Sending Patterns (Monitor)
- [ ] Start with 5-10 emails/day
- [ ] Track bounce rate (keep < 2%)
- [ ] Monitor engagement (aim for > 20% open rate)
- [ ] Gradually increase volume
- [ ] Only email opted-in contacts
- [ ] Remove bounces immediately

### E. Technical Setup (Verify)
- [ ] From name is personalized: "Jonny Waite" not "noreply"
- [ ] Reply-To header is set correctly
- [ ] Unsubscribe link for marketing emails
- [ ] HTML is valid (no broken tags)
- [ ] All images use HTTPS
- [ ] No broken links

---

## 🔍 SPECIFIC DIAGNOSTIC SCENARIOS

### Scenario 1: ALL Emails Go to Spam

**Symptoms**:
- Every email from jonnywaite@recho.co lands in spam
- Happens across Gmail, Outlook, Yahoo
- Started immediately or within first week

**Most Likely Causes**:
1. **Domain on blacklist** (check with MXToolbox)
2. **Content triggers** (spam words in every email)
3. **Email format issues** (too many images, no text)
4. **No engagement** (recipients never open/reply)

**Quick Tests**:
```bash
# Test 1: Send plain text email (no HTML, no links)
Subject: Quick question
Body: Hi, quick question about marketing services. Best, Jonny

# Test 2: Send from different email service
Try: jonny@recho.co instead of jonnywaite@recho.co

# Test 3: Check if it's domain-specific
Send from personal Gmail to same recipient
```

**Diagnosis**:
- If plain text works: Content/HTML issue
- If both addresses fail: Domain reputation issue
- If Gmail works: recho.co domain issue

---

### Scenario 2: SOME Emails Go to Spam, Not All

**Symptoms**:
- Email A goes to inbox
- Email B goes to spam
- Same domain, different content

**Most Likely Causes**:
1. **Content-specific triggers** (certain words/phrases)
2. **Attachment issues** (specific file types)
3. **Link problems** (certain URLs flagged)
4. **Recipient-specific rules** (their filters vary)

**Quick Tests**:
```
Compare successful vs. failed emails:
- What's different in content?
- Different links?
- Different attachments?
- Different recipients?
```

**Diagnosis**:
- Identify pattern in spam emails
- Remove/replace problematic elements
- Test again

---

### Scenario 3: Gmail Works, But Outlook/Yahoo Fails

**Symptoms**:
- Gmail: Inbox or Promotions (working)
- Outlook: Junk folder (blocked)
- Yahoo: Spam or blocked

**Most Likely Causes**:
1. **Provider-specific reputation** (each has separate scoring)
2. **Microsoft/Yahoo stricter filters** (less forgiving for new domains)
3. **Different content analysis** (Outlook hates certain formats)

**Solutions**:
- **Outlook-Specific**:
  - Use plain text or simple HTML
  - Avoid marketing language
  - Include physical address in signature
  - Use Microsoft SNDS: https://postmaster.live.com/snds/
  
- **Yahoo-Specific**:
  - Yahoo is notoriously strict for new domains
  - Focus on engagement (replies, not spam marks)
  - May take 2-3 months to improve

---

### Scenario 4: Corporate Emails Consistently Blocked

**Symptoms**:
- Personal Gmail: Works fine ✅
- Corporate emails: Blocked, quarantined, or rejected ❌
- Enterprise clients can't receive your emails

**Root Causes**:
1. **Stricter corporate filters** (enterprises use advanced security)
2. **New domain policy** (auto-block domains < 30 days)
3. **Category filtering** (marketing/sales emails blocked)
4. **Attachment restrictions** (some attachments auto-blocked)

**Solutions**:

**Option A: Request Whitelisting**

Email template for clients to send to their IT:
```
Subject: Whitelist Request - recho.co Email Domain

Hi [IT Department],

We're working with RECHO (recho.co), a Reddit marketing agency, and need their emails whitelisted.

Domain: recho.co
Email addresses: jonnywaite@recho.co, delivery@recho.co

Verification:
- Business: RECHO - B2B Marketing Agency
- Website: https://www.recho.co
- LinkedIn: https://www.linkedin.com/company/rechoagency
- Email Provider: Google Workspace (verified)
- Email Authentication: SPF, DKIM, DMARC all configured

Please add to allowed senders list.

Thank you,
[Client Name]
```

**Option B: Use Alternative Initial Contact**
- LinkedIn message first
- Schedule Zoom call
- Share documents via trusted platform
- Build relationship before email

**Option C: Different Email Format**
- Use plain text (no HTML)
- Minimal links (1-2 max)
- Very professional tone
- Include phone number

---

### Scenario 5: Formspree Forms Not Delivering

**Symptoms**:
- Form submissions logged in Formspree ✅
- But emails not arriving at jonnywaite@recho.co ❌

**Causes**:
1. **Formspree sender blocked**: `noreply@formspree.io` flagged
2. **Monthly limit reached**: Free tier = 50 submissions/month
3. **Email forwarding issue**: jonnwaite vs jonnywaite typo
4. **Spam folder**: Check there first!

**Diagnostic Steps**:

1. **Check Formspree Dashboard**:
   ```
   Login: https://formspree.io
   Go to: Forms → mpwowyrn → Submissions
   Look for: Red/yellow warnings on deliveries
   ```

2. **Check Email Settings**:
   ```
   Formspree Settings → Email
   Verify recipient: jonnwaite@recho.co (check spelling!)
   Reply-To: Form submitter's email ✓
   ```

3. **Whitelist Formspree**:
   ```
   Add to Gmail allowed senders:
   - noreply@formspree.io
   - Do not send to spam
   ```

4. **Test Form Directly**:
   ```
   Visit: https://www.recho.co/contact
   Submit test with your personal email
   Check both:
   - Inbox of jonnwaite@recho.co
   - Spam folder
   - Formspree dashboard for delivery status
   ```

---

## 🛠️ IMMEDIATE ACTION PLAN

### TODAY (Next 30 Minutes)

**1. Run Mail-Tester (10 min)**
- Test from: jonnywaite@recho.co
- Use professional content (template above)
- Target score: 8+/10
- Screenshot results

**2. Check Blacklists (5 min)**
- MXToolbox: https://mxtoolbox.com/blacklists.aspx
- Spamhaus: https://check.spamhaus.org
- Must show: 0 blacklists

**3. Test Formspree (5 min)**
- Submit test form
- Check delivery to both emails
- Review Formspree dashboard

**4. Multi-Provider Test (10 min)**
- Send to Gmail, Outlook, corporate email
- Document where each lands
- Identify patterns

---

### THIS WEEK

**1. Set Up Google Postmaster Tools (15 min)**
- Add domain verification
- Wait 48 hours for data
- Monitor reputation scores

**2. Review DMARC Reports (10 min)**
- Check: dmarc_rua@onsecureserver.net
- Look for authentication failures
- Identify sending issues

**3. Audit Past Emails (20 min)**
- Review last 10 emails sent
- Check for spam trigger words
- Verify all used professional tone
- Note which got replies

**4. Clean Email List (30 min)**
- Remove invalid addresses
- Remove never-opened contacts
- Segment engaged vs. unengaged
- Focus on engaged recipients

---

### NEXT 2-4 WEEKS

**1. Follow Email Warm-Up Schedule**
```
Week 1: 5-10 emails/day
Week 2: 15-25 emails/day
Week 3: 30-50 emails/day
Week 4+: Normal volume (monitor metrics)
```

**2. Monitor Key Metrics**
```
Open Rate: Target > 25%
Click Rate: Target > 3%
Reply Rate: Target > 5%
Bounce Rate: Keep < 2%
Spam Rate: Keep < 0.3%
```

**3. Build Engagement**
```
- Personalize every email
- Ask questions
- Encourage replies
- Provide value first
- Avoid heavy sales pitches initially
```

---

## 📊 EMAIL DELIVERABILITY SCORECARD

### Current Status (Estimated Based on Setup)

| Factor | Status | Grade | Notes |
|--------|--------|-------|-------|
| SPF Authentication | ✅ Configured | A | Google Workspace SPF |
| DKIM Signature | ✅ Active | A | 2048-bit RSA |
| DMARC Policy | ✅ Active | B+ | Quarantine policy |
| Domain Reputation | ⚠️ New | C | < 3 months old |
| IP Reputation | ✅ Good | A | Google IPs |
| Sending Volume | 🔶 Unknown | - | Need to monitor |
| Engagement Rate | 🔶 Unknown | - | Need to track |
| Blacklist Status | 🔶 Unknown | - | Need to check |
| Content Quality | 🔶 Unknown | - | Need to audit |

**Overall Estimated Grade: B- to B**

**With Improvements (2-3 months): A- to A**

---

## 🚨 RED FLAGS TO WATCH FOR

### Signs Your Email Has Serious Issues:

**Critical Red Flags** (Fix Immediately):
- [ ] Mail-Tester score < 6/10
- [ ] Listed on 3+ blacklists
- [ ] Bounce rate > 10%
- [ ] Domain reputation = "Bad" in Postmaster Tools
- [ ] Consistent rejection by major providers
- [ ] SPF/DKIM/DMARC failures in reports

**Warning Signs** (Monitor and Improve):
- [ ] Mail-Tester score 6-7/10
- [ ] Listed on 1-2 minor blacklists
- [ ] Bounce rate 5-10%
- [ ] Open rate < 10%
- [ ] Consistent spam folder placement across all providers
- [ ] High spam complaint rate (> 0.1%)

**Normal for New Domain** (Expected):
- [x] Some spam folder placement (30-50% first month)
- [x] Promotions tab in Gmail (common for new senders)
- [x] Domain reputation "Medium" in Postmaster Tools
- [x] Gradual improvement over 2-3 months
- [x] Need to request "Not Spam" from recipients

---

## 💡 PROVEN STRATEGIES TO IMPROVE DELIVERABILITY

### 1. **The "Whitelist Request" Email Template**

For important clients/prospects who might miss your emails:

```
Subject: Quick favor - Add us to your safe senders

Hi [Name],

To make sure you receive our updates and replies, could you add jonnywaite@recho.co to your safe senders list?

In Gmail:
1. Click the three dots on any email from me
2. Select "Add to contacts"

In Outlook:
1. Right-click any email from me
2. Select "Junk" → "Never Block Sender"

This ensures you don't miss any updates about your Reddit campaigns.

Thanks!
Jonny
```

---

### 2. **The "Engagement Builder" Initial Email**

**Don't lead with sales pitch**. Build relationship first:

```
Subject: Quick Reddit marketing question

Hi [Name],

I noticed [specific observation about their company/Reddit presence].

We work with B2B brands on Reddit (400M+ users, 40% commercial intent) and I thought you might find this stat interesting:

[Share one specific, valuable insight]

Would you be open to a quick 10-minute call to explore if Reddit could work for [Company]?

No pressure - just wanted to reach out.

Best,
Jonny Waite
RECHO
https://www.recho.co
```

**Why This Works**:
- Personalized (not generic blast)
- Provides value first
- Low-pressure ask
- Encourages reply (builds reputation)

---

### 3. **The "Plain Text Fallback" Strategy**

**If HTML emails consistently go to spam, use plain text:**

```
To: client@company.com
From: jonnywaite@recho.co
Subject: Reddit marketing for [Company]

Hi [Name],

I'm Jonny from RECHO. We help B2B brands reach 400M+ Reddit users.

Quick question: Is [Company] currently using Reddit for marketing?

We've seen great results for [similar industry] companies with:
- 40% lower CPMs than LinkedIn
- 70%+ engagement rates
- Strong ROI on community-driven campaigns

Worth a conversation?

Best,
Jonny Waite
RECHO - Reddit Marketing Agency
delivery@recho.co
+1-XXX-XXX-XXXX
```

**Advantages**:
- Lower spam score (no HTML tricks)
- Appears more personal
- Better mobile rendering
- Bypasses some HTML-based filters

---

### 4. **The "Reply-Warm-Up" Technique**

**First Week Strategy**: Focus on getting replies, not conversions

**Day 1-3**: Email 5 warm contacts (people who know you)
- Ask simple question
- Request reply
- Goal: Build positive engagement signals

**Day 4-7**: Email 5-10 semi-warm contacts (mutual connections)
- Reference how you connected
- Provide value
- Ask question that requires reply

**Day 8-14**: Start cold outreach (10-15/day)
- Highly personalized
- Specific value prop
- Low-pressure ask

**Why This Works**:
- Email providers see replies = legitimate
- High engagement rate = better reputation
- Gradual volume = not spam-like

---

## 📧 SPECIFIC FIXES FOR COMMON ISSUES

### Issue: "Your Email Contains Spam Content"

**Mail-Tester Flags**:
- BAYES_50 or higher (content appears spammy)
- HTML_MESSAGE score penalty
- SUSPICIOUS_RECIPS (recipient list issue)

**Fixes**:
1. Remove spam trigger words (see list above)
2. Simplify HTML (or use plain text)
3. Add more legitimate text content
4. Include physical business address
5. Add clear unsubscribe link

**Before**:
```
Subject: FREE Reddit Marketing - ACT NOW!!!
Body: Click here to get FREE trial...
```

**After**:
```
Subject: Reddit marketing consultation for [Company]
Body: Hi [Name], I wanted to share insights about reaching B2B buyers on Reddit...
```

---

### Issue: "SPF/DKIM/DMARC Failures"

**Symptoms**:
- Mail-Tester shows authentication failures
- DMARC reports show failed messages

**Your Status**: ✅ Already configured correctly

**But Double-Check**:
```bash
# Verify SPF
nslookup -type=txt recho.co | grep spf

# Verify DKIM
nslookup -type=txt google._domainkey.recho.co

# Verify DMARC
nslookup -type=txt _dmarc.recho.co
```

**If any fail**: Contact Google Workspace support

---

### Issue: "High Bounce Rate"

**Problem**: > 5% of emails bounce (undeliverable)

**Causes**:
- Invalid email addresses
- Typos in addresses
- Inactive accounts
- Full mailboxes

**Fixes**:
1. **Verify emails before sending**:
   - Use: https://www.zerobounce.net (free tier)
   - Or: https://hunter.io/email-verifier

2. **Clean list immediately**:
   ```
   Remove hard bounces instantly
   Soft bounces: Retry once, then remove
   Monitor bounce rate weekly
   ```

3. **Double opt-in** for newsletter signups

**Target Bounce Rate**: < 2%

---

### Issue: "Domain Marked as Suspicious"

**Symptoms**:
- VirusTotal shows security vendor flags
- URLVoid shows reputation warnings
- Corporate firewalls block domain

**Fixes** (Follow URGENT_ACTION_REQUIRED.md):
1. Submit to Symantec WebPulse
2. Submit to Fortinet FortiGuard
3. Submit to Palo Alto Networks
4. Submit to Cisco Talos
5. Submit to McAfee TrustedSource
6. Submit to Trend Micro
7. Check Google Safe Browsing
8. Check Microsoft SmartScreen

**Timeline**: 1-4 weeks for approvals

**This Also Improves Email**: Some email filters check domain reputation

---

## 🧪 TESTING PROTOCOL (Run These Now)

### Test Suite 1: Deliverability Tests (20 min)

```
1. Mail-Tester Test
   - From: jonnywaite@recho.co
   - Get score, screenshot results
   - Target: 8+/10

2. Mail-Tester Test #2
   - From: jonny@recho.co (if separate account)
   - Compare scores
   - Should be similar

3. MXToolbox Blacklist
   - Check: recho.co
   - Must show: 0 blacklists
   - Screenshot results

4. Multi-Provider Test
   - Send to Gmail, Outlook, Yahoo
   - Document where each lands
   - Note patterns
```

---

### Test Suite 2: Content Analysis (15 min)

```
1. Review Last 10 Sent Emails
   - Look for spam trigger words
   - Check text-to-image ratio
   - Count links per email
   - Note which got replies

2. Test Different Content
   - Send plain text version
   - Send HTML version
   - Send with/without links
   - Compare delivery

3. Subject Line Testing
   - Professional vs. casual
   - Question vs. statement
   - Personalized vs. generic
   - Track open rates
```

---

### Test Suite 3: Formspree Verification (10 min)

```
1. Dashboard Check
   - Login to Formspree
   - Review all submissions
   - Check delivery status
   - Note any errors

2. Test Submission
   - Fill contact form
   - Use your personal email
   - Submit and track
   - Verify arrival

3. Email Settings
   - Confirm recipient: jonnwaite@recho.co
   - Check spelling (common typo!)
   - Verify Reply-To is set
   - Test email notifications
```

---

## 📈 SUCCESS METRICS

### Week 1 Targets
- Mail-Tester Score: 7-8/10
- Blacklist Status: 0 lists
- Delivery Rate: 50-70% inbox
- Bounce Rate: < 3%
- Volume: 5-10 emails/day

### Month 1 Targets
- Mail-Tester Score: 8-9/10
- Delivery Rate: 70-80% inbox
- Open Rate: > 20%
- Reply Rate: > 3%
- Bounce Rate: < 2%
- Volume: 30-50 emails/day

### Month 3 Targets (Mature Domain)
- Mail-Tester Score: 9-10/10
- Delivery Rate: 90-95% inbox
- Open Rate: > 30%
- Reply Rate: > 5%
- Bounce Rate: < 1%
- Volume: Normal (50-150/day)
- Google Postmaster: "High" reputation

---

## 🎯 DIAGNOSIS DECISION TREE

```
Start: Email going to spam?
  │
  ├─→ ALL emails to ALL recipients?
  │   └─→ Check blacklists
  │       ├─→ On blacklist: Request delisting
  │       └─→ Not on blacklist: Domain reputation (follow warm-up)
  │
  ├─→ SOME emails to ALL recipients?
  │   └─→ Compare content
  │       ├─→ Specific words/links: Remove triggers
  │       └─→ Random: Content quality issue
  │
  ├─→ ALL emails to SPECIFIC providers?
  │   └─→ Check provider
  │       ├─→ Gmail works, Outlook fails: Microsoft SNDS
  │       ├─→ Gmail/Outlook work, corporate fails: Request whitelist
  │       └─→ All fail: Domain on blacklist
  │
  └─→ Formspree forms not arriving?
      └─→ Check Formspree dashboard
          ├─→ Submissions logged: Whitelist noreply@formspree.io
          ├─→ Delivery failures: Fix email address typo
          └─→ No submissions: Form configuration issue
```

---

## 📞 WHAT TO DO IF TESTS SHOW ISSUES

### If Mail-Tester Score < 8/10

**Share these details**:
1. Screenshot of full Mail-Tester results
2. Specific errors/warnings shown
3. SPF/DKIM/DMARC status
4. Blacklist checks (if any)
5. Content analysis section

**I'll provide**:
- Specific fixes for each issue
- Updated email template
- Configuration changes if needed

---

### If Blacklisted

**Share these details**:
1. Which blacklist(s)?
2. Domain or IP listed?
3. Reason given (if shown)
4. When did it happen?

**I'll provide**:
- Delisting request instructions
- Prevention strategies
- Alternative sending methods

---

### If Corporate Emails Consistently Fail

**Share these details**:
1. Which companies/industries?
2. What error message (if any)?
3. Soft bounce or hard bounce?
4. Same for all enterprise or specific ones?

**I'll provide**:
- Whitelist request template
- Alternative contact methods
- Enterprise-specific email format

---

## 🎉 BOTTOM LINE

### Why Your Emails MIGHT Go to Spam

**It's NOT because**:
- ❌ Your DNS is wrong (it's perfect)
- ❌ Your domain is suspicious (it's legitimate)
- ❌ Your email provider is bad (Google Workspace is best-in-class)

**It's LIKELY because**:
- ⚠️ **New domain** (< 6 months old) = Lower reputation
- ⚠️ **No sending history** = Email providers are cautious
- ⚠️ **Content might have triggers** = Need to audit
- ⚠️ **Formspree sender** = Some filters block `noreply@formspree.io`

---

## ✅ YOUR ACTION ITEMS

### 🔴 CRITICAL (Do Today - 30 min)
1. Run Mail-Tester test from both email addresses
2. Check MXToolbox blacklists
3. Test Formspree form delivery
4. Send multi-provider test emails

### 🟡 IMPORTANT (This Week)
1. Set up Google Postmaster Tools
2. Audit last 10 emails for spam triggers
3. Start email warm-up schedule (5-10/day)
4. Monitor engagement metrics

### 🟢 ONGOING (Next 2-4 Weeks)
1. Gradually increase sending volume
2. Remove bounces immediately
3. Request whitelist from corporate clients
4. Review DMARC reports weekly
5. Track deliverability improvements

---

## 📚 RESOURCES

**Testing Tools**:
- Mail-Tester: https://www.mail-tester.com
- MXToolbox: https://mxtoolbox.com
- Spamhaus: https://check.spamhaus.org
- Google Postmaster: https://postmaster.google.com

**Reputation Databases**:
- VirusTotal: https://www.virustotal.com/gui/domain/recho.co
- URLVoid: https://www.urlvoid.com/scan/recho.co
- Talos: https://talosintelligence.com/reputation_center/lookup?search=recho.co

**Email Authentication Checkers**:
- DMARC Analyzer: https://www.dmarcanalyzer.com
- DKIM Validator: https://dkimvalidator.com
- SPF Record Check: https://www.kitterman.com/spf/validate.html

---

**Questions?** Run the tests in "IMMEDIATE ACTION PLAN" section and share results. I'll help diagnose and fix specific issues.

---

**Last Updated**: March 4, 2026  
**Next Review**: After running test suite (share results)
