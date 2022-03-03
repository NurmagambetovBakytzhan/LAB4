from distutils.filelist import findall
import re
arr = []
txt = input()
arr = re.findall("[A-Z][a-z]+",txt)
print(arr)