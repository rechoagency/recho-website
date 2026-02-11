#!/usr/bin/env python3
"""
Comprehensive blog.html fixes:
1. Change Ads → Advertising Tips
2. Change Global Growth → Platform Updates  
3. Add data-category attributes to all blog links
4. Add category filtering JavaScript
"""

# Read blog.html
with open('/home/user/webapp/blog.html', 'r') as f:
    content = f.read()

# 1. Fix category badges
content = content.replace(
    '<span class="px-3 py-1 bg-red-100 text-red-700 text-xs rounded-full font-semibold">Ads</span>',
    '<span class="px-3 py-1 bg-purple-100 text-purple-700 text-xs rounded-full font-semibold">Advertising Tips</span>'
)

content = content.replace(
    '<span class="px-3 py-1 bg-green-100 text-green-700 text-xs rounded-full font-semibold">Global Growth</span>',
    '<span class="px-3 py-1 bg-blue-100 text-blue-700 text-xs rounded-full font-semibold">Platform Updates</span>'
)

# Also change the icon for Reddit Overtakes TikTok post to match Platform Updates style
content = content.replace(
    '''                        <div class="bg-gradient-to-br from-green-600 to-green-800 h-48 flex items-center justify-center">
                            <i class="fas fa-globe-europe text-white text-5xl"></i>
                        </div>
                        <div class="p-6">
                            <div class="flex items-center gap-2 mb-3">
                                <span class="px-3 py-1 bg-blue-100 text-blue-700 text-xs rounded-full font-semibold">Platform Updates</span>
                                <span class="text-gray-500 text-xs">January 29, 2026</span>''',
    '''                        <div class="bg-gradient-to-br from-blue-600 to-blue-800 h-48 flex items-center justify-center">
                            <i class="fas fa-bell text-white text-5xl"></i>
                        </div>
                        <div class="p-6">
                            <div class="flex items-center gap-2 mb-3">
                                <span class="px-3 py-1 bg-blue-100 text-blue-700 text-xs rounded-full font-semibold">Platform Updates</span>
                                <span class="text-gray-500 text-xs">January 29, 2026</span>'''
)

# 2. Add data-category attributes to blog post links
blog_categories = {
    'brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search.html': 'Advertising Tips',
    'reddit-overtakes-tiktok-uk-international-growth-2026.html': 'Platform Updates',
    'how-much-do-reddit-ads-cost-in-2026.html': 'Advertising Tips',
    'reddit-max-campaigns-what-advertisers-need-to-know.html': 'Platform Updates',
    'how-to-measure-reddit-impact-google-ai-overviews.html': 'Reddit Strategy',
    'reddit-leads-ad-spend-growth-at-46-percent-2025.html': 'Platform Updates',
    'why-brand-reddit-posts-rank-in-google-and-chatgpt.html': 'Reddit Strategy',
    'is-reddit-marketing-worth-it-in-2026.html': 'Reddit Strategy',
    'how-to-grow-a-subreddit-from-zero-to-10000-members.html': 'Community Management',
    'how-reddit-pro-social-listening-tools-are-changing-marketing.html': 'Platform Updates',
    'which-brands-are-winning-with-reddit-ads.html': 'Advertising Tips',
    'how-to-work-with-reddit-moderators.html': 'Reddit Strategy',
    'how-to-build-an-engaged-reddit-community.html': 'Community Management',
    'why-your-reddit-strategy-is-failing.html': 'Reddit Strategy',
    'what-is-a-good-reddit-cpc-in-2025.html': 'Advertising Tips',
    'what-new-reddit-ad-tools-launched-in-2025.html': 'Platform Updates'
}

for filename, category in blog_categories.items():
    old = f'<a href="blog/{filename}" class="block">'
    new = f'<a href="blog/{filename}" class="block" data-category="{category}">'
    content = content.replace(old, new)

# 3. Add filtering JavaScript before closing body tag
# First, find where to insert it
insert_point = content.rfind('</body>')
if insert_point == -1:
    # If no </body> tag, add before final </html>
    insert_point = content.rfind('</html>')

if insert_point != -1:
    filter_script = '''
    <!-- Blog Category Filtering Script -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const categoryButtons = document.querySelectorAll('.category-tag');
        const blogCards = document.querySelectorAll('[data-category]');
        
        categoryButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Update active button styling
                categoryButtons.forEach(btn => {
                    btn.classList.remove('bg-recho-orange', 'text-white');
                    btn.classList.add('bg-gray-200', 'text-gray-700');
                });
                this.classList.remove('bg-gray-200', 'text-gray-700');
                this.classList.add('bg-recho-orange', 'text-white');
                
                // Filter blog cards
                const selectedCategory = this.textContent.trim();
                
                blogCards.forEach(card => {
                    if (selectedCategory === 'All Posts' || card.getAttribute('data-category') === selectedCategory) {
                        card.style.display = 'block';
                        // Add fade-in animation
                        card.style.opacity = '0';
                        setTimeout(() => {
                            card.style.transition = 'opacity 0.3s ease-in';
                            card.style.opacity = '1';
                        }, 10);
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    });
    </script>

'''
    content = content[:insert_point] + filter_script + content[insert_point:]

# Write the updated content
with open('/home/user/webapp/blog.html', 'w') as f:
    f.write(content)

print("✅ All blog.html fixes applied successfully!")
print("   - Changed 'Ads' → 'Advertising Tips'")
print("   - Changed 'Global Growth' → 'Platform Updates'")
print(f"   - Added {len(blog_categories)} data-category attributes")
print("   - Added category filtering JavaScript")
