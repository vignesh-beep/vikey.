v=int(input())
p=list(map(int,input().split()[:v]))
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i]>p[j]:
            p[i],p[j]=p[j],p[i]
for a in range(len(p)):
    print(p[a],end=" ")
