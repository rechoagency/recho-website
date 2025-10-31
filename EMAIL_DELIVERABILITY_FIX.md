# 🚨 Email Deliverability Fix Guide - Google Workspace (@recho.co)

**Date:** January 15, 2025  
**Issue:** Emails going to spam after Cloudflare Pages website launch

---

## 📋 **Quick Diagnosis Checklist**

Before we fix anything, we need to verify your current DNS email records.

### **Step 1: Check Your Current DNS Records in Cloudflare**

1. **Go to Cloudflare Dashboard:**
   - Visit: https://dash.cloudflare.com/
   - Select domain: **recho.co**
   - Click **DNS** in left sidebar

2. **Look for these critical records:**

---

## ✅ **Required Email Records for Google Workspace**

You should see these records in your Cloudflare DNS:

### **1. MX Records (Mail Routing)**
**Required for receiving email:**

```
Type: MX | Name: @ | Content: ASPMX.L.GOOGLE.COM | Priority: 1
Type: MX | Name: @ | Content: ALT1.ASPMX.L.GOOGLE.COM | Priority: 5
Type: MX | Name: @ | Content: ALT2.ASPMX.L.GOOGLE.COM | Priority: 5
Type: MX | Name: @ | Content: ALT3.ASPMX.L.GOOGLE.COM | Priority: 10
Type: MX | Name: @ | Content: ALT4.ASPMX.L.GOOGLE.COM | Priority: 10
```

**Proxy Status:** DNS only (grey cloud) ⚠️ IMPORTANT: MX records MUST NOT be proxied

---

### **2. SPF Record (Sender Authentication)**
**Tells recipients Google can send email for your domain:**

```
Type: TXT
Name: @
Content: v=spf1 include:_spf.google.com ~all
```

**What this means:**
- `v=spf1` - SPF version 1
- `include:_spf.google.com` - Google Workspace is authorized to send email
- `~all` - Soft fail (messages from other servers marked suspicious)

**Proxy Status:** DNS only (grey cloud)

---

### **3. DKIM Record (Email Signature)**
**Cryptographic signature proving emails are authentic:**

You need to get your DKIM key from Google Workspace Admin:

1. **Go to Google Workspace Admin Console:**
   - Visit: https://admin.google.com/
   - Go to: **Apps** → **Google Workspace** → **Gmail** → **Authenticate email**
   
2. **Generate DKIM Key:**
   - Click **Generate New Record**
   - Copy the DKIM record details

3. **Add to Cloudflare DNS:**
```
Type: TXT
Name: google._domainkey
Content: v=DKIM1; k=rsa; p=YOUR_LONG_PUBLIC_KEY_HERE
```

**Proxy Status:** DNS only (grey cloud)

---

### **4. DMARC Record (Email Policy)**
**Tells recipients what to do with failed authentication:**

```
Type: TXT
Name: _dmarc
Content: v=DMARC1; p=quarantine; rua=mailto:dmarc@recho.co; pct=100; adkim=r; aspf=r
```

**What this means:**
- `v=DMARC1` - DMARC version 1
- `p=quarantine` - Quarantine emails that fail authentication (send to spam)
- `rua=mailto:dmarc@recho.co` - Send aggregate reports here
- `pct=100` - Apply policy to 100% of emails
- `adkim=r` - Relaxed DKIM alignment
- `aspf=r` - Relaxed SPF alignment

**Proxy Status:** DNS only (grey cloud)

---

## 🔍 **Step 2: Verify What's Missing**

### **Option A: Check in Cloudflare Dashboard** (Recommended)

1. Go to Cloudflare DNS settings
2. Look for each record type above (MX, TXT for SPF, TXT for DKIM, TXT for DMARC)
3. Note which ones are missing

### **Option B: Use Online DNS Checker**

1. **Go to MXToolbox:**
   - Visit: https://mxtoolbox.com/SuperTool.aspx
   
2. **Check MX records:**
   - Enter: `mx:recho.co`
   - Click **MX Lookup**
   - Should show 5 Google MX servers

