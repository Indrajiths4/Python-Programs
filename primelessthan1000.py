def prime(num):
    prime=1
    for i in range(2,num//2+1):
        if num%i==0:
            prime=0
            break
    return prime


for i in range(2,1000+1):
    result=prime(i)
    if result == 1:
        print(i)  