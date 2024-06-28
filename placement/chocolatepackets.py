numchoc=list(map(int,input().split()))
stu=int(input())
numchoc=sorted(numchoc)
mindiff=9999999999
for i in range(len(numchoc) - stu+1):
    if numchoc[stu+i-1] - numchoc[i] < mindiff:
        mindiff=numchoc[stu+i-1] - numchoc[i]
print(mindiff)