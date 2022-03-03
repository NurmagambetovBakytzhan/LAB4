def first_n(n):
    for i in range(int(n**0.5) + 1):
        yield (i*i)
print(*first_n(125))
