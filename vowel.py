c=input()
if c in ["a","e","i","o","u","A","E","I","O","U"]:
    print(c, "is a Vowel")
elif (c>='a'and c<='z' or c>='A' and c<='Z'):
    print(c, "is a Consonant")
else:
    print("invalid Character")
