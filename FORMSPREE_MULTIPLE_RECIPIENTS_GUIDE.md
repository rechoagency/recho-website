# How to Add jonny@recho.co as Contact Form Recipient

## ❌ Issue Discovered
The `_cc` hidden field approach **does not work** with Formspree. After testing, neither email received the form submission because Formspree requires dashboard configuration for multiple recipients.

---

## ✅ Solution: Configure in Formspree Dashboard

To add `jonny@recho.co` as a recipient, you need to configure it in your Formspree account:

### Step-by-Step Instructions

1. **Log in to Formspree**
   - Visit: https://formspree.io
   - Log in with your Formspree account credentials

2. **Locate Your Form**
   - Find the form with ID: `mpwowyrn`
   - This is the RECHO contact form

3. **Access Form Settings**
   - Click on the form to open its settings
   - Look for **"Rules"** or **"Email Notifications"** section

4. **Add Email Rule**
   - Click **"Add Rule"** or **"Add Notification"**
   - Set condition: **"When form is submitted"** (or "always")
   - Set action: **"Send Email to"**
   - Enter email: `jonny@recho.co`
   - Save the rule

5. **Verify Configuration**
   - Submit a test form
   - Check both inboxes:
     - jonnwaite@recho.co (primary)
     - jonny@recho.co (new recipient)

---

## ⚠️ Important Notes

### Formspree Pricing
- **Multiple recipients via Rules is a PAID feature** on most Formspree plans
- If you're on the free plan, you may need to upgrade
- Check your current plan at: https://formspree.io/plans

### Current Setup
- Form endpoint: `https://formspree.io/f/mpwowyrn`
- Primary recipient: `jonnwaite@recho.co` (configured in Formspree)
- Additional recipient: Needs to be added via dashboard

---

## 🔄 Alternative Solutions

If you don't want to pay for Formspree's Rules feature, here are alternatives:

### Option 1: Email Forwarding (Free)
**Set up at your email provider (not Formspree)**

Configure `jonnwaite@recho.co` to automatically forward all emails to `jonny@recho.co`

**Pros:**
- Free
- No Formspree changes needed
- Works immediately

**Cons:**
- Requires email provider configuration
- jonny@recho.co receives forwarded emails (not direct from Formspree)

**How to do it:**
- Log in to your email hosting provider (Google Workspace, Microsoft 365, etc.)
- Go to jonnwaite@recho.co email settings
- Set up auto-forwarding to jonny@recho.co
- Keep a copy in jonnwaite@recho.co inbox

---

### Option 2: Email Alias/Group (Free)
**Create a group email address**

Create a group email like `leads@recho.co` or `submissions@recho.co` that includes both addresses:
- jonnwaite@recho.co
- jonny@recho.co

Then update Formspree to send to the group email instead.

**Pros:**
- Free
- Both emails receive directly from Formspree
- Easy to add more recipients later

**Cons:**
- Requires creating a new email group/alias
- Need to update Formspree form endpoint

**How to do it:**
1. Create email group at your email provider
2. Add both emails as members
3. Update Formspree form to use new group email
4. Update form action in contact.html

---

### Option 3: Switch Form Service (Free)
**Replace Formspree with a service that supports multiple recipients**

**Recommended alternatives:**

#### Web3Forms (Free, unlimited recipients)
- Website: https://web3forms.com
- Supports multiple email recipients for free
- No signup required for basic use
- Easy migration from Formspree

#### FormSubmit (Free)
- Website: https://formsubmit.co
- Supports CC/BCC for multiple recipients
- No signup required
- Simple HTML form setup

#### Netlify Forms (Free on Netlify)
- If you switch to Netlify hosting
- Supports notifications to multiple emails
- Integrated with Netlify deployment

**Migration effort:** Low (just change form action URL and update hidden fields)

---

## 📝 Recommended Approach

**I recommend Option 1: Email Forwarding** because:
- ✅ Free (no additional costs)
- ✅ No code changes needed
- ✅ Works immediately
- ✅ Doesn't require Formspree upgrade
- ✅ Easy to configure at email provider level

**How to implement:**
1. Log in to your email hosting provider
2. Access settings for jonnwaite@recho.co
3. Enable auto-forwarding to jonny@recho.co
4. Test by submitting the contact form
5. Check both inboxes

---

## 🔍 Current Status

### What's in Production Now
- Form endpoint: Working (https://formspree.io/f/mpwowyrn)
- Primary recipient: jonnwaite@recho.co (configured in Formspree)
- Additional recipient: **NOT configured yet** (needs dashboard setup)

### HTML Comments Added
I've added comments in the HTML code (lines 246-247) to remind you where to configure this:

```html
<!-- NOTE: To add jonny@recho.co as recipient, configure "Form Rules" in Formspree dashboard -->
<!-- Go to: https://formspree.io/forms/mpwowyrn/settings and add email rule -->
```

---

## ✅ Action Items

**Choose ONE of these options:**

### ⭐ Option 1: Email Forwarding (Recommended)
- [ ] Log in to email hosting provider
- [ ] Configure jonnwaite@recho.co to forward to jonny@recho.co
- [ ] Test with form submission
- [ ] Verify both inboxes receive emails

### Option 2: Upgrade Formspree
- [ ] Log in to Formspree
- [ ] Upgrade to paid plan with Rules feature
- [ ] Add email rule for jonny@recho.co
- [ ] Test with form submission

### Option 3: Create Email Group
- [ ] Create leads@recho.co or submissions@recho.co group
- [ ] Add both emails as members
- [ ] Update Formspree to use group email
- [ ] Update contact.html form action (requires code change)

### Option 4: Switch Form Service
- [ ] Choose alternative service (Web3Forms, FormSubmit)
- [ ] Create new form endpoint
- [ ] Update contact.html with new action URL
- [ ] Test thoroughly

---

## 📧 Support

If you need help with any of these options:
- **Email Forwarding**: Contact your email hosting provider support
- **Formspree Dashboard**: Visit https://help.formspree.io
- **Alternative Services**: Check their documentation websites

---

**Updated**: February 16, 2026  
**Status**: Awaiting configuration choice  
**Recommendation**: Email forwarding (free, fast, no code changes)
