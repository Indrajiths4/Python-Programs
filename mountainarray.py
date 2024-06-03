import math
n=int(input())
mountain=[int(input()) for _ in range(n)]
mid1,mid2=0,0
num=1 if n%2==0 else 0
count=0
if num==1:
    mid1,mid2=int((n/2)-1),int(n/2)
    for i in range(mid1-1,-1,-1):
        if i==mid1-1:
            if mountain[i]!=mountain[mid1]-1:
                mountain[i]=mountain[mid1]-1
                count+=1
            if mountain[n-i-1]!=mountain[mid1]-1:
                mountain[n-i-1]=mountain[mid1]-1
                count+=1
        else:
            if mountain[i]!=mountain[i+1]-1:
                mountain[i]=mountain[i+1]-1
                count+=1
            if mountain[n-i-1]!=mountain[i+1]-1:
                mountain[n-i-1]=mountain[i+1]-1
                count+=1
            
    print(count)
    
elif num==0:
    mid1=math.floor(n/2)

