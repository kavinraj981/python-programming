a=int(input("Enter the 3 digit Number: "))
b=int(input("Enter the 3 digit Number: "))
for num in range(a,b+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp//=10
    if num==sum:
        print(num)
