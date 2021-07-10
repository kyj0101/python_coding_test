a,d,n = input().split()
a = int(a)
d= int(d)
n = int(n)
result = a

for i in range(n - 1):
    result *= d

print(result)