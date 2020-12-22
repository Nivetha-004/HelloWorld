n=int(input())
f1=0
f2=1
i,s=0,0
if n==1 or n==0:
    print(f1)
elif n==2:
    print("{} {}".format(f1,f2))
else:
    print("{} {} ".format(f1,f2),end="")
    while(i!=n-2):
        s=f2+f1
        f1=f2
        f2=s
        print(s,end=" ")
        i=i+1
        
        
    
