import os
path ="."
filelist = []
d = 0
for root, dirs, files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] == ".py" or os.path.splitext(file)[1] == ".json":
            filelist.append(os.path.join(root,file))
for name in filelist:
    with open(name, "r", encoding = "utf-8") as f:
        d += len(f.read().split("\n"))
print(d)
