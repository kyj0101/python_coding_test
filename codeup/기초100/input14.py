time = input()
indexFront = time.index(":")
indexBack = time.index(":",indexFront + 2)

print(time[indexFront + 1:indexBack])