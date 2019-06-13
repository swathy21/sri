s=int(input())
b=list(map(int,input().split()))
sum=0
average=0
for x in b:
    sum=sum+x
average=sum//len(b)
print(average)
    
