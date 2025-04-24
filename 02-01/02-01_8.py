def recursive_1(n):
    if n > 0:
        print(n)
        recursive_1(n - 1)
        print(n)

recursive_1(3)

print()

def recursive_2(n):
    if n > 0:
        recursive_2(n - 1)
        print(n)

recursive_2(3)