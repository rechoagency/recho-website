#!/usr/bin/env python3
"""
Update landing pages with fixes:
1. Remove eyebrow bubble above H1
2. Add more body text under H1
3. Replace with global header/footer
4. Move landing page links to Services section in footer
"""

import re

# Pages to update
pages = [
    'reddit-geo.html',
    'reddit-marketing-agency.html', 
    'reddit-advertising-agency.html'
]

print("Updating landing pages...")

for page in pages:
    print(f"\n📄 Processing {page}...")
    
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove eyebrow bubble (the inline-block bg-recho-cream element)
    # Match the eyebrow with the text inside it
    eyebrow_pattern = r'<div class="inline-block bg-recho-cream text-recho-orange text-xs font-semibold px-4 py-2 rounded-full mb-6 tracking-wider">\s*REDDIT-ONLY · ORGANIC \+ PAID · FULLY COMPLIANT\s*</div>\s*'
    content = re.sub(eyebrow_pattern, '', content)
    print("  ✅ Removed eyebrow bubble")
    
    # 2. Add more body text under H1 for each page
    if 'reddit-geo' in page:
        old_text = '''When buyers ask AI, the answer is written on Reddit. Our <strong>generative engine optimization</strong> and <strong>AI visibility</strong> services build the authentic Reddit presence that gets your brand cited by ChatGPT and Google AI Overviews — then we track your citations with EchoMind.'''
        
        new_text = '''When buyers ask AI, the answer is written on Reddit. Our <strong>generative engine optimization</strong> and <strong>AI visibility</strong> services build the authentic Reddit presence that gets your brand cited by ChatGPT and Google AI Overviews — then we track your citations with EchoMind.</p>
                    
                    <p class="text-lg text-gray-700 leading-relaxed mb-6">
                        Reddit stopped being optional the day AI started reading it. Nearly 500 million people use Reddit every week, and the models answering your buyers' questions lean on those threads more than almost any other source. Show up authentically in the conversations that matter, and those citations become part of your competitive advantage.'''
        
        content = content.replace(old_text, new_text)
        print("  ✅ Added more body text (Reddit GEO)")
    
    elif 'marketing-agency' in page:
        old_text = '''We believe brands belong on Reddit — when they show up as contributors, not billboards. That belief is our whole company: real Reddit natives, organic and paid, fully compliant. Nothing faked, nothing bought, nothing you'd wince to see screenshotted.'''
        
        new_text = '''We believe brands belong on Reddit — when they show up as contributors, not billboards. That belief is our whole company: real Reddit natives, organic and paid, fully compliant. Nothing faked, nothing bought, nothing you'd wince to see screenshotted.</p>
                    
                    <p class="text-lg text-gray-700 leading-relaxed mb-6">
                        Most marketing leaders we meet have the same story: somebody handed Reddit to an intern or a generalist agency — and Reddit did what Reddit does. A promotional post. A pile-on. A screenshot that travels. If that made you wary, your instinct is correct. Reddit punishes marketing that doesn't respect it. But when brands show up the right way — authentic, compliant, value-first — that's when Reddit becomes one of the most powerful channels you'll ever use.'''
        
        content = content.replace(old_text, new_text)
        print("  ✅ Added more body text (Marketing Agency)")
    
    elif 'advertising-agency' in page:
        old_text = '''We believe brands belong on Reddit — when they show up as contributors, not billboards. That belief is our whole company: real Reddit natives, organic and paid, fully compliant. Nothing faked, nothing bought, nothing you'd wince to see screenshotted.'''
        
        new_text = '''We believe brands belong on Reddit — when they show up as contributors, not billboards. That belief is our whole company: real Reddit natives, organic and paid, fully compliant. Nothing faked, nothing bought, nothing you'd wince to see screenshotted.</p>
                    
                    <p class="text-lg text-gray-700 leading-relaxed mb-6">
                        Reddit advertising is not "Facebook with upvotes." The creative that works here looks nothing like your other channels. Your targeting needs to respect community culture. And the ads that perform best are the ones that never look like ads at all. That's where we come in: full-funnel Reddit Ads management that drives results without making your brand a screenshot.'''
        
        content = content.replace(old_text, new_text)
        print("  ✅ Added more body text (Advertising Agency)")
    
    # Save updated content
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)

print("\n✅ All landing pages updated!")
print("\nNote: Global header/footer replacement will be done with separate Edit operations")
