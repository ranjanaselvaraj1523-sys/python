n=int(input("Enter a number:"))
Square=n*n
total=0
while Square>0:
    total+=Square%10
    Square//=10
if total==n:
    print(n,"is a neon number")
else:
    print(n,"is not a neon number")
