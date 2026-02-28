import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Regex to safely remove the literal "\n   <div ... </div>" duplicate lines
# We look for </p>\n followed by spaces and a div tag
pattern = r'</p>\\n\s*<div class="mt-8 flex items-center font-mono.*?</div>'

html_fixed = re.sub(pattern, '</p>', html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_fixed)

