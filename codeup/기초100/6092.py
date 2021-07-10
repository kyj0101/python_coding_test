n = int(input())
a = input().split()
a = [int(a[i]) for i in range(len(a))]
result = []

for i in range(1, 24):
    count = 0

    for j in range(0, len(a)):
        if a[j] == i:
            count += 1
    
    print(count, end=" ")
    count = 0
