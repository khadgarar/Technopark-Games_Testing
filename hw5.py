import os,glob


#log_path = 'C:\logs'  'C:\logs\log.log'
log_path=input()
isDir = os.path.isdir(log_path)
if isDir:
    print("is a dir")
    for filename in glob.glob(os.path.join(log_path, '*.log')):
      with open(filename, 'r') as f:
        text = f.read()
        print (filename)
        print (len(text))
else:
    print("is a file")
    with open(log_path, 'r') as f:
        text = f.read()
        print (log_path)
        print (len(text))
        
