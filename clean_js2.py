import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the NEWS DASHBOARD FUNCTIONALITY block
pattern = r'// --- NEWS DASHBOARD FUNCTIONALITY START ---.*?// --- NEWS DASHBOARD FUNCTIONALITY END ---'
content = re.sub(pattern, '', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
