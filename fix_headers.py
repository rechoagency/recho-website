import os
import re
from pathlib import Path

# Read the master header from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the header section from index.html (including CSS)
# Get CSS for dropdown navigation
dropdown_css_match = re.search(r'<!-- Dropdown Navigation Styles -->.*?</style>', index_content, re.DOTALL)
dropdown_css = dropdown_css_match.group(0) if dropdown_css_match else ""

# Get the header HTML
header_match = re.search(r'<!-- Header/Navigation -->.*?</header>', index_content, re.DOTALL)
master_header = header_match.group(0) if header_match else ""

print(f"Master header length: {len(master_header)} characters")
print(f"Dropdown CSS length: {len(dropdown_css)} characters")

# Files to fix
files_to_fix = [
    'services/reddit-seo-geo.html',
    'services/brand-monitoring-social-listening.html'
]

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update relative paths for files in subdirectories
    if file_path.startswith('services/'):
        fixed_header = master_header.replace('href="', 'href="../')
        fixed_header = fixed_header.replace('href="../http', 'href="http')  # Fix external links
        fixed_header = fixed_header.replace('src="images/', 'src="../images/')
        fixed_header = fixed_header.replace('href="../index.html"', 'href="../index.html"')
    else:
        fixed_header = master_header
    
    # Add Code of Conduct link after Services dropdown
    # The pattern should already be in the master header, but let's verify
    if 'code-of-conduct.html' not in fixed_header:
        print(f"WARNING: Code of Conduct not found in header for {file_path}")
    
    # Replace existing header
    content = re.sub(
        r'<!-- Header/Navigation -->.*?</header>',
        fixed_header,
        content,
        flags=re.DOTALL
    )
    
    # Ensure dropdown CSS exists and is correct
    if '<!-- Dropdown Navigation Styles -->' not in content:
        # Insert dropdown CSS before </head>
        content = content.replace('</head>', f'{dropdown_css}\n</head>')
    else:
        # Replace existing dropdown CSS
        content = re.sub(
            r'<!-- Dropdown Navigation Styles -->.*?</style>',
            dropdown_css,
            content,
            flags=re.DOTALL
        )
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Fixed: {file_path}")

print("\nDone! All headers synchronized with index.html")
