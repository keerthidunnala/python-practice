str=input("Enter string ")  
c=len(str)
words=str.split(" ")  
count=0
for word in words:
    for ch in word:
        count=count+1
print("without space",count)
print("with space",c)