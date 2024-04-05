def checkherovsvillian(hero,villian,heroes,villians):
    h,v=heroes,villians
    i,j=0,0
    h1,v1=hero[::],villian[::]
    while j!=v and i!=h:
        if h1[i] > v1[j]:
            h1[i]=h1[i]-v1[j]
            j+=1
        elif h1[i] < v1[j]:
            i+=1
        else:
            i+=1
            j+=1
    return True if j==v else False
    
villians=int(input())
heroes=int(input())
herohealth=int(input())
hero=[herohealth]*heroes
villian=[]
count=0
for i in range(villians):
    villian.append(int(input()))
win=0
while win==0:
    if checkherovsvillian(hero,villian,heroes,villians) == True:
        win=1
    else:
        villian.pop(0)
        count+=1
        villians-=1
print(count)