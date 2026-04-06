# LLM Visibility Diagnosis - RECHO.co
**Date**: April 6, 2026
**Issue**: Peec AI shows blank results despite crawlers being allowed for 1 month

---

## Current Status Summary

### ✅ What's Working
1. **Cloudflare Settings**: Perfect
   - "Block AI training bots" = Do not block ✅
   - "Manage robots.txt" = Disabled (using custom robots.txt) ✅
   - All AI crawlers set to "Allow" ✅

2. **Crawler Access**: Confirmed Working
   - GPTBot: HTTP 200, 1.83 MB transferred, 151 requests allowed ✅
   - ClaudeBot: HTTP 200, 36.41 kB transferred, 9 requests allowed ✅
   - PerplexityBot: HTTP 200, 104.29 kB transferred, 8 requests allowed ✅
   - ChatGPT-User: HTTP 200, 1.83 MB transferred, 151 requests allowed ✅
   - **0 unsuccessful requests** across all crawlers ✅

3. **Technical Setup**:
   - robots.txt: Allows all AI bots ✅
   - sitemap.xml: 31 URLs ✅
   - Schema markup: 611 instances ✅
   - x-robots-tag: index, follow ✅

---

## ❌ The Mystery: Why No LLM Visibility?

**Timeline**:
- Cloudflare "Block AI Bots" disabled: ~1 month ago (early March 2026)
- Expected visibility by now: 20-40% (based on 4-week timeline)
- Actual Peec AI visibility: 0% (blank results)

**Possible Causes**:

### 1. Domain Age & Authority Issues
**Hypothesis**: LLMs may prioritize established domains with:
- Higher domain authority (DA/DR scores)
- More external backlinks
- Longer content history
- Established brand recognition

**Investigation needed**:
- What is recho.co's domain authority?
- How many quality backlinks does the site have?
- When was the domain first registered?
- Does the brand have citations elsewhere on the web?

### 2. Content Recency Bias
**Current situation**:
- Most blog posts are from Oct 2025 - Mar 2026 (relatively new)
- LLMs may favor content with:
  - Longer publishing history (years, not months)
  - More external validation (citations, mentions, shares)
  - Higher engagement signals

**Evidence from Cloudflare data**:
- ChatGPT-User: 151 requests (highest)
- GPTBot: 25 requests
- ClaudeBot: 9 requests (lowest)

This suggests crawling frequency is moderate, not aggressive.

### 3. Competitive Landscape
**Challenge**: Reddit marketing niche may be saturated
- Competitors: Reddit Inc official docs, major SEO sites, established agencies
- Your content needs to demonstrate unique authority/expertise
- LLMs may favor sources with:
  - Academic citations
  - Industry recognition
  - Executive/expert authorship
  - Case studies with data

### 4. Peec AI Coverage Limitations
**Possibility**: Peec AI may not track all LLM citations equally
- Different monitoring platforms show different results
- Peec AI may have:
  - Limited query coverage for your niche
  - Slower update cycles
  - Geographic/language biases
  - Sample size limitations

**Test needed**: Check visibility on other platforms:
- llmrefs.com/ai-search-visibility
- Profound AI
- Otterly.AI
- Manual ChatGPT/Claude/Perplexity searches

### 5. Content Format Mismatch
**LLM Preference**: Certain content formats get cited more:
- How-to guides with step-by-step instructions ✅ (you have these)
- Data-driven research with statistics ✅ (you have these)
- **Primary sources** (original research, surveys, case studies) ⚠️
- **Expert quotes** (interviews, industry leaders) ⚠️
- **Unique data** (proprietary insights, tools) ⚠️

**Potential gap**: Your content is well-written but may lack:
- Original proprietary research
- Exclusive data not available elsewhere
- Direct interviews with Reddit executives
- Unique case studies with client results

### 6. E-E-A-T Signals for LLMs
**Google cares about E-E-A-T, LLMs care even more**:
- **Experience**: Do you demonstrate hands-on Reddit marketing experience?
- **Expertise**: Are you recognized as a Reddit marketing expert?
- **Authoritativeness**: Is RECHO cited by other authoritative sources?
- **Trustworthiness**: Are there trust signals (reviews, testimonials, certifications)?

**Current status**:
- About page shows expertise ✅
- Blog content demonstrates knowledge ✅
- External citations: Unknown ⚠️
- Industry recognition: Unknown ⚠️
- Awards/certifications: Unknown ⚠️

---

## Investigation Steps

### Step 1: Check Domain Authority
```bash
# Use Moz, Ahrefs, or SEMrush to check:
- Domain Authority (DA)
- Domain Rating (DR)
- Number of referring domains
- Quality of backlinks
```

**Target**: DA 30+ preferred for LLM citations

### Step 2: Test LLM Visibility Manually
Ask direct questions to LLMs:
1. ChatGPT: "What are the best Reddit marketing agencies?"
2. Claude: "How do I improve Reddit engagement for my brand?"
3. Perplexity: "Reddit advertising costs 2026"
4. Gemini: "How to measure Reddit marketing impact?"

