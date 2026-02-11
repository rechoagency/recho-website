#!/usr/bin/env python3
"""
Add dropdown CSS to all blog posts
"""

import os
import re

# Dropdown CSS to add
DROPDOWN_CSS = '''        /* Dropdown Navigation Styles */
        .nav-item {
            position: relative;
        }
        
        .dropdown {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            border-radius: 0.5rem;
            min-width: 280px;
            z-index: 50;
            margin-top: 0;
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
        }
        
        /* Add invisible bridge area */
        .nav-item::after {
            content: '';
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            height: 0.5rem;
        }
        
        .nav-item:hover .dropdown {
            display: block;
        }
        
        .dropdown a {
            display: block;
            padding: 0.75rem 1.25rem;
            color: #374151;
            transition: all 0.2s;
        }
        
        .dropdown a:hover {
            background-color: #FFF7ED;
            color: #E6462F;
            padding-left: 1.5rem;
        }
'''

def add_css_to_post(filepath):
    """Add dropdown CSS to a blog post"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has dropdown CSS
        if '.nav-item:hover .dropdown' in content:
            print(f"✓ Already has CSS: {os.path.basename(filepath)}")
            return False
        
        # Find the closing </style> tag before </head>
        # Look for the last </style> before </head>
        head_match = re.search(r'</head>', content)
        if not head_match:
            print(f"⚠ No </head> found: {os.path.basename(filepath)}")
            return False
        
        # Find the last </style> before </head>
        head_pos = head_match.start()
        head_content = content[:head_pos]
        
        # Find last </style> in head section
        style_matches = list(re.finditer(r'</style>', head_content))
        
        if not style_matches:
            # No style tag found, add new style block before </head>
            css_block = f'    <style>\n{DROPDOWN_CSS}    </style>\n'
            new_content = content[:head_pos] + css_block + content[head_pos:]
        else:
            # Insert CSS before the last </style>
            last_style_pos = style_matches[-1].start()
            new_content = content[:last_style_pos] + DROPDOWN_CSS + '\n' + content[last_style_pos:]
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Added CSS: {os.path.basename(filepath)}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {filepath}: {str(e)}")
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
        if add_css_to_post(filepath):
            fixed_count += 1
    
    print("=" * 60)
    print(f"✅ Added CSS to {fixed_count} blog posts")
    print(f"Total blog posts: {len(html_files)}")

if __name__ == '__main__':
    main()
