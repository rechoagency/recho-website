#!/bin/bash

echo "Testing RECHO.co URLs..."
echo "========================"

# Array of all blog post URLs
URLS=(
  "https://recho.co/"
  "https://recho.co/blog"
  "https://recho.co/sitemap.xml"
  "https://recho.co/robots.txt"
  "https://recho.co/blog/how-to-remove-negative-reddit-posts-from-google-search"
  "https://recho.co/blog/reddit-time-spent-nearly-doubles-since-2018"
  "https://recho.co/blog/reddit-gender-shift-nearly-half-women-users"
  "https://recho.co/blog/reddit-q4-2025-earnings-report-analysis"
  "https://recho.co/blog/how-to-build-reddit-karma-cultural-fit-vs-product-fit"
  "https://recho.co/blog/brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search"
  "https://recho.co/blog/reddit-overtakes-tiktok-uk-international-growth-2026"
  "https://recho.co/blog/how-much-do-reddit-ads-cost-in-2026"
  "https://recho.co/blog/reddit-max-campaigns-what-advertisers-need-to-know"
  "https://recho.co/blog/how-to-measure-reddit-impact-google-ai-overviews"
  "https://recho.co/blog/reddit-leads-ad-spend-growth-at-46-percent-2025"
  "https://recho.co/blog/why-brand-reddit-posts-rank-in-google-and-chatgpt"
  "https://recho.co/blog/is-reddit-marketing-worth-it-in-2026"
  "https://recho.co/blog/how-to-grow-a-subreddit-from-zero-to-10000-members"
  "https://recho.co/blog/how-reddit-pro-social-listening-tools-are-changing-marketing"
  "https://recho.co/blog/which-brands-are-winning-with-reddit-ads"
  "https://recho.co/blog/how-to-work-with-reddit-moderators"
  "https://recho.co/blog/how-to-build-an-engaged-reddit-community"
  "https://recho.co/blog/why-your-reddit-strategy-is-failing"
  "https://recho.co/blog/what-is-a-good-reddit-cpc-in-2025"
  "https://recho.co/blog/what-new-reddit-ad-tools-launched-in-2025"
)

PASSED=0
FAILED=0

for URL in "${URLS[@]}"; do
  HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
  
  if [ "$HTTP_CODE" = "200" ]; then
    echo "✅ $HTTP_CODE - $URL"
    ((PASSED++))
  else
    echo "❌ $HTTP_CODE - $URL"
    ((FAILED++))
  fi
done

echo ""
echo "========================"
echo "Total: $((PASSED + FAILED)) URLs"
echo "Passed: $PASSED"
echo "Failed: $FAILED"

if [ $FAILED -eq 0 ]; then
  echo "🎉 All URLs are working correctly!"
  exit 0
else
  echo "⚠️  Some URLs failed. Please investigate."
  exit 1
fi
