num =int(input("Enter a number: "))
if num % 2 == 0:
    print("your number is even")
else:
    print("your number is odd")


myname = 'nika'
urname = input("Enter your name: ")
if myname == urname:
    print("hello")
else:
    print('bye')


num1 = int(input("Enter a number: "))
if num1>90:
    print('a')
elif num1<90 and num1>70:
    print('b')
elif num1<70 and num1>50:
    print('c')
else:
    print('d')

num2=1
while num2 != 100:
    if num2 % 2 == 0:
        print(num2, "is even")
    else:
        print(num2, "is odd")
    num2 +=1