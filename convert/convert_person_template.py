import re

file = "/home/random/Development/imagej/imagej/imagej-net-temp/Template:Person.mw"
wiki_user_regex = r'\|\ ([^\=]*)\ \=\ \[\[User:\{\{\{1\}\}\}\|([^\]]*)\]\]'
github_user_regex = r'\|\ ([^\=]*)\ \=\ \[https:\/\/github.com\/\{\{\{1\}\}\} ([^\[\]]*)\]'
with open(file, 'r') as file:
    data=file.readlines()
    res = ""
    for line in data:
        match_wiki = re.match(wiki_user_regex, line)
        match_github = re.match(github_user_regex, line)
        if match_wiki:
            line = re.sub(wiki_user_regex, r'{% if name == "\1" %}{% assign name = "\2" %}{% assign link = "User:\1" %}{% endif %}', line)
            res += line
        if match_github:
            line = re.sub(github_user_regex, r'{% if name == "\1" %}{% assign name = "\2" %}{% assign link = "https://github.com/\1" %}{% endif %}', line)
            res += line
    print(res)
