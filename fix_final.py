import os, re

files = ['index.html', 'index_ru.html', 'index_en.html']

for fn in files:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            html = f.read()

        # We need to extract the language block to reinsert it properly.
        match = re.search(r'(\s*<div class="language_links premium-lang-header.*?</div>)', html, re.DOTALL)
        if match:
            lang_block = match.group(1).strip()
            # Remove all instances
            html = html.replace(match.group(1), '')
            
            # Insert the lang block directly into the navbar-nav menu as the last item
            # Or insert it directly after the navbar-nav block inside the collapse block.
            html = re.sub(r'(<div class="navbar-nav">.*?</div>)', r'\1\n            ' + lang_block, html, flags=re.DOTALL)

        with open(fn, 'w', encoding='utf-8') as f:
            f.write(html)

css_path = 'css/premium_theme.css'
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    css += '''
/* Force strict alignment of the language block */
.language_links.premium-lang-header {
    margin-left: auto !important;
    display: flex !important;
    align-items: center;
    position: static !important;
    transform: none !important;
    padding-left: 20px;
}
.navbar-collapse {
    justify-content: flex-end !important;
    display: flex;
}
.navbar-nav {
    margin-left: auto;
}
'''
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

print('Final fixes applied cleanly.')
