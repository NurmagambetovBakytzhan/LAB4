import re
txt = input()
x = re.search("(a(b.{2}|b.{3})*)+",txt)
if x:
    print("Yes")
else:
    print("NO")