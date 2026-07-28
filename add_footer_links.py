#!/usr/bin/env python3
"""
Add orphan landing page links to footer Company section across all pages
"""

import os
import glob

# Footer links to add (these go after "Book a Call" link)
footer_links = '''                        <li><a href="reddit-geo.html" class="hover:text-recho-orange transition-colors text-gray-400 text-sm">Reddit GEO</a></li>
                        <li><a href="reddit-marketing-agency.html" class="hover:text-recho-orange transition-colors text-gray-400 text-sm">Reddit Marketing Agency</a></li>
                        <li><a href="reddit-advertising-agency.html" class="hover:text-recho-orange transition-colors text-gray-400 text-sm">Reddit Advertising Agency</a></li>'''

# Find the insertion point pattern
insertion_pattern = '''                        <li><a href="contact.html" class="hover:text-recho-orange transition-colors">Book a Call</a></li>
                    </ul>'''

replacement = '''                        <li><a href="contact.html" class="hover:text-recho-orange transition-colors">Book a Call</a></li>
''' + footer_links + '''
                    </ul>'''

# Files to update (main site pages with footers, excluding landing pages and thank you)
files_to_update = [
    'index.html',
    'services.html',
    'blog.html',
    'contact.html',
    'faq.html',
    'technology.html',
    'code-of-conduct.html'
]

# Also update blog post pages
blog_files = glob.glob('blog/*.html')
files_to_update.extend(blog_files)

# Also update service pages
service_files = glob.glob('services/*.html')
files_to_update.extend(service_files)

print(f"Updating {len(files_to_update)} files...")

for file_path in files_to_update:
    if not os.path.exists(file_path):
        print(f"  ⚠️  Skipping {file_path} (not found)")
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already updated
        if 'reddit-geo.html' in content:
            print(f"  ⏭️  Skipping {file_path} (already updated)")
            continue
        
        # Check if insertion pattern exists
        if insertion_pattern not in content:
            print(f"  ⚠️  Skipping {file_path} (pattern not found)")
            continue
        
        # Replace
        new_content = content.replace(insertion_pattern, replacement)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ Updated {file_path}")
    
    except Exception as e:
        print(f"  ❌ Error updating {file_path}: {e}")

print("\n✅ Footer links added successfully!")
