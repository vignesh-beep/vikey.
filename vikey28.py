v1,m1= map(int, input().split())
h2,m2= map(int, input().split())
if(v1>h2):
    z=v1-h2
    y=m1-m2
    print(z,y)
else:
    t=h2-v1
    s=m2-m1
    print(t,s)
