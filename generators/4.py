def squares(a,b):
    for i in range(a,b+1,1):
        yield(i**2)
print(*squares(int(input()), int(input()) ) )