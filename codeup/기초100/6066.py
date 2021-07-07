a, b, c = input().split()
list = [int(a), int(b), int(c)]

for i in range(len(list)):
    num = list[i]

    if num % 2 == 0:
        print("even")
    else:
        print("odd")