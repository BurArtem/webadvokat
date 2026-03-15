import os, re

files = ['index.html', 'index_ru.html', 'index_en.html']

for file_name in files:
    if not os.path.exists(file_name): continue
    
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace `<p>/</p>` with `<span>/</span>` globally inside language_links
    content = content.replace('<p>/</p>', '<span>/</span>')
    content = content.replace('class="language_links d-none d-md-block"', 'class="language_links premium-lang-header d-none d-md-flex ml-lg-4 ml-md-2"')

    # The block we want to move starts with <!-- Языковые версии сайта --> and ends with </div>
    # It currently lives after </nav> \n </div>
    
    match = re.search(r'(<!-- Языковые версии сайта -->\s*<div class="language_links premium-lang-header d-none d-md-flex ml-lg-4 ml-md-2">.*?</div>)', content, re.DOTALL)
    if match:
        lang_block = match.group(1)
        # Remove it from its original place
        content = content.replace(lang_block, '')
        
        # Insert it inside the justify-content-end navbarNavAltMarkup
        # The structure we match:
        # id="navbarNavAltMarkup">\s*<div class="navbar-nav">.*?</div>
        def replacer(m):
            return m.group(0) + '\n            ' + lang_block.replace('\n', '\n            ')

        nav_pattern = re.compile(r'id="navbarNavAltMarkup">\s*<div class="navbar-nav">.*?</div>', re.DOTALL)
        content = nav_pattern.sub(replacer, content)
        
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fix applied successfully to HTML files.")
