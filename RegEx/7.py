import re
txt = re.sub("_"," ",input()).split()
for i in txt:
    print(i.capitalize(),end="")
print()