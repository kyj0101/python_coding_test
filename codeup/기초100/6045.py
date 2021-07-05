a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

sum = a + b + c
result = round(float(sum) / float(3), 2)

print(sum)
print("%0.2f" %result)