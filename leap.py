u=int(input("Enter Year: "))
if((u%400)==0 and (u%4)==0):
    print("The Year is Leap Year")
elif((u%100)==0 and (u%400)==1):
    print("The Year is Not a Leap Year")
else:
    print("The Year is Not a Leap Year")
