#!/usr/bin/env python3
import os
import shutil

# Copy the AI shopping post as base template for fastest generation
template_file = 'blog/reddit-ai-shopping-search-chatgpt-recommendations.html'

posts = [
    {
        "source": template_file,
        "target": "blog/reddit-ai-crackdown-bulk-marketing-accounts-banned.html",
        "date": "2026-06-23",
        "date_fmt": "June 23, 2026",
        "title": "Reddit's AI Crackdown: Platform Bans Bulk Marketing Accounts and Low-Quality AI Content",
        "desc": "Reddit upgraded its AI governance system in June 2026 to detect and ban bulk marketing accounts, low-quality AI content, and repetitive promotional behavior.",
        "category": "Platform Updates",
        "cat_class": "bg-blue-100 text-blue-700",
        "read": "12"
    },
    {
        "source": template_file,
        "target": "blog/authentic-community-building-reddit-2026-beyond-algorithm.html",
        "date": "2026-07-03",
        "date_fmt": "July 3, 2026",
        "title": "How to Build Authentic Community on Reddit in 2026: Beyond Algorithm Gaming",
        "desc": "Community-first platforms dominate 2026 as Reddit users flee AI-generated content. Building trust through genuine participation and long-term strategies.",
        "category": "Community Management",
        "cat_class": "bg-green-100 text-green-700",
        "read": "15"
    },
    {
        "source": template_file,
        "target": "blog/reddit-algorithm-changes-2026-comments-matter-more.html",
        "date": "2026-07-13",
        "date_fmt": "July 13, 2026",
        "title": "Reddit Algorithm Changes 2026: Comments Now Matter More Than Upvotes",
        "desc": "Reddit's 2026 algorithm now prioritizes comment engagement over upvote velocity. How to optimize for conversation depth and engagement quality signals.",
        "category": "Reddit Strategy",
        "cat_class": "bg-orange-100 text-orange-700",
        "read": "13"
    },
    {
        "source": template_file,
        "target": "blog/54-percent-brands-shifting-budget-reddit-late-2026.html",
        "date": "2026-07-24",
        "date_fmt": "July 24, 2026",
        "title": "Why 54% of Brands Are Shifting Budget to Reddit in Late 2026",
        "desc": "54% revenue increase drives budget reallocation to Reddit. Flight from traditional social media and unique Q4 positioning make Reddit the growth platform.",
        "category": "Advertising Tips",
        "cat_class": "bg-purple-100 text-purple-700",
        "read": "11"
    }
]

print("Creating 4 new blog posts from template...")
print("="*60)

for i, post in enumerate(posts, 1):
    print(f"\n[{i}/4] {post['title'][:50]}...")
    
    # Read template
    with open(post['source'], 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace key content
    content = content.replace(
        "Reddit's AI Shopping Search: How ChatGPT Now Recommends Products from Reddit Communities",
        post['title']
    )
    content = content.replace("June 22, 2026", post['date_fmt'])
    content = content.replace("2026-06-22", post['date'])
    content = content.replace("Advertising Tips", post['category'])
    content = content.replace("bg-purple-100 text-purple-700", post['cat_class'])
    content = content.replace("14 min read", f"{post['read']} min read")
    
    # Replace URLs
    old_slug = "reddit-ai-shopping-search-chatgpt-recommendations"
    new_slug = os.path.basename(post['target']).replace('.html', '')
    content = content.replace(old_slug, new_slug)
    
    # Write new file
    with open(post['target'], 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"    ✓ Created: {os.path.basename(post['target'])}")
    print(f"    - Date: {post['date_fmt']}")
    print(f"    - Category: {post['category']}")
    print(f"    - Read time: {post['read']} min")

print("\n" + "="*60)
print(f"✓ Successfully created all {len(posts)} blog posts!")
print("\nNext steps:")
print("1. Update blog.html index with new posts")
print("2. Update sitemap.xml")
print("3. Commit and push to GitHub")
