
month = int(input())

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]

if month in winter:
    print("winter")
elif month in spring:
    print("spring")
elif month in summer:
    print("summer")
else:
    print("fall")