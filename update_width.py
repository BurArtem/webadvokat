import os

files = ['index.html', 'index_ru.html', 'index_en.html', 'about.html', 'about_uk.html', 'about_en.html', 'services.html', 'services_uk.html', 'services_en.html', 'price.html', 'price_uk.html', 'price_en.html', 'experience.html', 'experience_uk.html', 'experience_en.html', 'privacy_policy.html', 'privacy_policy_uk.html', 'privacy_policy_en.html']

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace max-width: 800px with max-width: 1200px
        new_content = content.replace('style="max-width: 800px;"', 'style="max-width: 1200px;"')
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
