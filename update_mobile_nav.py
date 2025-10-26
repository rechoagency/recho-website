#!/usr/bin/env python3
"""
Update mobile navigation on all pages to use modern slide-in design
"""

import re

# Modern mobile navigation template
MOBILE_NAV_TEMPLATE = '''                <!-- Mobile Menu Button -->
                <div class="md:hidden">
                    <button id="mobile-menu-button" class="text-gray-700 hover:text-recho-orange focus:outline-none z-50 relative" aria-label="Toggle menu" aria-expanded="false">
                        <i class="fas fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Mobile Navigation Overlay -->
        <div id="mobile-menu-overlay" class="fixed inset-0 bg-black bg-opacity-50 z-40 hidden transition-opacity duration-300 md:hidden" aria-hidden="true"></div>
        
        <!-- Mobile Navigation Slide-in Panel -->
        <nav id="mobile-menu" class="fixed top-0 right-0 h-full w-80 max-w-full bg-white shadow-2xl transform translate-x-full transition-transform duration-300 ease-in-out z-50 md:hidden" aria-label="Mobile navigation">
            <div class="flex flex-col h-full">
                <!-- Mobile Menu Header -->
                <div class="flex items-center justify-between p-6 border-b border-gray-200">
                    <img src="images/recho-logo-corrected.png" alt="RECHO" class="h-12">
                    <button id="mobile-menu-close" class="text-gray-700 hover:text-recho-orange focus:outline-none" aria-label="Close menu">
                        <i class="fas fa-times text-2xl"></i>
                    </button>
                </div>
                
                <!-- Mobile Menu Links -->
                <div class="flex-1 overflow-y-auto py-6">
                    <div class="flex flex-col space-y-1 px-4">
                        <a href="services.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-briefcase w-6 text-recho-orange"></i>
                            Services
                        </a>
                        <a href="technology.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-microchip w-6 text-recho-orange"></i>
                            Technology
                        </a>
                        <a href="faq.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-question-circle w-6 text-recho-orange"></i>
                            FAQs
                        </a>
                        <a href="blog.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-blog w-6 text-recho-orange"></i>
                            Blog
                        </a>
                    </div>
                </div>
                
                <!-- Mobile Menu Footer CTA -->
                <div class="p-6 border-t border-gray-200">
                    <a href="contact.html" class="block w-full bg-recho-blue text-white px-6 py-4 rounded-lg hover:bg-recho-blue-dark transition-all duration-300 font-semibold text-center shadow-lg hover:shadow-xl">
                        <i class="fas fa-calendar-alt mr-2"></i>
                        Book a Call
                    </a>
                    <div class="mt-4 text-center">
                        <a href="mailto:sales@recho.co" class="text-gray-600 hover:text-recho-orange text-sm">
                            <i class="fas fa-envelope mr-2"></i>
                            sales@recho.co
                        </a>
                    </div>
                </div>
            </div>
        </nav>'''

