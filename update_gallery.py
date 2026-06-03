import os
import random
import re

assets_dir = '/Users/user/Downloads/SNS-Groups/gallery/Assets'
images = [f for f in os.listdir(assets_dir) if f.endswith('.jpg') and '6g' not in f] # keep 6g for hero

html_blocks = []
categories = ['campus', 'events', 'labs', 'sports']

# Define a couple of templates for different aspect ratios to keep the masonry look
templates = [
    '<div class="gallery-item aspect-square shadow-sm" data-category="{cat}"><img src="Assets/{img}" alt="Gallery Image"><div class="gallery-overlay"><h3 class="text-white font-bold text-xl">SNS Institutions</h3><p class="text-gray-300 text-sm">Vibrant Campus Life.</p></div></div>',
    '<div class="gallery-item aspect-square shadow-sm" data-category="{cat}"><img src="Assets/{img}" alt="Gallery Image"><div class="gallery-overlay"><h3 class="text-white font-bold text-xl">SNS Institutions</h3><p class="text-gray-300 text-sm">State-of-the-art facilities.</p></div></div>',
    '<div class="gallery-item aspect-square shadow-sm" data-category="{cat}"><img src="Assets/{img}" alt="Gallery Image"><div class="gallery-overlay"><h3 class="text-white font-bold text-xl">SNS Institutions</h3><p class="text-gray-300 text-sm">Empowering the future.</p></div></div>'
]

# Randomize sort
random.seed(42)
for img in images:
    cat = random.choice(categories)
    # Give some col-span-2 to a few random images for masonry effect (1 in 5 chance)
    tpl = templates[2] if random.random() < 0.2 else templates[0]
    # urlencode space in img path
    img_encoded = img.replace(' ', '%20')
    html_blocks.append(tpl.format(cat=cat, img=img_encoded))

grid_content = '\n        '.join(html_blocks)

with open('/Users/user/Downloads/SNS-Groups/gallery/index.html', 'r') as f:
    content = f.read()

# Replace between <div class="grid ... scroll-animate delay-100"> and </div>\n      <!-- Load More -->
pattern = re.compile(r'(<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 scroll-animate delay-100">)(.*?)(      </div>\s*<!-- Load More -->)', re.DOTALL)

new_content = pattern.sub(r'\1\n        ' + grid_content + r'\n\3', content)

with open('/Users/user/Downloads/SNS-Groups/gallery/index.html', 'w') as f:
    f.write(new_content)

print("Gallery Updated with", len(images), "images")
