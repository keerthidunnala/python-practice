#Write a Python program to read 2 string values from the user and check whether all the characters of String1 are present in String2.

n =  input ("enter the number of string1")
v =  input ("enter the number of string2") 
count=0
for i in range(0,len(n)-1):
    for j in range(0,len(n)-1):
        if n[i]==v[j]:
            count=count+1
if count>1:
    print("1")
else:
    print("-1")