3. **Check SPF record:**
   - Enter: `spf:recho.co`
   - Click **SPF Record Lookup**
   - Should show: `v=spf1 include:_spf.google.com ~all`

4. **Check DMARC record:**
   - Enter: `txt:_dmarc.recho.co`
   - Click **TXT Lookup**
   - Should show DMARC policy

5. **Check DKIM record:**
   - Enter: `txt:google._domainkey.recho.co`
   - Click **TXT Lookup**
   - Should show DKIM public key

---

## 🛠️ **Step 3: Add Missing Records in Cloudflare**

Once you identify what's missing, add them:

### **To Add a Record in Cloudflare:**

1. **Cloudflare Dashboard** → **DNS**
2. Click **Add record**
3. Fill in:
   - **Type:** (MX or TXT)
   - **Name:** (@ or specific subdomain)
   - **Content:** (the record value)
   - **Priority:** (for MX records only)
   - **Proxy status:** DNS only (grey cloud) ⚠️
4. Click **Save**

---

## 🚨 **Most Likely Issues After Website Migration**

Based on your situation (emails to spam after Cloudflare Pages launch), the most likely causes are:

### **Issue 1: Missing SPF Record**
**Symptoms:** Emails marked as spam or rejected  
**Fix:** Add SPF TXT record (see above)

### **Issue 2: Missing or Invalid DKIM**
**Symptoms:** Emails fail authentication checks  
**Fix:** 
1. Get DKIM key from Google Workspace Admin
2. Add DKIM TXT record to Cloudflare DNS
3. Verify in Google Admin (takes 24-48 hours)

### **Issue 3: No DMARC Policy**
**Symptoms:** Recipients don't know how to handle failed auth  
**Fix:** Add DMARC TXT record (see above)

### **Issue 4: MX Records Accidentally Deleted**
**Symptoms:** Emails bounce or not received at all  
**Fix:** Re-add all 5 Google MX records

### **Issue 5: DNS Proxying Enabled on Email Records**
**Symptoms:** Email delivery failures  
**Fix:** Ensure all MX and email TXT records have **DNS only** (grey cloud)

---

## 📊 **Step 4: Verify Google Workspace DKIM Setup**

This is CRITICAL and often the cause of spam issues:

### **Enable DKIM in Google Workspace:**

1. **Go to Google Admin Console:**
   - https://admin.google.com/

2. **Navigate to Gmail settings:**
   - **Apps** → **Google Workspace** → **Gmail**
   - Click **Authenticate email**

3. **Generate DKIM key:**
   - Click **Generate New Record** (if not already done)
   - Select **Generate new record**
   - Prefix: `google` (default)
   - Key length: `2048 bits`
   - Click **Generate**

4. **Copy the DNS records shown:**
   - You'll see a TXT record like:
   ```
   Host/Name: google._domainkey
   TXT Record Value: v=DKIM1; k=rsa; p=MIGfMA0GCS...very long key...
   ```

5. **Add to Cloudflare DNS:**
   - Type: TXT
   - Name: `google._domainkey`
   - Content: (paste the entire TXT value from Google)
   - Proxy: DNS only
   - Save

6. **Wait 24-48 hours**, then return to Google Admin

7. **Click "Start Authentication":**
   - Google will verify the DKIM record
   - Status should change to "Authenticating email"

---

## ⏰ **DNS Propagation Timeline**

After adding/fixing records:
- **Immediate:** Changes visible in Cloudflare
- **5-10 minutes:** Changes propagate to Cloudflare nameservers
- **24-48 hours:** Full global DNS propagation
- **24-48 hours:** Google verifies DKIM authentication

**Note:** Email deliverability should improve within 1-2 hours of correct DNS setup

---

## 🧪 **Step 5: Test Your Email Deliverability**

After adding all records, test your setup:

