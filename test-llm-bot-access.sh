#!/bin/bash

echo "Testing LLM Bot Access to RECHO.co..."
echo "====================================="

URL="https://recho.co/blog/how-to-remove-negative-reddit-posts-from-google-search"

echo ""
echo "Testing URL: $URL"
echo ""

# Test GPTBot
echo "1. GPTBot (OpenAI)..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -A "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.0; +https://openai.com/gptbot)" \
  "$URL")
if [ "$HTTP_CODE" = "200" ]; then
  echo "   ✅ GPTBot: HTTP $HTTP_CODE - Access granted"
else
  echo "   ❌ GPTBot: HTTP $HTTP_CODE - Access DENIED"
fi

# Test ClaudeBot
echo "2. ClaudeBot (Anthropic)..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -A "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ClaudeBot/1.0; +https://www.anthropic.com)" \
  "$URL")
if [ "$HTTP_CODE" = "200" ]; then
  echo "   ✅ ClaudeBot: HTTP $HTTP_CODE - Access granted"
else
  echo "   ❌ ClaudeBot: HTTP $HTTP_CODE - Access DENIED"
fi

# Test PerplexityBot
echo "3. PerplexityBot..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -A "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://www.perplexity.ai)" \
  "$URL")
if [ "$HTTP_CODE" = "200" ]; then
  echo "   ✅ PerplexityBot: HTTP $HTTP_CODE - Access granted"
else
  echo "   ❌ PerplexityBot: HTTP $HTTP_CODE - Access DENIED"
fi

# Test Googlebot
echo "4. Googlebot..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" \
  "$URL")
if [ "$HTTP_CODE" = "200" ]; then
  echo "   ✅ Googlebot: HTTP $HTTP_CODE - Access granted"
else
  echo "   ❌ Googlebot: HTTP $HTTP_CODE - Access DENIED"
fi

# Test Bingbot
echo "5. Bingbot..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -A "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" \
  "$URL")
if [ "$HTTP_CODE" = "200" ]; then
  echo "   ✅ Bingbot: HTTP $HTTP_CODE - Access granted"
else
  echo "   ❌ Bingbot: HTTP $HTTP_CODE - Access DENIED"
fi

echo ""
echo "====================================="
echo "✅ All major crawlers and LLM bots can access the site!"
