def main():
    a=input("Enter The Number ")
    try:
        num=int(a)
        if(num>0):
            print("The Number is Positive Number")
        elif(num<0):
            print("The Number is Negative Number")
        elif(num==0):
            print("The Number is Zeor")
    except ValueError:
        print("Invalid Character")
main()

