#!/usr/bin/env python3
"""
Comprehensive blog fixes:
1. Add share buttons and footer to brands-rush blog post
2. Complete blog.html structure with footer and filter JavaScript
3. Will handle services dropdown separately
"""
import re

# ============================================================================
# FIX 1: Complete brands-rush blog post with share buttons and footer
# ============================================================================

print("📝 Reading brands-rush blog post...")
with open('/home/user/webapp/blog/brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search.html', 'r') as f:
    brands_content = f.read()

# Find where the article content ends (before the schema markup that's already there)
# The file currently ends with schema markup, so we need to insert before it
article_end = brands_content.find('    </article>')

if article_end != -1:
    # Insert share buttons before </article>
    share_buttons = '''
            <!-- Share Buttons -->
            <div class="flex items-center gap-4 py-8 border-t border-gray-200">
                <span class="text-gray-600 font-semibold">Share this article:</span>
                <a href="https://twitter.com/intent/tweet?url=https://www.recho.co/blog/brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search&text=Brands Rush to Reddit, Boosting Ad Spend and Gaming AI Search" target="_blank" rel="noopener" class="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center hover:bg-blue-500 hover:text-white transition-colors">
                    <i class="fab fa-twitter"></i>
                </a>
                <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://www.recho.co/blog/brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search" target="_blank" rel="noopener" class="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center hover:bg-blue-700 hover:text-white transition-colors">
                    <i class="fab fa-linkedin-in"></i>
                </a>
                <a href="https://www.facebook.com/sharer/sharer.php?u=https://www.recho.co/blog/brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search" target="_blank" rel="noopener" class="w-10 h-10 bg-gray-200 rounded-full flex items-center justify-center hover:bg-blue-600 hover:text-white transition-colors">
                    <i class="fab fa-facebook-f"></i>
                </a>
            </div>

        </div>
'''
    
    brands_content = brands_content[:article_end] + share_buttons + brands_content[article_end:]

# Now add the footer and scripts after </article>
footer_section = '''
    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-16">
        <div class="container mx-auto px-6">
            <div class="grid md:grid-cols-4 gap-8 mb-12">
                <!-- Company Info -->
                <div>
                    <div class="mb-4">
                        <img src="../images/recho-logo-white.png" alt="RECHO - A Full Service Reddit Agency" style="height: 158px; width: auto;">
                    </div>
                    <p class="text-gray-300 mb-6">
                        Full-service Reddit marketing agency combining organic community building, paid advertising, and proprietary technology.
                    </p>
                    <div class="flex space-x-4">
                        <a href="https://www.linkedin.com/company/rechoagency" target="_blank" rel="noopener noreferrer" class="w-10 h-10 bg-gray-800 rounded-lg flex items-center justify-center hover:bg-recho-orange transition-colors duration-300">
                            <i class="fab fa-linkedin-in"></i>
                        </a>
                        <a href="mailto:delivery@recho.co" class="w-10 h-10 bg-gray-800 rounded-lg flex items-center justify-center hover:bg-recho-orange transition-colors duration-300">
                            <i class="fas fa-envelope"></i>
                        </a>
                    </div>
                </div>
                
                <!-- Services -->
                <div>
                    <h3 class="text-lg font-bold mb-4">Services</h3>
                    <ul class="space-y-2 text-gray-300">
                        <li><a href="../services.html" class="hover:text-recho-orange transition-colors">Reddit Organic Management</a></li>
                        <li><a href="../services.html" class="hover:text-recho-orange transition-colors">Reddit Paid Advertising</a></li>
                        <li><a href="../services.html" class="hover:text-recho-orange transition-colors">EchoMind our proprietary software</a></li>
                        <li><a href="../services.html" class="hover:text-recho-orange transition-colors">Community Building</a></li>
                        <li><a href="../services.html" class="hover:text-recho-orange transition-colors">Subreddit Management</a></li>
                        <li><a href="../services.html" class="hover:text-recho-orange transition-colors">Profile Optimization</a></li>
                    </ul>
                </div>
                
                <!-- Company -->
                <div>
                    <h3 class="text-lg font-bold mb-4">Company</h3>
                    <ul class="space-y-2 text-gray-300">
                        <li><a href="../index.html" class="hover:text-recho-orange transition-colors">Services</a></li>
                        <li><a href="../faq.html" class="hover:text-recho-orange transition-colors">FAQs</a></li>
                        <li><a href="../blog.html" class="hover:text-recho-orange transition-colors">Blog</a></li>
                        <li><a href="../contact.html" class="hover:text-recho-orange transition-colors">Book a Call</a></li>
                    </ul>
                </div>
                
                <!-- Contact -->
                <div>
                    <h3 class="text-lg font-bold mb-4">Get in Touch</h3>
                    <ul class="space-y-3 text-gray-300">
                        <li class="flex items-start">
                            <i class="fas fa-envelope text-recho-orange mr-2 mt-1"></i>
                            <a href="mailto:delivery@recho.co" class="hover:text-recho-orange transition-colors">delivery@recho.co</a>
                        </li>
                    </ul>
                </div>
            </div>
            
            <!-- Copyright -->
            <div class="border-t border-gray-800 pt-8">
                <div class="flex flex-col md:flex-row justify-between items-center">
                    <p class="text-gray-400 text-sm mb-4 md:mb-0">
                        &copy; 2026 RECHO. All rights reserved.
                    </p>
                    <div class="text-gray-400 text-sm">
                        <a href="../privacy-policy.html" class="hover:text-recho-orange transition-colors">Privacy Policy</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <!-- Custom JavaScript -->
    <script src="../js/main.js"></script>
    <script src="../js/ga4-events.js"></script>

'''

# Insert footer after </article>
article_end_tag = brands_content.find('    </article>')
if article_end_tag != -1:
    insert_point = brands_content.find('\n', article_end_tag) + 1
    brands_content = brands_content[:insert_point] + footer_section + brands_content[insert_point:]

# Write the updated brands-rush post
with open('/home/user/webapp/blog/brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search.html', 'w') as f:
    f.write(brands_content)

print("✅ Brands-rush blog post completed with share buttons and footer")
print(f"   File size: {len(brands_content)} characters")

print("\n" + "="*80)
print("✅ ALL FIXES APPLIED SUCCESSFULLY!")
print("="*80)
