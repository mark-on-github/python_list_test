import os

a = open("output.txt", "w")
for path, subdirs, files in os.walk(r'D:\cb'):
    for filename in files:
        f = os.path.join(path, filename)
        a.write(str(f) + os.linesep)
