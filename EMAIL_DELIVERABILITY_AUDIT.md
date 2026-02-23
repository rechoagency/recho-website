# Email Deliverability Audit for jonnywaite@recho.co & jonny@recho.co

## Current Status Assessment

### ✅ What's Working
1. **Professional domain**: `recho.co` (not free email like Gmail/Yahoo)
2. **HTTPS website**: Legitimate business presence
3. **Formspree integration**: Professional form handling
4. **No spam triggers in code**: Clean HTML/JavaScript

### ⚠️ Potential Issues

#### 1. Domain Reputation (New Domain)
**Problem**: `recho.co` is a new domain without established email sending reputation  
**Impact**: Initial emails may land in spam until reputation is built  
**Solution**: See "Quick Wins" section below

#### 2. Missing Email Authentication Records
**Critical**: These DNS records prove you're a legitimate sender

**Check Current Status**:
- Visit: https://mxtoolbox.com/SuperTool.aspx
- Enter: `recho.co`
- Check for SPF, DKIM, DMARC records

#### 3. Formspree as Sender
**Issue**: Formspree sends emails on your behalf  
**Impact**: Some spam filters may flag third-party senders  
**Solution**: Verify Formspree is configured correctly

---

## Quick Wins (Do These Now)

### 1. Verify Email Authentication Records

#### Check SPF Record
```bash
# Run this command or use MXToolbox:
nslookup -type=TXT recho.co
```

**Expected Result**: Should include SPF record  
**Example**: `v=spf1 include:_spf.google.com ~all`

**If Missing**: Add SPF record to your DNS:
- If using Google Workspace: `v=spf1 include:_spf.google.com ~all`
- If using Office 365: `v=spf1 include:spf.protection.outlook.com ~all`
- If using other: Contact your email provider

#### Check DKIM Record
```bash
# Check DKIM selector (varies by provider)
nslookup -type=TXT default._domainkey.recho.co
```

**If Missing**: Enable DKIM in your email provider settings

#### Check DMARC Record
```bash
nslookup -type=TXT _dmarc.recho.co
```

**Expected**: `v=DMARC1; p=quarantine; rua=mailto:dmarc@recho.co`

**If Missing**: Add DMARC record to DNS:
```
_dmarc.recho.co IN TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@recho.co; pct=100; sp=quarantine"
```

---

### 2. Verify Formspree Configuration

#### Check Formspree Settings
1. Log in to: https://formspree.io
2. Go to form: `mpwowyrn`
3. Verify settings:
   - ✅ Email recipient: `jonnwaite@recho.co` (primary)
   - ✅ Reply-to: Respondent's email
   - ✅ Domain: `recho.co` or `www.recho.co`

#### Formspree Email Forwarding Note
- Formspree uses their own sending infrastructure
- Emails appear to come from: `noreply@formspree.io`
- This is normal and shouldn't cause spam issues
- Most email providers whitelist Formspree

---

### 3. Test Email Deliverability

#### Use Mail-Tester (Comprehensive Test)
1. Visit: https://www.mail-tester.com
2. Copy the unique email address they provide
3. Send a test email from `jonnywaite@recho.co` to that address
4. Return to Mail-Tester and click "Check Score"
5. **Goal**: Score 8/10 or higher

**Common Issues Found**:
- Missing SPF record (−1 to −3 points)
- Missing DKIM (−1 to −2 points)
- Missing DMARC (−0.5 to −1 point)
- New domain (−0.5 point, normal)

#### Test Form Submission
1. Visit: https://recho.co/contact
2. Fill out form with test data
3. Submit and wait for email
4. Check inbox AND spam folder
5. If in spam, mark as "Not Spam"

---

### 4. Configure Email Provider Properly

#### If Using Google Workspace
**Required DNS Records**:
```
# MX Records (priority matters!)
recho.co MX 1 ASPMX.L.GOOGLE.COM
recho.co MX 5 ALT1.ASPMX.L.GOOGLE.COM
recho.co MX 5 ALT2.ASPMX.L.GOOGLE.COM
recho.co MX 10 ALT3.ASPMX.L.GOOGLE.COM
recho.co MX 10 ALT4.ASPMX.L.GOOGLE.COM

# SPF Record
recho.co TXT "v=spf1 include:_spf.google.com ~all"

# DMARC Record
_dmarc.recho.co TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@recho.co"
```

