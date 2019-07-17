def main():
    try:
        a=input()
        print(a)
        n=int(a)
        if(n<0):
            print("Negative Number")
        elif((n%2)==0):
            print("The Number is Even")
        elif((n%2)==1):
            print("The Number is Odd")
    except ValueError:
        print("Invalid Character")
main()

