i=1
while i<=3:
    a=int(input("enter an even no"))
    if a%2==0:
        break
    i+=1
if i==4:
    print("this is wrong")
else:
    print("this is correct")
