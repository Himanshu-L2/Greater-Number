a = int(input("Please enter your first number."))
b = int(input("Please enter your second number."))
c = int(input("Please enter your third number."))

if (a > b):
    if (a>c):
        print(a,'is the greatest number.')
    elif (c>a) :
        print(c, 'is the greatest number.')
elif (b>a):
    if (b>c):
        print(b,'is the gratest number.')
    elif (c>b):
        print(c,'is the greatest number.')
