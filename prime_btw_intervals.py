q=int(input("Enter First Interval: "))
w=int(input("Enter Second Interval: "))
for var in range(q,w+1):
    if var>1:
        for i in range(2,var):
            if((var%i)==0):
                break
        else:
            print(var)
print("These are The Prime Numbers ")

