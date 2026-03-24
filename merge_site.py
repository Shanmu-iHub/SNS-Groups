import re
import os

def merge():
    cwd = r"c:\Users\HP\Desktop\SNS Groups"
    desktop_path = os.path.join(cwd, "Desktop.html")
    mobile_path = os.path.join(cwd, "mobile.html")
    index_path = os.path.join(cwd, "index.html")

    with open(desktop_path, "r", encoding="utf-8") as f:
        desktop_content = f.read()
    
    with open(mobile_path, "r", encoding="utf-8") as f:
        mobile_content = f.read()

    # Extract Body content
    desktop_body = re.search(r"<body[^>]*>(.*?)</body>", desktop_content, re.DOTALL).group(1)
    mobile_body = re.search(r"<body[^>]*>(.*?)</body>", mobile_content, re.DOTALL).group(1)

    with open(index_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Replace Placeholders
    final_content = template.replace("[DESKTOP_CODE]", desktop_body)
    final_content = final_content.replace("[MOBILE_CODE]", mobile_body)

    # Clean up duplicate meta/style tags if any in the bodies (usually bodies shouldn't have them but just in case)
    # The user manual merge might have some.
    
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(final_content)

if __name__ == "__main__":
    merge()