**Look for**: Does RECHO appear in any responses?

### Step 3: Check Competitor Citations
Search for known competitors:
1. Peec AI search for: reddit marketing agencies
2. Check if competitors appear
3. Analyze what makes their content citable

### Step 4: Use Alternative Monitoring Tools
Test visibility on:
1. https://llmrefs.com/ai-search-visibility
2. Profound AI (if available)
3. Otterly.AI
4. Manual LLM searches

### Step 5: Review External Brand Mentions
Check if RECHO is mentioned elsewhere:
```bash
site:reddit.com "RECHO" OR "recho.co"
site:linkedin.com "RECHO" Reddit agency
site:twitter.com "RECHO" Reddit
```

**Why it matters**: External mentions help establish authority

---

## Recommended Actions

### Immediate (This Week):
1. ✅ Verify Cloudflare settings (DONE)
2. ⏱️ Test manual LLM searches for RECHO
3. ⏱️ Check domain authority metrics
4. ⏱️ Use llmrefs.com crawler checker
5. ⏱️ Test alternative monitoring platforms

### Short-term (Next 2-4 Weeks):
1. **Build external citations**:
   - Guest posts on major marketing sites (Search Engine Journal, Moz, etc.)
   - Contribute to Reddit marketing discussions
   - Get quoted in industry publications
   
2. **Create unique proprietary content**:
   - Original survey data (Reddit marketers survey)
   - Exclusive case studies with metrics
   - Tools/calculators (Reddit ad cost calculator)
   - Industry reports (State of Reddit Marketing 2026)

3. **Enhance E-E-A-T signals**:
   - Add author bios with credentials
   - Include client testimonials
   - Show certifications/awards
   - Link to speaking engagements
   - Add social proof

4. **Optimize for LLM citation patterns**:
   - Add more data/statistics
   - Include expert quotes
   - Create definitive guides
   - Add comparison tables
   - Improve content depth (currently 4-5K words, aim for 6-8K for pillar content)

### Long-term (Next 3-6 Months):
1. **Build brand authority**:
   - Podcast appearances
   - Conference speaking
   - Industry award applications
   - Partnership announcements
   - Press releases

2. **Create linkable assets**:
   - Annual Reddit marketing report
   - Free tools (Reddit karma calculator, ad spend estimator)
   - Infographics with data
   - Research studies

3. **Expand content depth**:
   - Video content (YouTube)
   - Webinars
   - Interactive content
   - More frequent publishing (2-3x per week)

---

## Expected Timeline After Improvements

**If domain authority is the issue**:
- Month 1-2: Build backlinks, get external mentions
- Month 3-4: LLMs start discovering citations
- Month 5-6: 20-40% visibility
- Month 7-12: 60-80% visibility

**If content uniqueness is the issue**:
- Week 1-2: Create proprietary data/research
- Week 3-4: LLMs index new content
- Month 2-3: Citations start appearing
- Month 4-6: 60-80% visibility

**If it's just a timing issue**:
- Current: 4 weeks since enabling crawlers
- Typical LLM indexing: 6-12 weeks for new domains
- Expected visibility: Week 8-12 (mid-May to early June)

---

## Comparison: Similar Sites

### Established Reddit marketing competitors:
- Reddit.com official docs: High DA, cited frequently
- Major SEO blogs (Ahrefs, SEMrush): High DA, cited frequently
- Forbes, Business Insider: Extremely high DA, cited frequently

### New agencies (similar to RECHO):
- Often take 6-12 months to appear in LLM results
- Need strong backlink profile
- Require external validation

**Your advantage**: 
- 23 high-quality blog posts ✅
- 611 schema markup instances ✅
- Perfect technical SEO ✅
- Crawlers actively accessing site ✅

**Your challenge**:
- Possibly low domain authority ⚠️
- Limited external citations ⚠️
- Relatively new content ⚠️
- Need more unique proprietary data ⚠️

---

## Next Steps

**Immediate**:
1. Run domain authority check (Moz/Ahrefs)
2. Test manual LLM searches
3. Check llmrefs.com visibility
4. Test alternative monitoring platforms

**After testing, we can**:
1. Identify the root cause
2. Create targeted action plan
3. Set realistic timeline expectations
4. Track progress week-by-week

---

## Conclusion

**Good news**: Technical setup is perfect ✅  
**Challenge**: Need to boost authority signals and/or wait longer for indexing ⚠️

**Most likely causes** (in order of probability):
1. Domain authority too low (need 30+ DA)
2. Timing (need 8-12 weeks total, currently at 4 weeks)
3. Content needs more unique proprietary data
4. Limited external brand mentions
5. Peec AI coverage limitations

**Recommended next action**: Check domain authority and test manual LLM searches to narrow down root cause.

---

**Last Updated**: April 6, 2026
**Status**: Diagnosis in progress, awaiting domain authority data
