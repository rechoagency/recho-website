#!/usr/bin/env python3
"""
Fix all blog posts with proper Services dropdown navigation
"""

import os
import re

# Services dropdown HTML with proper structure
SERVICES_DROPDOWN = '''<div class="nav-item relative">
                        <a href="../services.html" class="text-gray-700 hover:text-recho-orange font-medium flex items-center gap-1">
                            Services
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="dropdown">
                            <a href="../services.html" class="text-sm">All Services</a>
                            <a href="../services/reddit-seo-geo.html" class="text-sm">Reddit SEO & GEO</a>
                            <a href="../services/brand-monitoring-social-listening.html" class="text-sm">Brand Monitoring & Social Listening</a>
                        </div>
                    </div>'''

# Old Services link pattern (simple link without dropdown)
OLD_SERVICES_PATTERN = r'<a\s+href="\.\.\/services\.html"[^>]*>Services<\/a>'

def fix_blog_post(filepath):
    """Fix a single blog post file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has dropdown (skip if already fixed)
        if 'nav-item relative' in content and 'Services' in content and 'dropdown' in content:
            print(f"✓ Already fixed: {os.path.basename(filepath)}")
            return False
        
        # Replace old Services link with dropdown version
        original_content = content
        content = re.sub(OLD_SERVICES_PATTERN, SERVICES_DROPDOWN, content)
        
        # Check if we made changes
        if content == original_content:
            print(f"⚠ No changes needed: {os.path.basename(filepath)}")
            return False
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Fixed: {os.path.basename(filepath)}")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing {filepath}: {str(e)}")
        return False

def main():
    blog_dir = '/home/user/webapp/blog'
    
    # Get all HTML files
    html_files = [f for f in os.listdir(blog_dir) if f.endswith('.html') and not f.endswith('.bak')]
    
    print(f"Found {len(html_files)} blog post files")
    print("=" * 60)
    
    fixed_count = 0
    for filename in sorted(html_files):
        filepath = os.path.join(blog_dir, filename)
        if fix_blog_post(filepath):
            fixed_count += 1
    
    print("=" * 60)
    print(f"✅ Fixed {fixed_count} blog posts")
    print(f"Total blog posts: {len(html_files)}")

if __name__ == '__main__':
    main()
