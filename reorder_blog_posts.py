#!/usr/bin/env python3
"""
Reorder blog posts on blog.html by date (most recent first)
"""

from datetime import datetime
import re

def extract_date_from_post(post_html):
    """Extract date from blog post HTML"""
    # Look for date in format "June 22, 2026" or "July 24, 2026"
    date_match = re.search(r'<span class="text-gray-500 text-xs">([^<]+)</span>', post_html)
    if date_match:
        date_str = date_match.group(1)
        try:
            # Parse date
            date_obj = datetime.strptime(date_str, "%B %d, %Y")
            return date_obj
        except:
            try:
                # Try alternate format like "March 31, 2026"
                date_obj = datetime.strptime(date_str, "%B %d, %Y")
                return date_obj
            except:
                print(f"Could not parse date: {date_str}")
                return None
    return None

def main():
    # Read blog.html
    with open('/home/user/webapp/blog.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the blog posts grid section
    grid_start = content.find('<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto">')
    if grid_start == -1:
        print("Could not find blog grid")
        return
    
    # Find where the grid ends (looking for the closing div tags before Footer)
    grid_end = content.find('\n            </div>\n        </div>\n    </section>\n\n    <!-- Footer -->', grid_start)
    if grid_end == -1:
        print("Could not find grid end")
        return
    
    # Extract the grid content
    grid_content = content[grid_start:grid_end + 6]  # +6 for </div>
    
    # Split into individual blog posts
    # Each post starts with <!-- Blog Post
    post_pattern = r'(<!-- Blog Post.*?</a>)'
    posts = re.findall(post_pattern, grid_content, re.DOTALL)
    
    print(f"Found {len(posts)} blog posts")
    
    # Parse dates and create list of (date, post_html) tuples
    dated_posts = []
    for post in posts:
        date = extract_date_from_post(post)
        if date:
            dated_posts.append((date, post))
            print(f"Parsed: {date.strftime('%B %d, %Y')}")
        else:
            print(f"WARNING: Could not parse date from post")
            # Still include it at the end
            dated_posts.append((datetime(1900, 1, 1), post))
    
    # Sort by date (most recent first)
    dated_posts.sort(key=lambda x: x[0], reverse=True)
    
    print("\nNew order (after sorting):")
    for i, (date, post) in enumerate(dated_posts, 1):
        print(f"{i}. {date.strftime('%B %d, %Y')}")
    
    # Reconstruct the grid with sorted posts
    new_grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto">\n'
    for date, post in dated_posts:
        new_grid += '                ' + post + '\n\n'
    new_grid += '            </div>'
    
    # Replace in content
    new_content = content[:grid_start] + new_grid + content[grid_end + 6:]
    
    # Write back
    with open('/home/user/webapp/blog.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("\n✅ Blog posts reordered successfully!")

if __name__ == '__main__':
    main()
