n = input()
n = int(n, 16)
hex_n = int('A',16)

for i in range(1,10):
     print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

for _ in range(6):
    print('%X'%n, '*%X'%hex_n, '=%X'%(n*hex_n), sep='')
    hex_n += 1