**Enable DKIM**:
1. Go to Google Admin Console
2. Apps → Google Workspace → Gmail → Authenticate email
3. Click "Generate new record"
4. Copy the DKIM record
5. Add to DNS: `google._domainkey.recho.co TXT "..."`
6. Wait 24-48 hours for propagation
7. Return and click "Start authentication"

#### If Using Office 365
**Required DNS Records**:
```
# MX Record
recho.co MX 0 recho-co.mail.protection.outlook.com

# SPF Record
recho.co TXT "v=spf1 include:spf.protection.outlook.com ~all"

# DMARC Record
_dmarc.recho.co TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@recho.co"
```

**Enable DKIM**:
1. Go to Microsoft 365 Admin Center
2. Settings → Domains → recho.co
3. Click "Enable DKIM"
4. Copy the two CNAME records
5. Add to DNS:
   ```
   selector1._domainkey.recho.co CNAME selector1-recho-co._domainkey.yourdomain.onmicrosoft.com
   selector2._domainkey.recho.co CNAME selector2-recho-co._domainkey.yourdomain.onmicrosoft.com
   ```

---

## Advanced Reputation Building

### 1. Warm Up Your Email Domain
**Don't blast 100 emails on day 1!**

**Recommended Schedule**:
- Week 1: 5-10 emails/day
- Week 2: 20-30 emails/day
- Week 3: 50-75 emails/day
- Week 4+: Normal volume (100+)

**Why**: Sudden high volume from new domain = spam flag

### 2. Monitor Bounce Rates
**Target**: < 2% bounce rate  
**Action if higher**:
- Clean email list
- Remove invalid addresses
- Use email verification service

### 3. Track Spam Complaints
**Target**: < 0.1% spam complaint rate  
**Action**:
- Include clear unsubscribe link
- Honor unsubscribe requests immediately
- Don't buy email lists

### 4. Build Engagement
**Best practices**:
- Personalized subject lines
- Relevant content
- Clear call-to-action
- Professional signature
- No ALL CAPS or excessive punctuation!!!

---

## Email Signature Best Practices

### Recommended Signature
```
Jonny Waite
RECHO - Reddit Marketing Agency
📧 jonnywaite@recho.co
🌐 https://www.recho.co
💼 LinkedIn: https://www.linkedin.com/company/rechoagency

Helping brands reach 400M+ Reddit users through organic management, paid advertising, and proprietary technology.
```

### Avoid in Signature:
- ❌ Large images (slow loading)
- ❌ Excessive emojis
- ❌ Marketing disclaimers in every email
- ❌ Unsubscribe links (not needed for 1-to-1 emails)

---

## Monitoring & Maintenance

### Weekly Checks
1. **DMARC Reports**: Check `dmarc@recho.co` for reports
2. **Bounce Reports**: Monitor bounced emails
3. **Spam Complaints**: Watch for spam reports

### Monthly Checks
1. **MXToolbox**: Run full email health check
2. **Google Postmaster**: Monitor domain reputation (if sending to Gmail users)
3. **Mail-Tester**: Random spot checks

### Tools to Use
- **MXToolbox**: https://mxtoolbox.com/SuperTool.aspx
- **Mail-Tester**: https://www.mail-tester.com
- **Google Postmaster**: https://postmaster.google.com
- **DMARC Analyzer**: https://dmarc.org/resources/tools/

---

## Troubleshooting Common Issues

### "My emails keep going to spam"

#### Check These First:
1. ✅ SPF record configured?
2. ✅ DKIM enabled?
3. ✅ DMARC record added?
4. ✅ Sending from professional email (not free service)?
5. ✅ Subject line isn't spammy?
6. ✅ Email content isn't all links?
7. ✅ Recipients have received emails from you before?

#### Quick Fixes:
1. **Ask recipients to whitelist your email**
   - Gmail: Add to contacts
   - Outlook: Add to safe senders
   - Corporate: Request IT whitelist

2. **Improve email content**:
   - Less images, more text
   - No shortened URLs (bit.ly, etc.)
   - Professional formatting
   - Clear unsubscribe option (for marketing emails)

3. **Authenticate your sending**:
   - Ensure SPF/DKIM/DMARC are set up
   - Wait 24-48 hours for DNS propagation

### "Formspree emails not arriving"

#### Check:
1. Spam folder (most common!)
2. Formspree dashboard for failed sends
3. Email quota limits on your account
4. Recipient email is valid

#### Solutions:
1. Whitelist: `noreply@formspree.io` in your email
2. Check Formspree logs: https://formspree.io/forms/mpwowyrn/submissions
3. Verify recipient addresses are correct
4. Test with another email address

