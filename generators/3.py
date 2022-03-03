def div(n):
    for i in range(n):
        if i % 3==0 or i %4 ==0:
            yield i
print(*div(int(input())))

