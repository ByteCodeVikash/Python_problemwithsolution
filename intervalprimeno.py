#print the prime no in an interval

lower=int(input("Enter a lower no here: "))
upper=int(input("Enter a upper no here: "))

for num in range(lower,upper+1):
    if num>1:
        for i in  range(2,num):
            if num % i==0:
                break
        else:
             print(num)