list1=[9,2,-3,1,-76]
list2=list(map(int,input().split()))
for i in [list1,list2]:
    print()
    for j in i:
        if j>=0:
           print('{} '.format(j),end="")