### "Gmail marks my emails as spam"

#### Specific to Gmail:
1. Check Google Postmaster: https://postmaster.google.com
2. Verify SPF includes Google's servers
3. Enable DKIM through Google Workspace
4. Ask recipients to mark as "Not Spam"
5. Improve engagement (replies, opens, clicks)

---

## Email Provider Recommendations

### Best Options for Business Email

#### ✅ Google Workspace (Recommended)
- **Cost**: $6-12/user/month
- **Pros**: Best deliverability, professional, integrated tools
- **SPF**: `include:_spf.google.com`
- **Setup**: Easy DKIM configuration

#### ✅ Microsoft 365
- **Cost**: $5-12.50/user/month
- **Pros**: Great for Microsoft ecosystem, strong spam filtering
- **SPF**: `include:spf.protection.outlook.com`
- **Setup**: Good DKIM support

#### ⚠️ Basic Hosting Email
- **Cost**: Often free with hosting
- **Cons**: Poor deliverability, limited support
- **Recommendation**: Avoid for business communication

#### ❌ Free Email (Gmail, Yahoo, Outlook.com)
- **Cost**: Free
- **Cons**: Unprofessional, poor sender reputation with custom domain
- **Recommendation**: Never use for business

---

## Action Plan (Next 48 Hours)

### Priority 1: DNS Records (Critical)
- [ ] Check SPF record exists
- [ ] Check DKIM is enabled
- [ ] Add DMARC record
- [ ] Wait 24 hours for propagation

### Priority 2: Formspree Configuration
- [ ] Log in to Formspree
- [ ] Verify recipient emails
- [ ] Check for failed submissions
- [ ] Test form submission

### Priority 3: Deliverability Testing
- [ ] Send test via Mail-Tester
- [ ] Check score (aim for 8+/10)
- [ ] Fix any flagged issues
- [ ] Test actual form submission

### Priority 4: Email Provider Setup
- [ ] Confirm email provider (Google/Microsoft)
- [ ] Verify all DNS records are correct
- [ ] Enable DKIM if not already done
- [ ] Set up email forwarding if needed

---

## Expected Timeline

### Immediate (0-24 hours)
- Add missing DNS records
- Configure Formspree properly
- Test deliverability

### Short-term (2-7 days)
- DNS records fully propagated
- DKIM authentication active
- Improved deliverability scores

### Medium-term (1-2 weeks)
- Domain reputation building
- Consistent inbox delivery
- Lower spam rates

### Long-term (1-3 months)
- Full email reputation established
- Excellent deliverability
- Trusted sender status

---

## Final Checklist

### Email Authentication
- [ ] SPF record configured correctly
- [ ] DKIM enabled and verified
- [ ] DMARC policy published
- [ ] MX records pointing to email provider
- [ ] PTR record (reverse DNS) configured

### Content Best Practices
- [ ] Professional email signature
- [ ] No spammy subject lines
- [ ] Balanced text-to-image ratio
- [ ] Clear unsubscribe option (for marketing)
- [ ] Mobile-friendly formatting

### Monitoring Setup
- [ ] DMARC reports configured
- [ ] Google Postmaster account created
- [ ] MXToolbox monitoring enabled
- [ ] Regular Mail-Tester checks scheduled

### Reputation Building
- [ ] Email warm-up schedule planned
- [ ] Engagement metrics tracked
- [ ] Bounce rate monitored
- [ ] Spam complaints reviewed

---

## Support Resources

### Need Help with DNS?
- **Cloudflare DNS**: https://dash.cloudflare.com (if using Cloudflare)
- **Google Domains**: https://domains.google.com
- **Namecheap**: https://www.namecheap.com/support
- **GoDaddy**: https://www.godaddy.com/help

### Email Provider Support
- **Google Workspace**: https://support.google.com/a
- **Microsoft 365**: https://support.microsoft.com/en-us/office

### Testing Tools
- **MXToolbox**: https://mxtoolbox.com
- **Mail-Tester**: https://www.mail-tester.com
- **Postmark DMARC**: https://dmarc.postmarkapp.com

---

## Questions?

If emails are still going to spam after implementing these fixes:
1. Share your Mail-Tester score
2. Provide DMARC reports
3. Share example email content
4. Check MXToolbox for blacklist issues

**Most email deliverability issues are resolved within 48 hours of fixing DNS records.**
