a,m,d,n = input().split()
a = int(a)
d= int(d)
m = int(m)
n = int(n)
result = a

for i in range(n - 1):
    result = (result *  m) + d

print(result)
