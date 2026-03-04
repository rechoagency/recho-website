#!/bin/bash

echo "======================================"
echo "RECHO.CO - Domain Reputation Check"
echo "Date: $(date)"
echo "======================================"
echo ""

# Check if domain resolves
echo "1. DNS Resolution Check:"
echo "------------------------"
getent hosts recho.co 2>&1 || echo "DNS resolution method not available"
echo ""

# Check SSL certificate
echo "2. SSL Certificate Check:"
echo "-------------------------"
echo | openssl s_client -servername recho.co -connect recho.co:443 2>/dev/null | openssl x509 -noout -dates -issuer -subject 2>&1
echo ""

# Check HTTP response
echo "3. HTTP Response Check:"
echo "-----------------------"
curl -I -s --max-time 10 https://recho.co/ 2>&1 | head -20
echo ""

# Check security headers
echo "4. Security Headers Check:"
echo "--------------------------"
echo "Checking for critical security headers..."
HEADERS=$(curl -I -s --max-time 10 https://recho.co/ 2>&1)
echo "$HEADERS" | grep -i "strict-transport-security" && echo "✓ HSTS: Present" || echo "✗ HSTS: Missing"
echo "$HEADERS" | grep -i "content-security-policy" && echo "✓ CSP: Present" || echo "✗ CSP: Missing"
echo "$HEADERS" | grep -i "x-frame-options" && echo "✓ X-Frame-Options: Present" || echo "✗ X-Frame-Options: Missing"
echo "$HEADERS" | grep -i "x-content-type-options" && echo "✓ X-Content-Type-Options: Present" || echo "✗ X-Content-Type-Options: Missing"
echo ""

# Check DNS records
echo "5. DNS Records Check:"
echo "---------------------"
echo "SPF Record:"
getent hosts -t txt recho.co 2>/dev/null | grep spf || echo "Checking via Python..."
python3 -c "import dns.resolver; print([str(r) for r in dns.resolver.resolve('recho.co', 'TXT')])" 2>/dev/null || echo "DNS library not available"
echo ""

echo "MX Records:"
getent hosts -t mx recho.co 2>/dev/null || python3 -c "import dns.resolver; print([str(r) for r in dns.resolver.resolve('recho.co', 'MX')])" 2>/dev/null || echo "DNS library not available"
echo ""

# Check common security lists
echo "6. Reputation Database Checks:"
echo "------------------------------"
echo "Note: These require manual verification at vendor websites"
echo ""
echo "Symantec WebPulse: https://sitereview.bluecoat.com/?url=recho.co"
echo "Fortinet FortiGuard: https://www.fortiguard.com/webfilter?q=recho.co"
echo "Palo Alto URL Filtering: https://urlfiltering.paloaltonetworks.com"
echo "VirusTotal: https://www.virustotal.com/gui/domain/recho.co"
echo "URLVoid: https://www.urlvoid.com/scan/recho.co/"
echo "Talos Intelligence: https://talosintelligence.com/reputation_center/lookup?search=recho.co"
echo ""

echo "7. Email Blacklist Checks:"
echo "--------------------------"
echo "MXToolbox Blacklists: https://mxtoolbox.com/SuperTool.aspx?action=blacklist%3arecho.co"
echo "Spamhaus: https://check.spamhaus.org/"
echo "SORBS: http://www.sorbs.net/lookup.shtml"
echo ""

echo "======================================"
echo "SCAN COMPLETE"
echo "======================================"
echo ""
echo "NEXT STEPS:"
echo "1. Visit each reputation URL above and check status"
echo "2. Submit domain for recategorization if 'Uncategorized'"
echo "3. Run email deliverability test: https://www.mail-tester.com"
echo ""
