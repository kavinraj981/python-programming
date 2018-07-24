a=int(input("Enter the 3 digit Number: "))
sum=0
while a>0:
   digit=a%10
   sum=sum+digit
if sum==a:
     print("YES")