### **Test 1: Send Email to Gmail**
1. Send email from your @recho.co address to a Gmail account
2. Check if it lands in inbox or spam
3. Open the email in Gmail
4. Click the three dots (⋮) → **Show original**
5. Check for:
   - ✅ `SPF: PASS`
   - ✅ `DKIM: PASS`
   - ✅ `DMARC: PASS`

### **Test 2: Use Mail Tester**
1. Go to: https://www.mail-tester.com/
2. Send email from @recho.co to the provided test address
3. Click **Then check your score**
4. Should score **9/10 or 10/10**
5. Review any warnings/errors

### **Test 3: Check DNS Records**
1. Go to: https://mxtoolbox.com/domain/recho.co/
2. Review **Domain Health Report**
3. All email authentication should show ✅ green

---

## 📋 **Quick Fix Checklist**

Copy this checklist and check off as you complete:

**DNS Records in Cloudflare:**
- [ ] 5 MX records pointing to Google servers
- [ ] SPF TXT record: `v=spf1 include:_spf.google.com ~all`
- [ ] DKIM TXT record at `google._domainkey`
- [ ] DMARC TXT record at `_dmarc`
- [ ] All email records set to "DNS only" (not proxied)

**Google Workspace Admin:**
- [ ] DKIM authentication enabled
- [ ] DKIM status shows "Authenticating email"
- [ ] No error messages in Gmail settings

**Testing:**
- [ ] Sent test email to Gmail (landed in inbox)
- [ ] SPF/DKIM/DMARC all show "PASS" in email headers
- [ ] Mail Tester score: 9/10 or 10/10
- [ ] MXToolbox shows all green checks

---

## 🎯 **What to Share With Me**

To help you fix this quickly, please share:

1. **Screenshot or list of current DNS records** in Cloudflare for:
   - All MX records
   - All TXT records (especially ones with SPF, DKIM, DMARC)

2. **Google Workspace DKIM status:**
   - Go to Google Admin → Gmail → Authenticate email
   - What does it show? (Not set up, Authenticating, etc.)

3. **Mail Tester results:**
   - Send test email to mail-tester.com
   - Share the score and any red/yellow warnings

4. **Sample spam email headers:**
   - Open spam email in Gmail
   - Show original → Copy SPF/DKIM/DMARC lines

Once I see these, I can tell you exactly what's missing and how to fix it!

---

## 🚀 **Expected Timeline**

**Today (15 minutes):**
- Check Cloudflare DNS records
- Identify what's missing
- Add missing records

**Within 1-2 hours:**
- DNS propagates
- Emails start landing in inbox

**Within 24-48 hours:**
- Google verifies DKIM
- Full email authentication working
- Spam issues resolved

---

## 💡 **Pro Tips**

1. **Never proxy email records** - Always set to "DNS only" (grey cloud)
2. **Wait 48 hours** after DKIM setup before testing
3. **Use strong DMARC policy** - `p=quarantine` or `p=reject` prevents spoofing
4. **Monitor reports** - Check DMARC aggregate reports at `dmarc@recho.co`
5. **Test regularly** - Use mail-tester.com monthly

---

## 🆘 **Common Errors & Solutions**

### **Error: "SPF record not found"**
**Solution:** Add SPF TXT record to Cloudflare DNS

### **Error: "DKIM signature missing"**
**Solution:** Enable DKIM in Google Workspace Admin and add TXT record

### **Error: "Multiple SPF records found"**
**Solution:** Consolidate into one SPF record (use `include:` for multiple senders)

### **Error: "MX record points to proxied domain"**
**Solution:** Disable Cloudflare proxy on MX records (grey cloud)

### **Error: "DMARC policy too weak"**
**Solution:** Change from `p=none` to `p=quarantine` or `p=reject`

---

## 📞 **Need Immediate Help?**

Share your Cloudflare DNS records and Google Workspace DKIM status, and I'll create a custom fix plan for your exact situation!

**Most likely you're missing:**
1. ✅ SPF record
2. ✅ DKIM record (most common cause of spam)
3. ✅ DMARC policy

Let's fix this together! 🚀
