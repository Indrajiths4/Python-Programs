n,k=map(int,input().split())
numofcoins=list(map(int,input().split()))
current_sum=0
start=0
for end in range(n):
    current_sum+=numofcoins[end]
    while current_sum>k and start<=end:
        current_sum-=numofcoins[start]
        start+=1
    if current_sum==k:
        break
print(start+1,"",end+1)