# Template for blog posts (with ../ paths)
MOBILE_NAV_TEMPLATE_BLOG = '''                <!-- Mobile Menu Button -->
                <div class="md:hidden">
                    <button id="mobile-menu-button" class="text-gray-700 hover:text-recho-orange focus:outline-none z-50 relative" aria-label="Toggle menu" aria-expanded="false">
                        <i class="fas fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Mobile Navigation Overlay -->
        <div id="mobile-menu-overlay" class="fixed inset-0 bg-black bg-opacity-50 z-40 hidden transition-opacity duration-300 md:hidden" aria-hidden="true"></div>
        
        <!-- Mobile Navigation Slide-in Panel -->
        <nav id="mobile-menu" class="fixed top-0 right-0 h-full w-80 max-w-full bg-white shadow-2xl transform translate-x-full transition-transform duration-300 ease-in-out z-50 md:hidden" aria-label="Mobile navigation">
            <div class="flex flex-col h-full">
                <!-- Mobile Menu Header -->
                <div class="flex items-center justify-between p-6 border-b border-gray-200">
                    <img src="../images/recho-logo-corrected.png" alt="RECHO" class="h-12">
                    <button id="mobile-menu-close" class="text-gray-700 hover:text-recho-orange focus:outline-none" aria-label="Close menu">
                        <i class="fas fa-times text-2xl"></i>
                    </button>
                </div>
                
                <!-- Mobile Menu Links -->
                <div class="flex-1 overflow-y-auto py-6">
                    <div class="flex flex-col space-y-1 px-4">
                        <a href="../services.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-briefcase w-6 text-recho-orange"></i>
                            Services
                        </a>
                        <a href="../technology.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-microchip w-6 text-recho-orange"></i>
                            Technology
                        </a>
                        <a href="../faq.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-question-circle w-6 text-recho-orange"></i>
                            FAQs
                        </a>
                        <a href="../blog.html" class="mobile-nav-link px-4 py-3 text-gray-700 hover:bg-orange-50 hover:text-recho-orange rounded-lg transition-all duration-200 font-medium">
                            <i class="fas fa-blog w-6 text-recho-orange"></i>
                            Blog
                        </a>
                    </div>
                </div>
                
                <!-- Mobile Menu Footer CTA -->
                <div class="p-6 border-t border-gray-200">
                    <a href="../contact.html" class="block w-full bg-recho-blue text-white px-6 py-4 rounded-lg hover:bg-recho-blue-dark transition-all duration-300 font-semibold text-center shadow-lg hover:shadow-xl">
                        <i class="fas fa-calendar-alt mr-2"></i>
                        Book a Call
                    </a>
                    <div class="mt-4 text-center">
                        <a href="mailto:sales@recho.co" class="text-gray-600 hover:text-recho-orange text-sm">
                            <i class="fas fa-envelope mr-2"></i>
                            sales@recho.co
                        </a>
                    </div>
                </div>
            </div>
        </nav>'''

def update_mobile_nav(filepath, is_blog_post=False):
    """Update mobile navigation in a single file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match old mobile navigation
    # Matches from "<!-- Mobile Menu Button -->" to "</header>"
    pattern = r'(.*<!-- Mobile Menu Button -->.*?)</div>\s*\n\s*</div>\s*\n\s*</header>'
    
    # Find the match
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  ⚠️  Could not find mobile nav pattern in {filepath}")
        return False
    
    # Get everything before the mobile menu section
    before_mobile = content[:match.start()]
    
    # Get everything after </header>
    after_header = content[match.end():]
    
    # Choose template based on file type
    template = MOBILE_NAV_TEMPLATE_BLOG if is_blog_post else MOBILE_NAV_TEMPLATE
    
    # Reconstruct file
    new_content = before_mobile + template + '\n    </header>' + after_header
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    """Update all pages"""
    pages = [
        ('services.html', False),
        ('technology.html', False),
        ('faq.html', False),
        ('blog.html', False),
        ('contact.html', False),
    ]
    
    blog_posts = [
        'blog/how-to-build-an-engaged-reddit-community.html',
        'blog/why-your-reddit-strategy-is-failing.html',
        'blog/what-is-a-good-reddit-cpc-in-2025.html',
        'blog/what-new-reddit-ad-tools-launched-in-2025.html',
    ]
    
    print("🔧 Updating mobile navigation on all pages...\n")
    
    # Update main pages
    for page, is_blog in pages:
        print(f"Updating: {page}")
        if update_mobile_nav(page, is_blog):
            print(f"  ✅ Updated successfully")
        print()
    
    # Update blog posts
    for blog_post in blog_posts:
        print(f"Updating: {blog_post}")
        if update_mobile_nav(blog_post, is_blog_post=True):
            print(f"  ✅ Updated successfully")
        print()
    
    print("🎉 All pages updated with modern mobile navigation!")

if __name__ == '__main__':
    main()
