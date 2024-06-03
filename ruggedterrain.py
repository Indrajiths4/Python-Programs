import math
n=int(input())
segment=[int(input()) for _ in range(n)]
max_dig=0
for i in range(0,n-1):
    if segment[i]<=segment[i+1]:
        max_dig=max(max_dig,segment[i+1]-segment[i]+1)
        segment[i+1]=segment[i]-1
    
print(math.ceil(math.sqrt(max_dig)))

