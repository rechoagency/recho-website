#!/usr/bin/env python3
"""
Comprehensive Schema.org JSON-LD Generator for RECHO
Adds proper structured data to all pages for Google Rich Results and AI visibility
"""

import json
import re

# Base organization schema (reused across all pages)
BASE_ORG = {
    "@type": "Organization",
    "@id": "https://www.recho.co/#organization",
    "name": "RECHO",
    "legalName": "RECHO - Full Service Reddit Marketing Agency",
    "url": "https://www.recho.co",
    "logo": {
        "@type": "ImageObject",
        "@id": "https://www.recho.co/#logo",
        "url": "https://www.recho.co/images/recho-logo.png",
        "contentUrl": "https://www.recho.co/images/recho-logo.png",
        "caption": "RECHO Logo",
        "inLanguage": "en-US"
    },
    "sameAs": ["https://www.linkedin.com/company/rechoagency"]
}

# FAQ data extracted from faq.html
FAQ_DATA = [
    {
        "q": "Why should my brand be on Reddit?",
        "a": "Reddit is the #1 platform for product conversations, with 51% of all online purchasing discussions happening on Reddit. With 400M+ weekly active users and strong year-over-year growth, Reddit offers unparalleled access to engaged communities actively seeking recommendations and making purchase decisions."
    },
    {
        "q": "What makes Reddit different from other social platforms?",
        "a": "Unlike other social platforms, Reddit is organized around interests and topics (subreddits) rather than follower relationships. This creates highly engaged, niche communities where users actively seek information and recommendations. The platform rewards authenticity and value over promotional content."
    },
    {
        "q": "What types of Reddit ads are available?",
        "a": "Reddit offers multiple ad formats: Promoted Posts (native feed ads), Video Ads (autoplay engagement), Carousel Ads (multi-image swipeable), Dynamic Product Ads (catalog-driven personalization), Conversation Ads (interactive formats), and Lead Generation Ads (in-ad forms)."
    },
    {
        "q": "How does Reddit ad targeting work?",
        "a": "Reddit offers sophisticated targeting including Community Targeting (specific subreddits), Interest Targeting (behaviors), Lookalike Audiences, Retargeting, Category Targeting (15 major verticals), and Geographic & Demographic filters."
    },
    {
        "q": "What's the typical cost of Reddit advertising?",
        "a": "Reddit ads operate on a bid-based system with $5 minimum daily budget. CPC typically ranges from $0.50 to $3.00 depending on targeting and competition. With RECHO's optimization expertise, we reduce CPC while maximizing reach and ROI."
    },
    {
        "q": "Do Reddit ads actually work?",
        "a": "Yes! When done correctly, Reddit ads deliver strong ROI. Reddit users actively seek information and recommendations, making them more receptive to valuable ads. RECHO combines data-driven targeting with creative optimization for measurable results."
    },
    {
        "q": "How does Reddit impact SEO and Google search rankings?",
        "a": "Reddit experienced a 1,328% increase in SEO visibility on Google between July 2023 and April 2024. Google prominently features Reddit discussions in search results. Authentic brand participation on Reddit becomes discoverable in Google search, driving organic traffic."
    },
    {
        "q": "Why is Reddit important for AI and ChatGPT visibility?",
        "a": "Reddit is the #1 platform for authentic product discussions, with 51% of all online purchase conversations. This makes it crucial for AI and LLM training. Authentic Reddit engagement positions your brand as the recommended solution in AI responses."
    },
    {
        "q": "How does RECHO manage my brand's Reddit presence?",
        "a": "RECHO provides full-service management including organic community engagement, paid advertising campaigns, content strategy, and EchoMind technology platform. We handle everything from subreddit research to campaign optimization."
    },
    {
        "q": "What makes RECHO different from other agencies?",
        "a": "RECHO combines deep Reddit platform expertise with proprietary EchoMind technology. We offer integrated organic and paid strategies, authentic community engagement, and data-driven optimization that other agencies can't match."
    },
    {
        "q": "How long does it take to see results?",
        "a": "Paid advertising shows results within days. Organic community building shows meaningful engagement within 4-8 weeks. Brand recall and sentiment improvements manifest over 3-6 months. RECHO's integrated approach provides immediate paid results while building long-term organic growth."
    },
    {
        "q": "What industries does RECHO work with?",
        "a": "RECHO works with brands across all industries including technology, consumer products, finance, healthcare, gaming, and B2B services. We tailor strategies to each industry's unique Reddit communities and audience behaviors."
    }
]

def create_faq_schema():
    """Generate FAQPage schema"""
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            BASE_ORG,
            {
                "@type": "WebPage",
                "@id": "https://www.recho.co/faq.html#webpage",
                "url": "https://www.recho.co/faq.html",
                "name": "Frequently Asked Questions | RECHO",
                "description": "Everything you need to know about Reddit marketing and how RECHO can help your brand succeed",
                "isPartOf": {"@id": "https://www.recho.co/#website"},
                "about": {"@id": "https://www.recho.co/#organization"},
                "inLanguage": "en-US"
            },
            {
                "@type": "FAQPage",
                "@id": "https://www.recho.co/faq.html#faqpage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": faq["q"],
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": faq["a"]
                        }
                    }
                    for faq in FAQ_DATA
                ]
            },
            {
                "@type": "BreadcrumbList",
                "@id": "https://www.recho.co/faq.html#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.recho.co"},
                    {"@type": "ListItem", "position": 2, "name": "FAQ", "item": "https://www.recho.co/faq.html"}
                ]
            }
        ]
    }
    return json.dumps(schema, indent=2)

def inject_schema(filepath, schema_json):
    """Inject schema before </body> tag"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if schema already exists
    if 'application/ld+json' in content:
        print(f"⚠️  Schema already exists in {filepath}, skipping...")
        return False
    
    # Inject before </body>
    schema_block = f'\n    <!-- Comprehensive JSON-LD Schema Markup -->\n    <script type="application/ld+json">\n{schema_json}\n    </script>\n</body>'
    content = content.replace('</body>', schema_block)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Added schema to {filepath}")
    return True

# Generate and inject FAQ schema
print("📊 Generating FAQ Page Schema...")
faq_schema = create_faq_schema()
inject_schema('/home/user/webapp/faq.html', faq_schema)

print("\n✅ FAQ schema generation complete!")
print("🔍 Validate at: https://search.google.com/test/rich-results")
