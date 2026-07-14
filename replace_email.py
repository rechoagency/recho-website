import os
import glob

# Find all HTML files
html_files = glob.glob('**/*.html', recursive=True)

count = 0
files_modified = []

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file contains delivery@recho.co
        if 'delivery@recho.co' in content:
            # Replace all occurrences
            new_content = content.replace('delivery@recho.co', 'sales@recho.co')
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            # Count occurrences in this file
            file_count = content.count('delivery@recho.co')
            count += file_count
            files_modified.append(f"{file_path}: {file_count} replacements")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"Total replacements: {count}")
print(f"Files modified: {len(files_modified)}")
print("\nDetailed changes:")
for change in files_modified:
    print(f"  {change}")
