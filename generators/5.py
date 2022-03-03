def to_zero(n):
    for i in range(n,-1,-1):
        yield i
print(*to_zero(int(input())))