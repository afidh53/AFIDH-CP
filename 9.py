str2=input("enter the string:")
word={}
for char in str2:
    if char in word:
        word[char] +=1
    else:
        word[char]=1
print("characterfrequency:")
for char,count in word.items():
    print(f"{char}:{count}")