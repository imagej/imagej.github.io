import os

def processfile(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    file_changed = False
    while True:
        line_changed = False
        for old, new in redirects.items():
            if new.startswith('TODO') or new == '<UNCHANGED>' or new == '???': continue
            for i in range(len(lines)):
                l = lines[i]
                l = l.replace(f'src="{old}"', f'src="/{new}"') # HTML src, no slash
                l = l.replace(f'src="{old}#', f'src="/{new}#') # HTML src, no slash, with anchor
                l = l.replace(f'href="{old}"', f'href="/{new}"') # HTML href, no slash
                l = l.replace(f'href="{old}#', f'href="/{new}#') # HTML href, no slash, with anchor
                l = l.replace(f']({old})', f'](/{new})') # Markdown, no slash
                l = l.replace(f']({old}#', f'](/{new}#') # Markdown, no slash, with anchor
                l = l.replace(f'src="/{old}"', f'src="/{new}"') # HTML src, with slash
                l = l.replace(f'src="/{old}#', f'src="/{new}#') # HTML src, with slash, with anchor
                l = l.replace(f'href="/{old}"', f'href="/{new}"') # HTML href, with slash
                l = l.replace(f'href="/{old}#', f'href="/{new}#') # HTML href, with slash, with anchor
                l = l.replace(f'](/{old})', f'](/{new})') # Markdown, with slash
                l = l.replace(f'](/{old}#', f'](/{new}#') # Markdown, with slash, with anchor
                if lines[i] != l:
                    file_changed = line_changed = True
                    lines[i] = l
        if not line_changed: break
    if not file_changed: return
    # write out file with updated links
    with open(path, 'w') as f:
        for line in lines:
            f.write(line)

with open('redirects.txt', 'r') as f:
    lines = f.readlines()
redirects = {l.split(' :: ')[0]: l.split(' :: ')[1].rstrip() for l in lines}

for root, dirs, files in os.walk("_pages"):
    for name in files:
        processfile(os.path.join(root, name))

