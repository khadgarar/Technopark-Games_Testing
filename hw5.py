import os
import glob
import re

#log_path = 'C:\logs' 'C:\logs\log.log' 'C:\logs\shorts' 'C:\logs\shorts\short1.log'
log_path=input("Please eneter the path to the logs you want to be parsed\n")
isDir = os.path.isdir(log_path)
full_text = []
if isDir:
    print("is a dir")
    for filename in glob.glob(os.path.join(log_path, '*.log')):
        with open(filename, 'r') as f:
            text = f.readlines()
            full_text.extend(text)
else:
    print("is a file")
    with open(log_path, 'r') as f:
        full_text = f.readlines()

print (*full_text, sep = "\n")
print(len(full_text))

result = []
for line in full_text:
    if re.search(".*Error.*", line) != None:
        result.append(line)

print("\n\n\nAns:\n",*result, sep = "\n")
