#!/usr/bin/env python3
"""Ensure every full HTML page carries the site's tracking tags.

This is the ONE mechanism that puts Google Tag Manager on the site (it
replaced the Pages Function middleware that blew the Cloudflare free-plan
100k/day Function-invocation limit). It is idempotent: running it twice in a
row must change nothing on the second run — .github/workflows/tracking-guard.yml
relies on that to auto-fix new pages on push without commit loops.

Per full HTML document (fragments without <head>/<body> are skipped):
  1. Insert the GTM container snippet in <head> if missing. When a page has
     the hardcoded GA4 gtag.js block, GTM goes right AFTER it so the GTM
     container's "Hardcoded GA4 Tag Present" blocking variable always sees
     gtag already defined (no async race). Otherwise GTM goes right after the
     viewport meta (or the <head> open tag as a last resort).
  2. Insert the GTM <noscript> iframe right after the <body> open tag if missing.
  3. Normalize the attribution script tag: strip every utm-tracking.js
     reference (any path, any version) and ensure exactly one
     <script src="/js/utm-tracking.js?v=3" defer></script> in <head>.
     Bump UTM_SRC's ?v= whenever js/utm-tracking.js changes (/js/* is cached
     immutable for a year).

Usage:
  python3 scripts/ensure_tracking.py           # fix files in place
  python3 scripts/ensure_tracking.py --check   # exit 1 if any file would change
"""

import argparse
import re
import sys
from pathlib import Path

GTM_ID = "GTM-5B67MTB8"
UTM_SRC = "/js/utm-tracking.js?v=3"

REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".wrangler", "node_modules", "__pycache__"}

GTM_HEAD_BLOCK = (
    "    <!-- Google Tag Manager -->\n"
    "    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':\n"
    "    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],\n"
    "    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=\n"
    "    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);\n"
    "    })(window,document,'script','dataLayer','" + GTM_ID + "');</script>\n"
    "    <!-- End Google Tag Manager -->"
)

UTM_TAG = '<script src="' + UTM_SRC + '" defer></script>'

GTM_NOSCRIPT_BLOCK = (
    "    <!-- Google Tag Manager (noscript) -->\n"
    '    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=' + GTM_ID + '"\n'
    '    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\n'
    "    <!-- End Google Tag Manager (noscript) -->"
)

# The hardcoded GA4 block: async gtag.js loader + the inline config script
# immediately after it. Non-greedy .*? stops at the inline script's close.
GTAG_BLOCK_RE = re.compile(
    r'<script[^>]*src="https://www\.googletagmanager\.com/gtag/js[^"]*"[^>]*>\s*</script>'
    r"\s*<script>.*?</script>",
    re.DOTALL,
)
VIEWPORT_RE = re.compile(r'<meta\s+name="viewport"[^>]*>')
HEAD_OPEN_RE = re.compile(r"<head(?:\s[^>]*)?>")
BODY_OPEN_RE = re.compile(r"<body(?:\s[^>]*)?>")
UTM_SCRIPT_RE = re.compile(
    r'[ \t]*<script[^>]*src="[^"]*utm-tracking\.js[^"]*"[^>]*>\s*</script>[ \t]*\n?'
)


def is_full_document(text):
    return bool(
        HEAD_OPEN_RE.search(text)
        and "</head>" in text
        and BODY_OPEN_RE.search(text)
        and "</body>" in text
    )


def insert_after(text, match, block):
    end = match.end()
    return text[:end] + "\n" + block + text[end:]


def head_insertion_match(text):
    """Where the GTM block goes: after gtag block > after viewport > after <head>."""
    return (
        GTAG_BLOCK_RE.search(text)
        or VIEWPORT_RE.search(text)
        or HEAD_OPEN_RE.search(text)
    )


def process(text):
    # 3a. Strip every existing utm-tracking.js tag (old paths like
    # "js/utm-tracking.js" or "../js/utm-tracking.js", stale ?v= values).
    text = UTM_SCRIPT_RE.sub("", text)

    # 1. GTM head snippet (+ the attribution script directly under it).
    if GTM_ID not in text:
        m = head_insertion_match(text)
        if m:
            text = insert_after(text, m, GTM_HEAD_BLOCK + "\n    " + UTM_TAG)

    # 3b. Pages that already had GTM still need the attribution tag restored.
    if UTM_SRC not in text:
        marker = "<!-- End Google Tag Manager -->"
        idx = text.find(marker)
        if idx != -1:
            end = idx + len(marker)
            text = text[:end] + "\n    " + UTM_TAG + text[end:]
        else:
            m = head_insertion_match(text)
            if m:
                text = insert_after(text, m, "    " + UTM_TAG)

    # 2. GTM noscript right after the <body> open tag.
    if "googletagmanager.com/ns.html?id=" not in text:
        m = BODY_OPEN_RE.search(text)
        if m:
            text = insert_after(text, m, GTM_NOSCRIPT_BLOCK)

    return text


def html_files():
    for path in sorted(REPO_ROOT.rglob("*.html")):
        if SKIP_DIRS.intersection(path.relative_to(REPO_ROOT).parts):
            continue
        yield path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report files that would change and exit 1; modify nothing",
    )
    args = parser.parse_args()

    modified, unchanged, skipped = [], 0, 0
    for path in html_files():
        original = path.read_text(encoding="utf-8")
        if not is_full_document(original):
            skipped += 1
            continue
        result = process(original)
        if result == original:
            unchanged += 1
            continue
        modified.append(path.relative_to(REPO_ROOT))
        if not args.check:
            path.write_text(result, encoding="utf-8")

    verb = "would change" if args.check else "modified"
    print(
        f"{verb}: {len(modified)}, unchanged: {unchanged}, skipped fragments: {skipped}"
    )
    for p in modified:
        print(f"  {p}")
    if args.check and modified:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
