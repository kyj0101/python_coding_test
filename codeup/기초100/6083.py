r,g,b = input().split()
r = int(r)
g = int(g)
b = int(b)

for i in range(0, r):
    for j in range(0, g):
        for x in range(0, b):
            print(i, j, x)

print(r * g * b)