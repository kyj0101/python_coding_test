w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)

mb = w * h * b / 8 / 1024 / 1024

print("%0.2f" %mb, end=" MB")