import os, re

files = ['index.html', 'index_ru.html', 'index_en.html']

for fn in files:
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            html = f.read()

        # Find the language block
        match = re.search(r'(<div class="language_links premium-lang-header.*?</div>)', html, re.DOTALL)
        if match:
            lang_block = match.group(1)
            # Remove from everywhere
            html = html.replace(lang_block, '')
            
            # Find the closing tag of navbarNavAltMarkup (or navbarNavAltMarkupMobile)
            # We will insert the lang_block right before </nav> for both desktop and mobile
            html = html.replace('</nav>', f'  {lang_block}\n          </nav>')
            
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(html)

css_path = 'css/premium_theme.css'
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    css += '''
/* FIX HEADER DISPLAY AND LANG SWITCHER */
.navbar {
    display: flex;
    flex-wrap: nowrap !important;
    align-items: center;
}
.header {
    position: relative; /* ensure it stays sticky fixed */
    z-index: 100000;
}
.premium-sticky-menu {
    position: fixed !important;
    top: 0; left: 0; right: 0;
    margin: 0 auto;
    width: 100% !important;
    max-width: 100% !important;
    padding-left: 5%;
    padding-right: 5%;
    z-index: 999999 !important;
}
/* Ensure brand and language toggles are always arranged correctly */
.navbar-brand {
    margin-right: auto !important;
}
.premium-lang-header {
    margin-left: 20px !important;
}
'''
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

print('Updated header layout & css.')
