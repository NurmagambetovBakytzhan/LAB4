from distutils.filelist import findall
import re
arr = []
txt = input()
arr = re.findall("[a-z]_[a-z]+",txt)
print(arr)