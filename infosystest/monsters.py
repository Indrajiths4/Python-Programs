n=int(input("Enter number of monsters : "))
exp=int(input("Enter the experience points : "))
print(f"Enter the {n} power of monsters : ")
power=list(map(int,input().split()))
print(f"Enter the {n} bonus of monsters : ")
bonus=list(map(int,input().split()))
flag=1
vis=[0]*n
while flag==1:
    flag=0
    for i in range(n):
        if vis[i]==0:
            if exp>=power[i]:
                exp+=bonus[i]
                vis[i]=1
                flag=1
                break
            
print(sum(vis))