def main():
    try:
        a=input()
        print(a)
        n=int(a)
        if((int(a)%2)==1):
            print("The Number is Odd")
        elif((int(a)%2)==0):
            print("The Number is Even")
    except ValueError:
        print("Invalid Character")
main()
