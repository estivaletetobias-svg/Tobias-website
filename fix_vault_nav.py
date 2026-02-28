import re

with open("vault-acesso-exclusivo.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the navigation logo to link back to index.html and remove standard anchor behavior
logo_pattern = r'<a href="#home" class="flex items-center gap-3 group">'
html = html.replace(logo_pattern, '<a href="index.html" class="flex items-center gap-3 group">')

with open("vault-acesso-exclusivo.html", "w", encoding="utf-8") as f:
    f.write(html)
