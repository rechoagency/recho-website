#!/usr/bin/env python3
"""
Update all blog post navigation headers to include Code of Conduct link
"""

import os
import glob

def update_blog_post(filepath):
    """Update a single blog post file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Desktop navigation update - Pattern 1 (font-medium on FAQs)
    old_desktop_1 = '''                    <a href="../technology.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">Technology</a>
                    <a href="../faq.html" class="text-gray-700 hover:text-recho-orange transition-colors font-medium">FAQs</a>'''
    
    new_desktop_1 = '''                    <a href="../technology.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">Technology</a>
                    <a href="../code-of-conduct.html" class="text-gray-700 hover:text-recho-orange transition-colors font-medium">Code of Conduct</a>
                    <a href="../faq.html" class="text-gray-700 hover:text-recho-orange transition-colors font-medium">FAQs</a>'''
    
    # Desktop navigation update - Pattern 2 (nav-link on FAQs)
    old_desktop_2 = '''                    <a href="../technology.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">Technology</a>
                    <a href="../faq.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">FAQs</a>'''
    
    new_desktop_2 = '''                    <a href="../technology.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">Technology</a>
                    <a href="../code-of-conduct.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">Code of Conduct</a>
                    <a href="../faq.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">FAQs</a>'''
    
    # Mobile navigation update
    old_mobile = '''                        <a href="../technology.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-microchip w-6 text-recho-orange"></i>
                            Technology
                        </a>
                        <a href="../faq.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">'''
    
    new_mobile = '''                        <a href="../technology.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-microchip w-6 text-recho-orange"></i>
                            Technology
                        </a>
                        <a href="../code-of-conduct.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-balance-scale w-6 text-recho-orange"></i>
                            Code of Conduct
                        </a>
                        <a href="../faq.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">'''
    
    # Apply updates
    updated = False
    if old_desktop_1 in content:
        content = content.replace(old_desktop_1, new_desktop_1)
        updated = True
    elif old_desktop_2 in content:
        content = content.replace(old_desktop_2, new_desktop_2)
        updated = True
    
    if old_mobile in content:
        content = content.replace(old_mobile, new_mobile)
        updated = True
    
    # Write back if changes were made
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    blog_dir = '/home/user/webapp/blog'
    blog_posts = glob.glob(os.path.join(blog_dir, '*.html'))
    
    print(f"Found {len(blog_posts)} blog post files")
    
    updated_count = 0
    for filepath in sorted(blog_posts):
        filename = os.path.basename(filepath)
        if update_blog_post(filepath):
            print(f"✓ Updated: {filename}")
            updated_count += 1
        else:
            print(f"✗ Skipped (already updated or pattern not found): {filename}")
    
    print(f"\nTotal updated: {updated_count}/{len(blog_posts)}")

if __name__ == '__main__':
    main()
