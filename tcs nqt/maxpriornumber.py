list_nums=list(map(int,input().split()))
max_num=list_nums[0]
count=1
for i in range(1,len(list_nums)):
    if list_nums[i]>max_num:
        max_num=list_nums[i]
        count+=1
print(count)