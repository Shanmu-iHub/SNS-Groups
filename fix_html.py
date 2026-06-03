with open('/Users/user/Downloads/SNS-Groups/mandatory-disclosure/index.html', 'r') as f:
    content = f.read()

content = content.replace(
    "</tbody></table>\n        \n        <div class=\"scroll-animate visible mt-12\">",
    "</tbody></table></div>\n        \n        <div class=\"scroll-animate visible mt-12\">"
)

with open('/Users/user/Downloads/SNS-Groups/mandatory-disclosure/index.html', 'w') as f:
    f.write(content)

print("Fix applied")
