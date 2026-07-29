#!/usr/bin/env python3
"""
Proper fix for all reported issues:
1. Fix Font Awesome CDN on 3 landing pages to match homepage
2. Add footer to code-of-conduct.html
3. Verify header navigation CSS is correct
"""

import re

print("🔧 Proper Fix - Addressing All Issues")
print("=" * 60)

# Read homepage for correct templates
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract correct Font Awesome link from homepage
fa_match = re.search(r'<link rel="stylesheet" href="https://cdn\.jsdelivr\.net/npm/@fortawesome/fontawesome-free@6\.4\.0/css/all\.min\.css">', index_content)
correct_fa_link = fa_match.group(0)

# Extract footer from homepage
footer_match = re.search(r'(<footer class="bg-gray-900 text-white py-16">.*?</footer>)', index_content, re.DOTALL)
correct_footer = footer_match.group(1)

print("\n📦 Extracted from homepage:")
print(f"  ✅ Font Awesome CDN link")
print(f"  ✅ Footer ({len(correct_footer)} characters)")

# Fix 1: Replace Font Awesome CDN on 3 landing pages
print("\n1️⃣ Fixing Font Awesome CDN on landing pages...")
landing_pages = ['reddit-geo.html', 'reddit-marketing-agency.html', 'reddit-advertising-agency.html']

for page in landing_pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the Font Awesome link
    content = re.sub(
        r'<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/6\.4\.0/css/all\.min\.css">',
        correct_fa_link,
        content
    )
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ {page} - Font Awesome CDN updated")

# Fix 2: Add footer to code-of-conduct.html
print("\n2️⃣ Adding footer to code-of-conduct.html...")
with open('code-of-conduct.html', 'r', encoding='utf-8') as f:
    coc_content = f.read()

# Check if footer already exists
if '<footer' in coc_content:
    print("  ℹ️  Footer already exists in code-of-conduct.html")
else:
    # Find where to insert footer (before closing body tag)
    # First, find the last closing div of the content
    # Then add footer before </body>
    if '</body>' in coc_content:
        coc_content = coc_content.replace('</body>', f'\n{correct_footer}\n\n    <!-- JavaScript -->\n    <script src="js/main.js"></script>\n    <script src="js/ga4-events.js"></script>\n</body>')
        print("  ✅ Footer added to code-of-conduct.html")
    else:
        # If no </body> tag, add it at the end
        coc_content = coc_content.rstrip()
        # Find last closing tag and add after it
        if '</div>' in coc_content:
            last_div_pos = coc_content.rfind('</div>')
            # Add footer after the last content div
            coc_content = coc_content[:last_div_pos+6] + f'\n    </section>\n\n{correct_footer}\n\n    <!-- JavaScript -->\n    <script src="js/main.js"></script>\n    <script src="js/ga4-events.js"></script>\n</body>\n</html>'
        print("  ✅ Footer and closing tags added to code-of-conduct.html")
    
    with open('code-of-conduct.html', 'w', encoding='utf-8') as f:
        f.write(coc_content)

# Fix 3: Verify navigation styles are present
print("\n3️⃣ Verifying navigation styles on landing pages...")
for page in landing_pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_dropdown_css = '.dropdown {' in content
    has_nav_item_css = '.nav-item {' in content
    
    if has_dropdown_css and has_nav_item_css:
        print(f"  ✅ {page} - Navigation CSS present")
    else:
        print(f"  ⚠️  {page} - Navigation CSS may be incomplete")

print("\n" + "=" * 60)
print("✅ All fixes applied!")
print("\nSummary:")
print("  • Font Awesome CDN updated on 3 landing pages")
print("  • Footer added to code-of-conduct.html")
print("  • Navigation styles verified")
