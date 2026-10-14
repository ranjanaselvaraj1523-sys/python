n=int(input("Enter a number:"))
temp=n
total=0
while temp>0:
    digit=temp%10
    total+=digit**len(str(n))
    temp//=10
if total==n:
    print("Amstrong number")
else:
    print("Not an Amstrong number")
