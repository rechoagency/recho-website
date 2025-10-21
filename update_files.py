#!/usr/bin/env python3
import re

# Update function for adding brand icon to header
def add_brand_icon_to_header(content):
    # Pattern to find logo section
    old_pattern = r'(<a href="index\.html" class="flex items-center space-x-3 cursor-pointer">)\s*(<img src="images/recho-logo\.svg")'
    new_text = r'\1\n                    <img src="images/recho-icon.png" alt="RECHO Icon" class="h-10 w-10">\n                    \2'
    return re.sub(old_pattern, new_text, content)

# Update function for adding brand icon to footer  
def add_brand_icon_to_footer(content):
    # Pattern to find footer logo
    old_pattern = r'(<div class="md:col-span-2">)\s*(<img src="images/recho-logo\.svg"[^>]+>)'
    new_text = r'\1\n                    <div class="flex items-center space-x-3 mb-4">\n                        <img src="images/recho-icon.png" alt="RECHO Icon" class="h-8 w-8 brightness-0 invert">\n                        <img src="images/recho-logo.svg" alt="RECHO Logo" class="h-10 brightness-0 invert">\n                    </div>'
    content = re.sub(old_pattern, new_text, content)
    # Remove standalone logo img that we just wrapped
    content = re.sub(r'\s*<img src="images/recho-logo\.svg" alt="RECHO Logo" class="h-10 mb-4 brightness-0 invert">', '', content)
    return content

# Update Services link in navigation
def update_services_link(content):
    content = re.sub(r'<a href="index\.html" class="nav-link([^"]*)"([^>]*)>Services</a>',
                    r'<a href="services.html" class="nav-link\1"\2>Services</a>', content)
    content = re.sub(r'<a href="index\.html"([^>]*)>Services</a>',
                    r'<a href="services.html"\1>Services</a>', content)
    return content

# Files to update
files_to_update = ['blog.html', 'contact.html']

for filename in files_to_update:
    filepath = f'/home/user/webapp/{filename}'
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Apply all updates
        content = add_brand_icon_to_header(content)
        content = add_brand_icon_to_footer(content)
        content = update_services_link(content)
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"✅ Updated {filename}")
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")

print("\n✅ All files updated successfully!")
