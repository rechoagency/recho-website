#!/usr/bin/env python3
"""
Standardize all headers and footers across the site to match index.html exactly.
This ensures consistent navigation order and styling on every page.
"""

import os
import re
from pathlib import Path

# Master desktop navigation (from index.html)
MASTER_DESKTOP_NAV = '''                <!-- Desktop Navigation -->
                <div class="hidden md:flex items-center space-x-8">
                    <div class="nav-item relative">
                        <a href="{services_path}services.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300 flex items-center">
                            Services
                            <i class="fas fa-chevron-down ml-1 text-xs"></i>
                        </a>
                        <div class="dropdown">
                            <a href="{services_path}services.html" class="border-b border-gray-100">
                                <i class="fas fa-th-large mr-2 text-recho-orange"></i>
                                All Services
                            </a>
                            <a href="{services_path}services/reddit-seo-geo.html">
                                <i class="fas fa-search mr-2 text-recho-orange"></i>
                                Reddit SEO & GEO
                            </a>
                            <a href="{services_path}services/brand-monitoring-social-listening.html">
                                <i class="fas fa-chart-line mr-2 text-recho-orange"></i>
                                Brand Monitoring & Social Listening
                            </a>
                        </div>
                    </div>
                    <a href="{services_path}code-of-conduct.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">Code of Conduct</a>
                    <a href="{services_path}technology.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">Technology</a>
                    <a href="{services_path}faq.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">FAQs</a>
                    <a href="{services_path}blog.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">Blog</a>
                    <a href="{services_path}contact.html" class="bg-recho-blue text-white px-6 py-2 rounded-full hover:bg-recho-blue-dark transition-all duration-300 font-medium shadow-lg hover:shadow-xl">
                        Book a Call
                    </a>
                </div>'''

# Master mobile navigation (from index.html)
MASTER_MOBILE_NAV = '''                <!-- Mobile Menu Links -->
<div class="flex-1 overflow-y-auto py-6">
                    <div class="flex flex-col space-y-1 px-4">
                        <a href="{services_path}services.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-briefcase w-6 text-recho-orange"></i>
                            All Services
                        </a>
                        <a href="{services_path}services/reddit-seo-geo.html" class="mobile-nav-link px-4 py-3 ml-4 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200">
                            <i class="fas fa-search w-6 text-recho-orange"></i>
                            Reddit SEO & GEO
                        </a>
                        <a href="{services_path}services/brand-monitoring-social-listening.html" class="mobile-nav-link px-4 py-3 ml-4 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200">
                            <i class="fas fa-shield-alt w-6 text-recho-orange"></i>
                            Brand Monitoring
                        </a>
                        <a href="{services_path}code-of-conduct.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-balance-scale w-6 text-recho-orange"></i>
                            Code of Conduct
                        </a>
                        <a href="{services_path}technology.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-microchip w-6 text-recho-orange"></i>
                            Technology
                        </a>
                        <a href="{services_path}faq.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-question-circle w-6 text-recho-orange"></i>
                            FAQs
                        </a>
                        <a href="{services_path}blog.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-blog w-6 text-recho-orange"></i>
                            Blog
                        </a>
                    </div>
                </div>'''

def standardize_page(filepath, is_blog_post=False):
    """Standardize header and footer for a page"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Determine path prefix based on file location
    services_path = "../" if is_blog_post else ""
    
    # Replace desktop navigation
    # Match from "<!-- Desktop Navigation -->" to the closing </div>
    desktop_pattern = r'(<!-- Desktop Navigation -->)\s*<div class="hidden md:flex[^>]*>.*?</div>\s*(?=\s*<!-- Mobile Menu Button -->)'
    desktop_replacement = MASTER_DESKTOP_NAV.format(services_path=services_path) + '\n                \n                '
    
    content = re.sub(desktop_pattern, desktop_replacement, content, flags=re.DOTALL)
    
    # Replace mobile navigation
    # Match from "<!-- Mobile Menu Links -->" to closing </div> (2 levels deep)
    mobile_pattern = r'(<!-- Mobile Menu Links -->)\s*<div class="flex-1[^>]*>.*?</div>\s*</div>'
    mobile_replacement = MASTER_MOBILE_NAV.format(services_path=services_path) + '\n                '
    
    content = re.sub(mobile_pattern, mobile_replacement, content, flags=re.DOTALL)
    
    # Write back if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = Path('/home/user/webapp')
    
    # Main pages to standardize (excluding index.html which is the master)
    main_pages = [
        'services.html',
        'technology.html',
        'faq.html',
        'blog.html',
        'contact.html',
        'privacy-policy.html',
        'code-of-conduct.html'
    ]
    
    print("=== Standardizing Headers & Footers ===\n")
    print("Master Template: index.html")
    print(f"Standard Order: Services → Code of Conduct → Technology → FAQs → Blog → Book a Call\n")
    
    updated_count = 0
    
    # Standardize main pages
    print("Main Pages:")
    for page in main_pages:
        filepath = base_dir / page
        if filepath.exists():
            if standardize_page(filepath):
                print(f"✓ Updated: {page}")
                updated_count += 1
            else:
                print(f"✗ Skipped: {page} (no changes needed)")
        else:
            print(f"⚠ Not found: {page}")
    
    # Standardize blog posts
    print("\nBlog Posts:")
    blog_dir = base_dir / 'blog'
    blog_posts = sorted(blog_dir.glob('*.html'))
    
    for filepath in blog_posts:
        if standardize_page(filepath, is_blog_post=True):
            print(f"✓ Updated: blog/{filepath.name}")
            updated_count += 1
    
    print(f"\n=== Total Updated: {updated_count} ===")

if __name__ == '__main__':
    main()
