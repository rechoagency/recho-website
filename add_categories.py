#!/usr/bin/env python3
"""
Add data-category attributes to all blog post cards for filtering
"""
import re

# Read the blog.html file
with open('/home/user/webapp/blog.html', 'r') as f:
    content = f.read()

# Pattern to find blog post links and their categories
# We need to find: <a href="blog/...html" class="block"> followed by the category span
pattern = r'(<a href="blog/[^"]+\.html" class="block")(\s+data-category="[^"]+")?(>.*?<span class="px-3 py-1[^"]*text-xs rounded-full font-semibold">)([^<]+)(</span>)'

def add_category(match):
    link_open = match.group(1)
    existing_data = match.group(2)  # May be None
    middle_part = match.group(3)
    category = match.group(4)
    span_close = match.group(5)
    
    # If already has data-category, skip
    if existing_data:
        return match.group(0)
    
    # Add data-category attribute
    return f'{link_open} data-category="{category}"{middle_part}{category}{span_close}'

# Apply the replacement
updated_content = re.sub(pattern, add_category, content, flags=re.DOTALL)

# Count how many were updated
original_count = content.count('class="block">')
updated_count = updated_content.count('data-category="')

print(f"✅ Added data-category attributes")
print(f"   Total blog links: {original_count}")
print(f"   Links with data-category: {updated_count}")

# Write back
with open('/home/user/webapp/blog.html', 'w') as f:
    f.write(updated_content)

print("✅ blog.html updated successfully!")
