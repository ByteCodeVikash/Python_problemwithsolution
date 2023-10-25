#find the factorial

                    #using for loop

""" num=int(input("Enter a number here: "))
fact=1
if num<0:
    print("factorial of zero does not exist")
if num==0:
    print("factorial of zero is",1)
if num>0:
    for i in range(1,num+1):
        fact=fact*i
print("the factorial of the given number is: ",fact)  """ 


      #using recursion

def fact(a):
    if a==0:
        return 1
    else:
        return ((a)*fact(a-1))

num=int(input("Enter a number here: "))
result=fact(num)
print("the factoial of the given number is",result)          