a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
c=int(input("Enter number3: "))
if (a>b and a>c) :
    print("{} is the greatest".format(a))
elif (b>a and b>c) :
    print("{} is the greatest".format(b))
else :
    print("{} is the greatest".format(c))
