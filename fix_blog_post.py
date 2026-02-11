#!/usr/bin/env python3
"""
Fix the brands-rush blog post by adding proper header and footer
"""

# Read the header template (everything up to <!-- Blog Content -->)
with open('/tmp/header_template.html', 'r') as f:
    header = f.read()

# Read the footer template
with open('/tmp/footer_template.html', 'r') as f:
    footer = f.read()

# Read the current brands-rush blog post content (skip the incomplete head/style section)
with open('/home/user/webapp/blog/brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search.html', 'r') as f:
    current_content = f.read()

# Find where the actual article content starts (after the schema markup)
article_start = current_content.find('<article class="max-w-4xl')
if article_start == -1:
    print("ERROR: Could not find article start")
    exit(1)

# Extract just the article content
article_content = current_content[article_start:]

# Find where the article ends (before any existing footer or closing tags)
article_end = article_content.find('</article>')
if article_end != -1:
    article_content = article_content[:article_end + len('</article>')]

# Now customize the header for this specific blog post
# Replace the breadcrumb
header = header.replace('<li class="text-gray-800">Reddit Ad Costs</li>', 
                       '<li class="text-gray-800">AI Search & Ad Spend</li>')

# Replace the article header section
header = header.replace('''            <!-- Article Header -->
            <header class="mb-12">
                <div class="flex items-center gap-3 mb-6">
                    <span class="px-4 py-1 bg-purple-100 text-purple-700 text-sm rounded-full font-semibold">Advertising Tips</span>
                    <time datetime="2026-01-15" class="text-gray-600 text-sm">January 15, 2026</time>
                    <span class="text-gray-600 text-sm">• 10 min read</span>
                </div>
                <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6 leading-tight">
                    How Much Do Reddit Ads Cost in 2026? (Complete Pricing Guide)
                </h1>
                <p class="text-xl text-gray-600 leading-relaxed">
                    Reddit ads cost $0.50-$4.00 per click and $3.50-$15 CPM with a $5 minimum daily budget. Here's everything advertisers need to know about Reddit advertising costs, platform comparisons, and maximizing ROI in 2026.
                </p>
            </header>

            <!-- Direct Answer Box -->
            <div class="bg-gradient-to-r from-orange-50 to-red-50 border-l-4 border-recho-orange p-6 mb-8 rounded-r-lg">
                <h2 class="text-lg font-bold text-gray-900 mb-3">💰 Quick Answer</h2>
                <p class="text-gray-800 leading-relaxed">
                    <strong>Reddit ads in 2026 cost $0.50-$4.00 per click (CPC) and $3.50-$15.00 per 1,000 impressions (CPM)</strong>, with a $5 minimum daily budget. Average ROAS ranges from 2.3x to 4.7x across most verticals, with consumer tech achieving ~$7 ROAS according to Reddit's official data. Most successful campaigns run $50-$100 daily budgets for sufficient data. Reddit is 42% cheaper per click than Facebook and offers 69% more clicks at lower CPMs than Meta ads.
                </p>
            </div>

            <!-- Pricing Reality Check Callout -->
            <div class="bg-blue-50 border-l-4 border-recho-blue p-6 my-8 rounded-r-lg">
                <h3 class="font-bold text-gray-900 mb-3 text-lg flex items-center gap-2">
                    <i class="fas fa-chart-line text-recho-blue"></i>
                    Why Reddit Ad Costs Matter Now
                </h3>
                <p class="text-gray-800 leading-relaxed mb-3">
                    Reddit's ad revenue is projected to hit <strong>$2.5 billion in 2026</strong> (39% growth from 2025). With 443.8 million weekly active users and 46.3% YoY ad spend growth—crushing Instagram (22%), TikTok (9%), and Facebook (7.6%)—understanding Reddit's pricing gives you a competitive edge.
                </p>
                <p class="text-gray-800 leading-relaxed">
                    <strong>The catch?</strong> Most advertisers underestimate the $50/day minimum needed for Reddit's algorithm to optimize effectively. Anything less wastes budget on insufficient data.
                </p>
            </div>

            <!-- Table of Contents -->
            <div class="table-of-contents p-6 rounded-lg mb-12">
                <h2 class="text-xl font-bold text-gray-900 mb-4 flex items-center gap-2">
                    <i class="fas fa-list"></i>
                    Table of Contents
                </h2>
                <ol class="space-y-2">
                    <li><a href="#reddit-ad-pricing-models" class="hover:text-recho-orange transition-colors">1. Reddit Ad Pricing Models: CPC vs CPM Explained</a></li>
                    <li><a href="#cost-breakdown-by-format" class="hover:text-recho-orange transition-colors">2. Cost Breakdown by Ad Format and Objective</a></li>
                    <li><a href="#platform-comparison" class="hover:text-recho-orange transition-colors">3. Reddit vs Meta vs LinkedIn vs TikTok: Price Comparison</a></li>
                    <li><a href="#budget-recommendations" class="hover:text-recho-orange transition-colors">4. Minimum Budget Requirements and Recommendations</a></li>
                    <li><a href="#industry-benchmarks" class="hover:text-recho-orange transition-colors">5. Industry Benchmarks: CTR, CPC, and CPM by Vertical</a></li>
                    <li><a href="#maximizing-roi" class="hover:text-recho-orange transition-colors">6. How to Maximize ROI and Lower Your Costs</a></li>
                </ol>
            </div>

            <!-- Main Content -->
            <div class="blog-content prose prose-lg max-w-none">''',
                                
'''            <!-- Article Header -->
            <header class="mb-12">
                <div class="flex items-center gap-3 mb-6">
                    <span class="px-4 py-1 bg-purple-100 text-purple-700 text-sm rounded-full font-semibold">Advertising Tips</span>
                    <time datetime="2026-02-08" class="text-gray-600 text-sm">February 8, 2026</time>
                    <span class="text-gray-600 text-sm">• 11 min read</span>
                </div>
                <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6 leading-tight">
                    Brands Rush to Reddit, Boosting Ad Spend and Gaming AI Search
                </h1>
                <p class="text-xl text-gray-600 leading-relaxed">
                    A leaked presentation deck reveals major brands are dramatically increasing Reddit ad budgets—not just for traditional reach, but to dominate AI-powered search results in ChatGPT, Google Gemini, and Perplexity.
                </p>
            </header>

            <!-- Main Content -->
            <div class="blog-content prose prose-lg max-w-none">''')

# Combine everything
final_content = header + '\n' + article_content + '\n' + footer

# Write the fixed file
with open('/home/user/webapp/blog/brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search.html', 'w') as f:
    f.write(final_content)

print("✅ Blog post fixed successfully!")
print(f"Final file size: {len(final_content)} characters")
