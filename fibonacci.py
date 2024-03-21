limit=int(input("Enter number : "))
a=0
b=1
c=0
for _ in range(limit):
    print(a)
    c=a+b
    a=b
    b=c