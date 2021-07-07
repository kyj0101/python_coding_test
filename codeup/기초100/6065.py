a, b, c = input().split()
list = [int(a), int(b), int(c)]
result = [num for num in list if num % 2 == 0]

for i in range(len(result)):
    print(result[i])
