
'''
with open("sample.txt", "r") as f:
  #f.write("This is the sample file created just for file handling.")

  print(f.read())'''

# to delete the file we will import os
import os
os.remove("demofile.txt")
