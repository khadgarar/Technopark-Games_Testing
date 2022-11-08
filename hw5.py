import os
import glob
import re
from progress.bar import IncrementalBar
from tqdm import tqdm

#1
log_path=input("Please eneter the path to the logs you want to be parsed\n")
isDir = os.path.isdir(log_path)
full_text = []
if isDir:
    print("Inputted path is a directory")
    for filename in glob.glob(os.path.join(log_path, '*.log')):
        with open(filename, 'r') as f:
            text = f.readlines()
            full_text.extend(text)
            print("File", filename, "read completely")
else:
    print("Inputted path is a file")
    with open(log_path, 'r') as f:
        full_text = f.readlines()
    print("File read completely")

print("Proceding to search all read lines ising regex")
#2
result = []

for line in tqdm(range(len(full_text))):
    if re.search(".*Error.*", full_text[line]) != None:
        result.append(full_text[line])
#3
print("Search completed, outputting to file")
with open("res.log", 'w') as f:
    print(*result, file = f, end = "")

print(len(result))
