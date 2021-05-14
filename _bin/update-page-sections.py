with open('_includes/layout/menu', 'r') as f:
    lines = f.readlines()

section = []
for line in lines:
    line = line.strip()
    if line.startswith("{% include menu/section "):
        q1 = line.find('"') + 1
        q2 = line.rfind('"')
        section.append(line[q1:q2])
    elif line.startswith("{% include menu/section-end "):
        section.pop()
    elif line.startswith("{% include menu/item "):
        q1 = line.find('link="') + 6
        q2 = line.find('"', q1)
        link = "_pages/" + line[q1:q2] + ".md"
        if len(section) > 0:
            s = 'section: ' + ':'.join(section)
            print(f'sed -i -e "/^section: /d" {link}')
            print(f'sed -i -e "s/^categor/{s}\\ncategor/" {link}')
