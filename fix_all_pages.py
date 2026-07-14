import os
import glob
import re

# Get all HTML files
html_files = glob.glob('**/*.html', recursive=True)

# Exclude backup files
html_files = [f for f in html_files if 'backup' not in f.lower()]

print(f"Found {len(html_files)} HTML files to process\n")

google_fonts_link = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'

fixed_files = []

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        # 1. Ensure Google Fonts Poppins is loaded (add after Font Awesome)
        if 'Poppins' not in content and 'fontawesome' in content.lower():
            # Add Google Fonts after Font Awesome
            content = re.sub(
                r'(<!-- Font Awesome -->.*?</link>)',
                r'\1\n    \n    <!-- Google Fonts -->\n    ' + google_fonts_link,
                content,
                flags=re.DOTALL
            )
            modified = True
            print(f"  + Added Google Fonts to: {file_path}")
        
        # 2. Fix body tag - ensure it has font-poppins class
        if '<body' in content:
            # Check current body tag
            body_match = re.search(r'<body[^>]*>', content)
            if body_match:
                current_body_tag = body_match.group(0)
                
                # If it doesn't have font-poppins
                if 'font-poppins' not in current_body_tag:
                    # Add font-poppins to class attribute
                    if 'class="' in current_body_tag:
                        new_body_tag = current_body_tag.replace('class="', 'class="font-poppins ')
                    else:
                        new_body_tag = current_body_tag.replace('<body', '<body class="font-poppins"')
                    
                    content = content.replace(current_body_tag, new_body_tag)
                    modified = True
                    print(f"  + Added font-poppins class to body: {file_path}")
        
        # 3. Write back if modified
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_files.append(file_path)
    
    except Exception as e:
        print(f"  ERROR processing {file_path}: {e}")

print(f"\n✓ Fixed {len(fixed_files)} files")
if fixed_files:
    print("\nModified files:")
    for f in fixed_files:
        print(f"  - {f}")
