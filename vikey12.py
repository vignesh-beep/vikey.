v,p=map(int,input().split())
for i in range(v+1,p,1):
      if(i>1):
        for x in range(2,i):
          if(i%x==0):
             break
        else:
           print(i,end=" ")
