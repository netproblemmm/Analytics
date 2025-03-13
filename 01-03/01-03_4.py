n = int(input())
max = -1
min = 30001

for i in range(n):
    x = int(input())
    if x > max:
        max = x
    if x < min:
        min = x

print(max, min)