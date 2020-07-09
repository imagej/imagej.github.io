import re
import os

in_root = "/home/random/Development/imagej/imagej/imagej-net-temp/"
out_file = "/home/random/Development/imagej/imagej/imagej.github.io/convert/status/template_count.csv"

res = {}
out = ""
for filename in os.listdir(in_root):
    if not filename.endswith(".mw"):
        continue
    with open(os.path.join(in_root, filename), 'r') as file:
        data = file.read()
        pattern = re.compile(r'\{\{[ ]*([^ |\}\{]*)')
        for (name) in re.findall(pattern, data):
            # name = name.replace("-", "")
            if len(name.strip()) == 0:
                continue
            if res.get(name):
                res[name] = int(res[name]) + 1
            else:
                res[name] = int(1)
res = {k: v for k, v in sorted(res.items(), key=lambda item: item[1], reverse=True)}
for name in res:
    out += name + "," + str(res[name]) + "\n"
with open(out_file, 'w') as file:
    file.write(out)

