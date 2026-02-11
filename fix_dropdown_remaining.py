#!/usr/bin/env python3
"""
Add Services dropdown to remaining blog post pages
"""
import os
import glob

# The old structure for files with <div> navigation
old_nav_div = '''                <div class="hidden md:flex items-center space-x-8">
                    <a href="../services.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300">Services</a>'''

# The new structure with dropdown
new_nav_div = '''                <div class="hidden md:flex items-center space-x-8">
                    <div class="nav-item relative">
                        <a href="../services.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300 flex items-center">
                            Services
                            <i class="fas fa-chevron-down ml-1 text-xs"></i>
                        </a>
                        <div class="dropdown">
                            <a href="../services.html" class="border-b border-gray-100">
                                <i class="fas fa-th-large mr-2 text-recho-orange"></i>
                                All Services
                            </a>
                            <a href="../services/reddit-seo-geo.html">
                                <i class="fas fa-search mr-2 text-recho-orange"></i>
                                Reddit SEO & GEO
                            </a>
                            <a href="../services/brand-monitoring-social-listening.html">
                                <i class="fas fa-chart-line mr-2 text-recho-orange"></i>
                                Brand Monitoring & Social Listening
                            </a>
                        </div>
                    </div>'''

# Get all blog post HTML files
blog_posts = glob.glob('/home/user/webapp/blog/*.html')

fixed_count = 0
for blog_post in blog_posts:
    with open(blog_post, 'r') as f:
        content = f.read()
    
    # Check if it needs fixing (has old structure)
    if old_nav_div in content and '<div class="nav-item relative">' not in content:
        # Replace the nav structure
        content = content.replace(old_nav_div, new_nav_div)
        
        with open(blog_post, 'w') as f:
            f.write(content)
        
        fixed_count += 1
        print(f"✅ Fixed: {os.path.basename(blog_post)}")

print(f"\n✅ Updated {fixed_count} more blog post files with Services dropdown")
