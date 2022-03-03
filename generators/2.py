def first_n(n):
    for i in range(n):
        if i % 2== 0:
            yield i
print(*first_n(int(input())), sep = ', ')