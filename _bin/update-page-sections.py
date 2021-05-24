import os, sys

with open('_includes/layout/menu', 'r') as f:
    lines = f.readlines()

section = []
for line in lines:
    line = line.strip()
    if line.startswith("{% include menu/section "):
        q1 = line.find('"') + 1
        q2 = line.find('"', q1 + 1)
        section.append(line[q1:q2])
    elif line.startswith("{% include menu/section-end "):
        section.pop()
    elif line.startswith("<li>"):
        q1 = line.find('href="') + 6
        q2 = line.find('"', q1)
        link = f'_pages{line[q1:q2]}.md'
        if not os.path.exists(link):
            link = f'_pages{line[q1:q2]}/index.md'
        if not os.path.exists(link):
            sys.stderr.write(f'[WARNING] No such link: {line[q1:q2]}\n')
            continue
        if len(section) > 0:
            s = 'section: ' + ':'.join(section)
            print(f'grep -q \'^section: \' {link} &&')
            print(f'  sed -i -e "s;^section: .*;{s};" {link} ||')
            print(f'  sed -i -e "s;^\(title: .*\);\\1\\n{s};" {link}')
