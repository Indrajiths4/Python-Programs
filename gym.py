energy=int(input())
found,count=0,0
num_exercises = int(input())
list,vis=[],[]
for i in range(num_exercises):
    list.append(int(input()))
    vis.append(0)
list.sort()
while i>=0:
    if list[i]<=energy and vis[i]<2:
        vis[i]=vis[i]+1
        energy=energy-list[i]
    if vis[i]==2 or list[i]>energy:
        i=i-1
    if energy==0:
        found=1
        break
print("Output : ",sum(vis)) if found==1 else print("Output : ",-1)