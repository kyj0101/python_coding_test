a,d,n = input().split()
a = int(a)
d= int(d)
n = int(n)

if d == 0:
    print(a)
else:
    list = list(range(a, n * d, d))
    print(list[len(list) - 1])