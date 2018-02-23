a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))

d=[]
sum=0
for i in range(0,a):
    e=int(input("Enter the list element: "))
    d.append(e)
for j in range(0,b):
    sum=sum+d[j]
    
    
print(sum)
