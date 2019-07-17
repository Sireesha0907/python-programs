n=(int(input("Enter the size of an Array : ")))
ary=[]
for _ in range(n):
    a=(int(input("Enter Array Elements: ")))
    ary.append(a)
print("The Array Elements: ",ary)
m=(int(input("Number of Elements to be Added : ")))
ary1=[]
ary1 = ary[:m].copy()
print("The Sum Of Array is : ",sum(ary1))

