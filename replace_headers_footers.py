#!/usr/bin/env python3
"""
Replace slim headers and simple footers with global header/footer on landing pages
"""

import re

# Read global header and footer templates
with open('global_header_template.html', 'r', encoding='utf-8') as f:
    global_header = f.read()

with open('global_footer_template.html', 'r', encoding='utf-8') as f:
    global_footer = f.read()

# Landing pages to update
pages = [
    'reddit-geo.html',
    'reddit-marketing-agency.html',
    'reddit-advertising-agency.html'
]

for page in pages:
    print(f"\nProcessing {page}...")
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace slim header with global header
    # Find the current header section
    header_pattern = r'    <!-- Slim Header -->\n    <header class="bg-white border-b border-gray-200 sticky top-0 z-50">.*?</header>'
    
    if re.search(header_pattern, content, re.DOTALL):
        content = re.sub(header_pattern, global_header, content, flags=re.DOTALL)
        print(f"  ✅ Replaced header")
    else:
        print(f"  ⚠️  Could not find header pattern")
    
    # Replace simple footer with global footer
    # Find current footer section
    footer_pattern = r'    <!-- Footer -->\n    <footer class="bg-white border-t border-gray-200 py-6">.*?</footer>'
    
    if re.search(footer_pattern, content, re.DOTALL):
        content = re.sub(footer_pattern, global_footer, content, flags=re.DOTALL)
        print(f"  ✅ Replaced footer")
    else:
        print(f"  ⚠️  Could not find footer pattern")
    
    # Write updated content
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Saved {page}")

print("\n✅ All landing pages updated with global header/footer!")
