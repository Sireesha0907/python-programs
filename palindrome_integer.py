p=int(input("Enter the Number"))
tempo=p
rev=0
if(p<=1000):
    while(p>0):
        num=p%10
        rev=rev*10+num
        p=p//10
    if(tempo==rev):
        print("The Number is a palindrome")
    else:
        print("The Number is not a palindrome")
else:
    print("Invalid")
