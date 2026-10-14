num=[5,-3,8,-1,0,7,-9,2]
positive=0
negative=0
for n in num:
    if n>0: 
        positive +=1
    elif n<0:
        negative +=1
print(positive,"positive")
print(negative,"negative")
