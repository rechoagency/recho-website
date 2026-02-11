#!/bin/bash
# Fix Services dropdown on all blog post pages

cd /home/user/webapp/blog

for file in *.html; do
    echo "Processing $file..."
    
    # Replace the simple Services link with dropdown structure
    sed -i '/<nav class="hidden md:flex items-center space-x-8">/,/<\/nav>/{
        s|<a href="../services.html" class="text-gray-700 hover:text-recho-orange transition-colors duration-300">Services</a>|<div class="nav-item relative">\n                        <a href="../services.html" class="nav-link text-gray-700 hover:text-recho-orange transition-colors duration-300 flex items-center">\n                            Services\n                            <i class="fas fa-chevron-down ml-1 text-xs"></i>\n                        </a>\n                        <div class="dropdown">\n                            <a href="../services.html" class="border-b border-gray-100">\n                                <i class="fas fa-th-large mr-2 text-recho-orange"></i>\n                                All Services\n                            </a>\n                            <a href="../services/reddit-seo-geo.html">\n                                <i class="fas fa-search mr-2 text-recho-orange"></i>\n                                Reddit SEO \& GEO\n                            </a>\n                            <a href="../services/brand-monitoring-social-listening.html">\n                                <i class="fas fa-chart-line mr-2 text-recho-orange"></i>\n                                Brand Monitoring \& Social Listening\n                            </a>\n                        </div>\n                    </div>|
    }' "$file"
    
done

echo "✅ All blog post files updated with Services dropdown"
