n=int(input("Enter number"))
temp=n
s=0
while n>0:
    d=n%10
    f=1
for i in range(1,d+1):
    f*=i
    s+=f
    n//=10
if s==temp:
    print("Peterson number")
else:
    print("Not a peterson number")
