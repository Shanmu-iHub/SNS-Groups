import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
html_files = [f for f in html_files if not f.startswith('components/') and not f.startswith('.gemini/')]

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {file_path}: {e}")
        continue

    original_content = content

    # REPLACEMENT 1: Header
    # Match starting with the announcement banner (if exists) up to the closing </nav> for mainNav
    # Or just match mainNav
    
    # We'll use custom search because regex with DOTALL might be too greedy or fail on large text
    header_start_str1 = 'id="announcementBanner"'
    header_start_str2 = '<nav id="mainNav"'
    
    idx_start = content.find(header_start_str1)
    if idx_start != -1:
        # Start from the opening <div of the banner
        idx_start = content.rfind('<div', 0, idx_start)
    else:
        idx_start = content.find(header_start_str2)
        
    if idx_start != -1:
        idx_end = content.find('</nav>', idx_start)
        if idx_end != -1:
            idx_end += len('</nav>')
            
            # The replacement string
            replacement = '<div id="global-header"></div>'
            
            # Remove any comment prefixes immediately before the match (e.g., <!-- Navigation -->)
            # To be safe, just replace the block.
            content = content[:idx_start] + replacement + content[idx_end:]
            print(f"Updated Header in {file_path}")

    # REPLACEMENT 2: Footer
    idx_footer_start = content.find('<footer ')
    if idx_footer_start != -1:
        idx_footer_end = content.find('</footer>', idx_footer_start)
        if idx_footer_end != -1:
            idx_footer_end += len('</footer>')
            
            # Calculate depth to construct relative script path
            depth = file_path.count('/')
            prefix = '../' * depth if depth > 0 else './'
            script_tag = f'<script src="{prefix}components/loader.js"></script>'
            
            replacement = f'<div id="global-footer"></div>\n    {script_tag}'
            content = content[:idx_footer_start] + replacement + content[idx_footer_end:]
            print(f"Updated Footer in {file_path}")

    # Only write if changes made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
