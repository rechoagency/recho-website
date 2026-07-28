#!/usr/bin/env python3
"""
Move landing page links from Company section to Services section in footer
"""

files = ['services.html', 'blog.html', 'contact.html', 'faq.html', 'technology.html']

for file in files:
    print(f"Processing {file}...")
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove from Company section
    old_company = '''                        <li><a href="contact.html" class="hover:text-recho-orange transition-colors">Book a Call</a></li>
                        <li><a href="reddit-geo.html" class="hover:text-recho-orange transition-colors text-gray-400 text-sm">Reddit GEO</a></li>
                        <li><a href="reddit-marketing-agency.html" class="hover:text-recho-orange transition-colors text-gray-400 text-sm">Reddit Marketing Agency</a></li>
                        <li><a href="reddit-advertising-agency.html" class="hover:text-recho-orange transition-colors text-gray-400 text-sm">Reddit Advertising Agency</a></li>
                    </ul>'''
    
    new_company = '''                        <li><a href="contact.html" class="hover:text-recho-orange transition-colors">Book a Call</a></li>
                    </ul>'''
    
    content = content.replace(old_company, new_company)
    
    # Add to Services section
    old_services = '''                        <li><a href="services.html" class="hover:text-recho-orange transition-colors">Profile Optimization</a></li>
                    </ul>'''
    
    new_services = '''                        <li><a href="services.html" class="hover:text-recho-orange transition-colors">Profile Optimization</a></li>
                        <li><a href="reddit-geo.html" class="hover:text-recho-orange transition-colors">Reddit GEO</a></li>
                        <li><a href="reddit-marketing-agency.html" class="hover:text-recho-orange transition-colors">Reddit Marketing Agency</a></li>
                        <li><a href="reddit-advertising-agency.html" class="hover:text-recho-orange transition-colors">Reddit Advertising Agency</a></li>
                    </ul>'''
    
    content = content.replace(old_services, new_services)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Updated {file}")

print("\n✅ All files updated!")
