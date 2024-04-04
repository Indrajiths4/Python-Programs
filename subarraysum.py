list= [-2, -3, 4, -1, -2, 1, 5, -3]
sum,large=0,0
for i in range(len(list)):
    sum=list[i]
    for j in range(i+1,len(list)):
        if sum>large:
            large=sum
            minindex,maxindex=i,j
        sum+=list[j]
print(large)
print(list[minindex:maxindex])