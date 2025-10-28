/**
 * Google Analytics 4 Event Tracking
 * Tracks user interactions across RECHO website
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // ===========================================
    // 1. EMAIL LINK TRACKING (sales@recho.co)
    // ===========================================
    const emailLinks = document.querySelectorAll('a[href^="mailto:sales@recho.co"]');
    emailLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'email_click', {
                    'event_category': 'Contact',
                    'event_label': 'sales@recho.co',
                    'email_address': 'sales@recho.co',
                    'location': window.location.pathname
                });
                console.log('GA4 Event: Email click tracked');
            }
        });
    });
    
    // ===========================================
    // 2. SOCIAL SHARE BUTTON TRACKING
    // ===========================================
    
    // LinkedIn Share
    const linkedinShareButtons = document.querySelectorAll('a[href*="linkedin.com/sharing"]');
    linkedinShareButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (typeof gtag !== 'undefined') {
                const articleTitle = document.querySelector('h1') ? document.querySelector('h1').textContent : 'Unknown';
                gtag('event', 'share', {
                    'method': 'LinkedIn',
                    'content_type': 'article',
                    'item_id': window.location.pathname,
                    'article_title': articleTitle
                });
                console.log('GA4 Event: LinkedIn share tracked');
            }
        });
    });
    
    // Twitter/X Share
    const twitterShareButtons = document.querySelectorAll('a[href*="twitter.com/intent/tweet"]');
    twitterShareButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (typeof gtag !== 'undefined') {
                const articleTitle = document.querySelector('h1') ? document.querySelector('h1').textContent : 'Unknown';
                gtag('event', 'share', {
                    'method': 'Twitter',
                    'content_type': 'article',
                    'item_id': window.location.pathname,
                    'article_title': articleTitle
                });
                console.log('GA4 Event: Twitter share tracked');
            }
        });
    });
    
    // Reddit Share
    const redditShareButtons = document.querySelectorAll('a[href*="reddit.com/submit"]');
    redditShareButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (typeof gtag !== 'undefined') {
                const articleTitle = document.querySelector('h1') ? document.querySelector('h1').textContent : 'Unknown';
                gtag('event', 'share', {
                    'method': 'Reddit',
                    'content_type': 'article',
                    'item_id': window.location.pathname,
                    'article_title': articleTitle
                });
                console.log('GA4 Event: Reddit share tracked');
            }
        });
    });
    
    // Email Share
    const emailShareButtons = document.querySelectorAll('a[href^="mailto:"][href*="subject="]');
    emailShareButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (typeof gtag !== 'undefined') {
                const articleTitle = document.querySelector('h1') ? document.querySelector('h1').textContent : 'Unknown';
                gtag('event', 'share', {
                    'method': 'Email',
                    'content_type': 'article',
                    'item_id': window.location.pathname,
                    'article_title': articleTitle
                });
                console.log('GA4 Event: Email share tracked');
            }
        });
    });
    
    // ===========================================
    // 3. BLOG SEARCH TRACKING
    // ===========================================
    const blogSearchInput = document.getElementById('blog-search');
    const searchButton = document.getElementById('search-btn');
    
    if (blogSearchInput && searchButton) {
        // Track search when button is clicked
        searchButton.addEventListener('click', function(e) {
            const searchTerm = blogSearchInput.value.trim();
            if (searchTerm && typeof gtag !== 'undefined') {
                gtag('event', 'search', {
                    'search_term': searchTerm,
                    'search_location': 'blog_page'
                });
                console.log('GA4 Event: Blog search tracked -', searchTerm);
            }
        });
        
        // Track search when Enter key is pressed
        blogSearchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                const searchTerm = blogSearchInput.value.trim();
                if (searchTerm && typeof gtag !== 'undefined') {
                    gtag('event', 'search', {
                        'search_term': searchTerm,
                        'search_location': 'blog_page'
                    });
                    console.log('GA4 Event: Blog search tracked -', searchTerm);
                }
            }
        });
    }
    
    // ===========================================
    // 4. "BOOK A CALL" BUTTON TRACKING
    // ===========================================
    const bookCallButtons = document.querySelectorAll('a[href*="contact.html"], a[href*="contact"]');
    bookCallButtons.forEach(function(button) {
        // Only track if it looks like a CTA button (contains "Book", "Call", "Contact", etc.)
        const buttonText = button.textContent.toLowerCase();
        if (buttonText.includes('book') || buttonText.includes('call') || buttonText.includes('contact') || buttonText.includes('schedule')) {
            button.addEventListener('click', function(e) {
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'cta_click', {
                        'event_category': 'Engagement',
                        'event_label': button.textContent.trim(),
                        'cta_location': window.location.pathname,
                        'cta_type': 'Book a Call'
                    });
                    console.log('GA4 Event: CTA button click tracked -', button.textContent.trim());
                }
            });
        }
    });
    
    // ===========================================
    // 5. BLOG CARD CLICK TRACKING
    // ===========================================
    const blogCards = document.querySelectorAll('a[href*="/blog/"]');
    blogCards.forEach(function(card) {
        card.addEventListener('click', function(e) {
            if (typeof gtag !== 'undefined') {
                const blogTitle = card.querySelector('h3') ? card.querySelector('h3').textContent : 'Unknown';
                const blogUrl = card.getAttribute('href');
                gtag('event', 'blog_click', {
                    'event_category': 'Content',
                    'event_label': blogTitle,
                    'blog_url': blogUrl,
                    'click_location': window.location.pathname
                });
                console.log('GA4 Event: Blog card click tracked -', blogTitle);
            }
        });
    });
    
    // ===========================================
    // 6. EXTERNAL LINK TRACKING (LinkedIn, etc.)
    // ===========================================
    const externalLinks = document.querySelectorAll('a[target="_blank"]:not([href*="recho.co"])');
    externalLinks.forEach(function(link) {
        // Exclude share buttons (already tracked above)
        if (!link.href.includes('twitter.com/intent') && 
            !link.href.includes('linkedin.com/sharing') && 
            !link.href.includes('reddit.com/submit')) {
            
            link.addEventListener('click', function(e) {
                if (typeof gtag !== 'undefined') {
                    const destination = link.hostname;
                    const linkText = link.textContent.trim() || link.getAttribute('aria-label') || 'External Link';
                    gtag('event', 'external_link_click', {
                        'event_category': 'Outbound',
                        'event_label': destination,
                        'link_text': linkText,
                        'link_url': link.href,
                        'from_page': window.location.pathname
                    });
                    console.log('GA4 Event: External link click tracked -', destination);
                }
            });
        }
    });
    
    console.log('GA4 Custom Event Tracking Initialized ✅');
});
