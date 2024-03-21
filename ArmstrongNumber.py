num=int(input("Enter number : "))
num1=num
count=len(str(num))
sum=0
while num1!=0:
    rem=int(num1%10)
    sum=sum+rem**count
    num1=num1//10
if sum==num:
    print("Armstrong")
else:
    print("Not")