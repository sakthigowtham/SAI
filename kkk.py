a=int(input())
sum=0
t=a
while(t>0):
       q=t%10
       sum=sum+(q**3)
       t=t//10
if(a==sum):
       print("yes")
else:
       print("no")
