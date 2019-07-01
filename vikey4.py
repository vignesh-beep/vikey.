pravy=int(input())
if (pravy<=1000):
   for i in range(2,pravy):
       if(pravy %i==0):
         print("no")
         break
   else:
       print("yes")
else:
    print("no")
