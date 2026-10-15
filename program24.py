n=int(input("Enter a number"))
temp=n
sum=0
while n>0:
    digit=n%10
    fact=1
for i on range(1,digit+1):
    fact*=i
sum+=fact
n//=10
if sum==temp:
    print("Strong number")
else:
    print("Not a strong number")
