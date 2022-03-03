txt = input()
txt = ''.join(word.title() for word in txt.split('_'))
print(txt)