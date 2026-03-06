#!/bin/bash
# test-all-urls.sh - Test all major URLs on recho.co

echo "=========================================="
echo "Testing recho.co URL Availability"
echo "=========================================="

echo -e "\n📄 Testing Main Pages..."
curl -s -o /dev/null -w "Homepage: %{http_code}\n" https://recho.co/
curl -s -o /dev/null -w "Blog Index: %{http_code}\n" https://recho.co/blog
curl -s -o /dev/null -w "Services: %{http_code}\n" https://recho.co/services
curl -s -o /dev/null -w "Contact: %{http_code}\n" https://recho.co/contact
curl -s -o /dev/null -w "Technology: %{http_code}\n" https://recho.co/technology
curl -s -o /dev/null -w "FAQ: %{http_code}\n" https://recho.co/faq

echo -e "\n✨ Testing NEW Blog Posts (March 2026)..."
curl -s -o /dev/null -w "Time Spent Post: %{http_code}\n" \
  https://recho.co/blog/reddit-time-spent-nearly-doubles-since-2018
curl -s -o /dev/null -w "Gender Shift Post: %{http_code}\n" \
  https://recho.co/blog/reddit-gender-shift-nearly-half-women-users

echo -e "\n📰 Testing Recent Blog Posts..."
curl -s -o /dev/null -w "Q4 Earnings: %{http_code}\n" \
  https://recho.co/blog/reddit-q4-2025-earnings-report-analysis
curl -s -o /dev/null -w "Karma Building: %{http_code}\n" \
  https://recho.co/blog/how-to-build-reddit-karma-cultural-fit-vs-product-fit
curl -s -o /dev/null -w "Brands Rush to Reddit: %{http_code}\n" \
  https://recho.co/blog/brands-rush-to-reddit-boosting-ad-spend-gaming-ai-search
curl -s -o /dev/null -w "Reddit Overtakes TikTok: %{http_code}\n" \
  https://recho.co/blog/reddit-overtakes-tiktok-uk-international-growth-2026

echo -e "\n🔧 Testing Service Pages..."
curl -s -o /dev/null -w "Reddit SEO & GEO: %{http_code}\n" \
  https://recho.co/services/reddit-seo-geo
curl -s -o /dev/null -w "Brand Monitoring: %{http_code}\n" \
  https://recho.co/services/brand-monitoring-social-listening

echo -e "\n🗺️ Testing Sitemap & Robots..."
curl -s -o /dev/null -w "Sitemap: %{http_code}\n" https://recho.co/sitemap.xml
curl -s -o /dev/null -w "Robots.txt: %{http_code}\n" https://recho.co/robots.txt

echo -e "\n🤖 Testing LLM Crawler Access..."
curl -s -A "GPTBot/1.0" -o /dev/null -w "GPTBot (ChatGPT): %{http_code}\n" https://recho.co/
curl -s -A "ClaudeBot/1.0" -o /dev/null -w "ClaudeBot (Claude): %{http_code}\n" https://recho.co/
curl -s -A "PerplexityBot/1.0" -o /dev/null -w "PerplexityBot: %{http_code}\n" https://recho.co/
curl -s -A "Googlebot/2.1" -o /dev/null -w "Googlebot (Gemini): %{http_code}\n" https://recho.co/

echo -e "\n=========================================="
echo "✅ All tests complete!"
echo "Expected: All URLs should return 200 OK"
echo "=========================================="
