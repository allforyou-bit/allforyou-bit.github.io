"""
fix_global_issues.py
Changes applied to ALL HTML files:
1. Remove AdSense placeholder banners → <!-- AdSense banner placeholder -->
2. Newsletter text: "Join 1,000+" → "Join fellow Red Seal candidates"
3. Remove exit-intent popups (article/hub pages)
"""
import os, glob, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

QUIZ_PAGES = {'421a.html','310t.html','309a.html','310s.html','308a.html',
              '276a.html','447a.html','313a.html','442a.html'}

files = glob.glob(os.path.join(BASE, '*.html'))
total = changed = 0

for fpath in files:
    fname = os.path.basename(fpath)
    total += 1
    content = open(fpath, encoding='utf-8').read()
    original = content

    # ── 1. AdSense banner removal ──────────────────────────────────────

    # Pattern A: quiz top banner in its own <div class="container"> (Template A: 421a)
    content = re.sub(
        r'<!-- AD SLOT TOP -->\s*\n<div class="container">\s*\n\s*<div class="ad-banner">.*?</div>\s*\n</div>',
        '<!-- AdSense banner placeholder -->',
        content, flags=re.DOTALL
    )

    # Pattern B: quiz middle banner with comment (Template A: 421a)
    content = re.sub(
        r'\s*<!-- AD SLOT MIDDLE -->\s*\n\s*<div class="ad-banner">.*?</div>',
        '\n  <!-- AdSense banner placeholder -->',
        content, flags=re.DOTALL
    )

    # Pattern C: quiz top banner in its own container (Template B: 276a etc.)
    # <div class="container">\n  <div class="ad-banner">📢 Advertisement...</div>\n</div>
    content = re.sub(
        r'<div class="container">\s*\n\s*<div class="ad-banner">📢 Advertisement[^<]*(?:<[^>]+>[^<]*)*</div>\s*\n</div>\s*\n',
        '<!-- AdSense banner placeholder -->\n',
        content, flags=re.DOTALL
    )

    # Pattern D: inline quiz banner (Template B bottom / 442a top)
    content = re.sub(
        r'\s*<div class="ad-banner"[^>]*>📢 Advertisement[^<]*(?:<[^>]+>[^<]*)*</div>',
        '\n  <!-- AdSense banner placeholder -->',
        content, flags=re.DOTALL
    )

    # Pattern E: article / hub pages
    content = content.replace('<div class="ad-banner">Advertisement</div>', '<!-- AdSense banner placeholder -->')

    # ── 2. Newsletter text ─────────────────────────────────────────────

    content = content.replace(
        'Join 1,000+ Red Seal candidates. Get 10 new practice questions + exam strategies weekly \u2014 free.',
        'Join fellow Red Seal candidates. Get exam tips and new questions \u2014 free.'
    )
    # Variant with &mdash;
    content = content.replace(
        'Join 1,000+ Red Seal candidates. Get 10 new practice questions + exam strategies weekly &mdash; free.',
        'Join fellow Red Seal candidates. Get exam tips and new questions &mdash; free.'
    )
    # Variant with HTML dash
    content = content.replace(
        'Join 1,000+ Red Seal candidates. Get 10 new practice questions + exam strategies weekly &#8212; free.',
        'Join fellow Red Seal candidates. Get exam tips and new questions &#8212; free.'
    )

    # ── 3. Exit popup removal (article/hub pages only) ──────────────────
    # Quiz pages: exit popup is inside the study sheet template string (removed via #4)
    # Article/hub pages: real DOM popup
    if '<!-- EXIT INTENT POPUP -->' in content:
        start = content.find('<!-- EXIT INTENT POPUP -->')
        # Find the closing </script> of the exit listener (contains "exitShown")
        # The pattern ends with: })();\n</script>
        end_marker = '})();\n</script>'
        end_alt = '  })();\n</script>'
        end_pos = content.find(end_marker, start)
        end_pos_alt = content.find(end_alt, start)
        end_pos = max(end_pos, end_pos_alt)  # take whichever found
        if end_pos != -1:
            content = content[:start] + content[end_pos + len(end_marker):]

    # ── 4. Write if changed ────────────────────────────────────────────
    if content != original:
        open(fpath, 'w', encoding='utf-8').write(content)
        changed += 1
        print(f'  Updated: {fname}')

print(f'\nDone. {changed}/{total} files updated.')
