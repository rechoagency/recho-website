import os
import glob

# Find all blog post HTML files
blog_files = glob.glob('blog/*.html')

for file_path in blog_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has Poppins
    if 'fonts.googleapis.com' in content and 'Poppins' in content:
        continue
    
    # Add after Font Awesome
    if '<!-- Font Awesome -->' in content and '<!-- Google Fonts -->' not in content:
        content = content.replace(
            '    <!-- Custom CSS -->',
            '    <!-- Google Fonts -->\n    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">\n    \n    <!-- Custom CSS -->'
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Added Google Fonts to: {file_path}")

print("\nDone!")
