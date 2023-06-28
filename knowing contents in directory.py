#python script for knowing the contents in a file or directory 

import os
dir = "C:\devops project"  # In dir variable we have to assign directory inside the double quotes
for name in os.listdir(dir):
  fullname = os.path.join(dir, name)
  if os.path.isdir(fullname):
    print("{} is a directory".format(fullname))
  else:
    print("{} is a file".format(fullname))
