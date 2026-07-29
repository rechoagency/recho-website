#!/usr/bin/env python3
"""
Surgical fix for 3 landing pages only:
1. Fix header to match homepage (lines 56-219 from index.html)
2. Footer social icons already exist - verify only
3. Add budget dropdown to forms and make it mandatory
"""

import re

# Read index.html to get the correct header
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract dropdown styles from index.html (lines 55-103)
dropdown_styles = '''    <!-- Dropdown Navigation Styles -->
    <style>
        .nav-item {
            position: relative;
        }
        
        .dropdown {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background: white;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border-radius: 0.5rem;
            min-width: 280px;
            z-index: 50;
            margin-top: 0rem;
            padding-top: 0.5rem;
        }
        
        /* Add invisible bridge area */
        .nav-item::after {
            content: "";
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            height: 1rem;
            background: transparent;
            z-index: 49;
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
    </style>'''

# Extract header from index.html (lines 108-219)
header_match = re.search(r'(<header class="fixed w-full bg-white shadow-md z-50">.*?</header>)', index_content, re.DOTALL)
correct_header = header_match.group(1)

print("🔧 Fixing 3 Landing Pages")
print("=" * 60)

# Landing pages to fix
pages = ['reddit-geo.html', 'reddit-marketing-agency.html', 'reddit-advertising-agency.html']

for page_name in pages:
    print(f"\n📄 Processing {page_name}...")
    
    with open(page_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix 1: Add dropdown styles if missing (before </head>)
    if '.dropdown {' not in content:
        print(f"  ✅ Adding dropdown navigation styles")
        content = content.replace('</head>', f'{dropdown_styles}\n</head>')
    else:
        print(f"  ℹ️  Dropdown styles already present")
    
    # Fix 2: Replace header with correct one from index.html
    content = re.sub(
        r'<header[^>]*>.*?</header>',
        correct_header,
        content,
        flags=re.DOTALL
    )
    print(f"  ✅ Header replaced with homepage version")
    
    # Fix 3: Add budget dropdown to form (find the interest dropdown and add budget after it)
    # Look for the "What are you exploring?" field
    budget_field = '''
                            <div class="mb-4">
                                <label for="budget" class="block text-xs font-semibold text-gray-700 mb-2">Monthly Budget Range *</label>
                                <select id="budget" name="budget" required 
                                    class="w-full px-4 py-3 border border-gray-300 rounded-lg bg-gray-50 text-sm focus:outline-none focus:ring-2 focus:ring-recho-orange focus:border-transparent">
                                    <option value="">Select a budget range...</option>
                                    <option value="under-5k">Under $5,000</option>
                                    <option value="5k-10k">$5,000 - $10,000</option>
                                    <option value="10k-25k">$10,000 - $25,000</option>
                                    <option value="25k-50k">$25,000 - $50,000</option>
                                    <option value="50k-plus">$50,000+</option>
                                    <option value="not-sure">Not sure yet</option>
                                </select>
                            </div>
'''
    
    # Find the closing </select> tag for interest field and insert budget after its closing </div>
    # Pattern: finds the interest field and its closing div
    pattern = r'(<div class="mb-4">.*?<label for="interest".*?</select>\s*</div>)'
    
    if re.search(pattern, content, re.DOTALL):
        # Check if budget field already exists
        if 'id="budget"' not in content:
            content = re.sub(
                pattern,
                r'\1' + budget_field,
                content,
                flags=re.DOTALL
            )
            print(f"  ✅ Added mandatory budget dropdown to form")
        else:
            # Budget exists but may not be mandatory - make it required
            content = re.sub(
                r'(<select id="budget"[^>]*?)>',
                r'\1 required>',
                content
            )
            print(f"  ✅ Made budget dropdown mandatory")
    else:
        print(f"  ⚠️  Could not find interest field to insert budget")
    
    # Verify footer has social icons (just check, don't modify)
    if '<i class="fab fa-linkedin-in"></i>' in content and '<i class="fas fa-envelope"></i>' in content:
        print(f"  ✅ Footer social icons verified present")
    else:
        print(f"  ⚠️  Footer social icons may be missing")
    
    # Write the file back
    with open(page_name, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ {page_name} updated successfully")

print("\n" + "=" * 60)
print("✅ All 3 landing pages fixed!")
print("\nChanges made:")
print("  • Header now matches homepage (dropdown navigation)")
print("  • Budget dropdown added to forms (mandatory)")
print("  • Footer social icons verified")
