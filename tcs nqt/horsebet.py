n,k=map(int,input().split())
horses_price=list(map(int,input().split()))
current_sum=0
start=0
max_length=0
for end in range(n):
    current_sum+=horses_price[end]
    while current_sum>=k and start<=end:
        current_sum-=horses_price[start]
        start+=1
    max_length=max(max_length,end-start+1)
print(max_length)