#!/bin/bash

# Schema Validation Script for RECHO.co
# Validates all structured data markup across the site

BASE_URL="https://recho.co"
TOTAL_SCHEMAS=0
ERRORS=0

echo "================================================"
echo "RECHO.co Schema Validation Report"
echo "Date: $(date)"
echo "================================================"
echo ""

# Function to validate and count schemas
validate_page() {
    local url=$1
    local page_name=$2
    
    echo "Checking: $page_name"
    echo "URL: $url"
    
    # Fetch page and count @type occurrences
    schema_count=$(curl -s "$url" | grep -c "@type" || echo "0")
    
    if [ "$schema_count" -eq 0 ]; then
        echo "  ❌ ERROR: No schemas found"
        ((ERRORS++))
    else
        echo "  ✅ Found $schema_count schema types"
        
        # Extract and display schema types
        schemas=$(curl -s "$url" | grep -o '"@type"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/"@type"[[:space:]]*:[[:space:]]*"\([^"]*\)"/\1/' | sort | uniq)
        
        if [ -n "$schemas" ]; then
            echo "  Schema types:"
            while IFS= read -r schema; do
                echo "    • $schema"
            done <<< "$schemas"
        fi
    fi
    
    TOTAL_SCHEMAS=$((TOTAL_SCHEMAS + schema_count))
    echo ""
}

# Main pages
echo "=== MAIN PAGES ==="
validate_page "$BASE_URL/" "Homepage"
validate_page "$BASE_URL/blog" "Blog Index"
validate_page "$BASE_URL/services" "Services Overview"
validate_page "$BASE_URL/services/reddit-seo-geo" "Reddit SEO & Geo Service"
validate_page "$BASE_URL/services/brand-monitoring-social-listening" "Brand Monitoring Service"
validate_page "$BASE_URL/technology" "Technology"
validate_page "$BASE_URL/faq" "FAQ"
validate_page "$BASE_URL/contact" "Contact"
validate_page "$BASE_URL/privacy-policy" "Privacy Policy"

echo ""
echo "=== BLOG POSTS (23 posts) ==="

# Array of all blog post URLs
blog_posts=(
    "blog/how-to-remove-negative-reddit-posts-from-google-search"
    "blog/reddit-launches-human-verification-to-combat-bot-crisis"
    "blog/reddit-time-spent-nearly-doubles-since-2018"
    "blog/reddit-gender-shift-nearly-half-women-users"
    "blog/how-to-build-reddit-karma-cultural-fit-vs-product-fit"
    "blog/reddit-q4-2025-earnings-report-analysis"
    "blog/how-to-build-an-engaged-reddit-community"
    "blog/why-your-reddit-strategy-is-failing"
    "blog/what-is-a-good-reddit-cpc-in-2025"
    "blog/what-new-reddit-ad-tools-launched-in-2025"
    "blog/how-to-work-with-reddit-moderators"
    "blog/which-brands-are-winning-with-reddit-ads"
    "blog/how-reddit-pro-social-listening-tools-are-changing-marketing"
    "blog/how-to-grow-a-subreddit-from-zero-to-10000-members"
    "blog/is-reddit-marketing-worth-it-in-2026"
    "blog/why-brand-reddit-posts-rank-in-google-and-chatgpt"
    "blog/reddit-leads-ad-spend-growth-at-46-percent-2025"
    "blog/reddit-max-campaigns-what-advertisers-need-to-know"
    "blog/how-to-measure-reddit-impact-google-ai-overviews"
    "blog/how-much-do-reddit-ads-cost-in-2026"
    "blog/reddit-overtakes-tiktok-uk-international-growth-2026"
    "blog/brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search"
)

# Validate each blog post
post_count=1
for post in "${blog_posts[@]}"; do
    title=$(echo "$post" | sed 's/blog\///' | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')
    validate_page "$BASE_URL/$post" "Post $post_count: $title"
    ((post_count++))
done

echo ""
echo "================================================"
echo "VALIDATION SUMMARY"
echo "================================================"
echo "Total pages checked: $((9 + ${#blog_posts[@]}))"
echo "Total schema types found: $TOTAL_SCHEMAS"
echo "Pages with errors: $ERRORS"
echo ""

# Expected schema counts
echo "Expected Schema Distribution:"
echo "  • Blog Index: ~4 (CollectionPage, ItemList, BreadcrumbList, Organization)"
echo "  • Privacy Policy: ~3 (WebPage, BreadcrumbList, Organization)"
echo "  • Each blog post: ~3-4 (Article, FAQPage, BreadcrumbList)"
echo "  • Other main pages: ~5-10 each"
echo ""

if [ "$TOTAL_SCHEMAS" -ge 80 ]; then
    echo "✅ PASS: Site has robust schema markup ($TOTAL_SCHEMAS types)"
else
    echo "⚠️  WARNING: Schema count lower than expected ($TOTAL_SCHEMAS < 80)"
fi

if [ "$ERRORS" -eq 0 ]; then
    echo "✅ All pages have schema markup"
else
    echo "❌ $ERRORS pages missing schema markup"
fi

echo ""
echo "================================================"
echo "NEXT STEPS"
echo "================================================"
echo "1. Submit sitemap to Google Search Console:"
echo "   https://search.google.com/search-console"
echo "   Sitemap URL: https://recho.co/sitemap.xml"
echo ""
echo "2. Request indexing for updated pages"
echo ""
echo "3. Use Google Rich Results Test to validate schemas:"
echo "   https://search.google.com/test/rich-results"
echo ""
echo "4. Check Schema.org Validator:"
echo "   https://validator.schema.org/"
echo ""
echo "5. Monitor GSC Schema reports after 7-14 days"
echo "   Expected: 80-100+ schema instances"
echo "================================================"
