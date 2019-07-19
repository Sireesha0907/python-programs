q=int(input("Enter First Interval: "))
w=int(input("Enter Second Interval: "))
print("Numbers Are",q, "and", w )
for i in range(q,w+1):
    if i%2 !=0:
        print(i,end=' ')
print("these are the odd numbers between two interval")
