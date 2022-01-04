#Write a Python program to read a number n from the user and compute n+nn+nnn
#Example: If the n = 5
#5+55+555 = 615

#Input:
#Enter a number n: 5
#Output:
#The value is: 615

#Input:
#Enter a number n: 20
#Output:
#The value is: 204060
n=int(input("Enter a number n:"))
temp=str(n)
n1=temp+temp
n2=temp+temp+temp
comp=n+int(n1)+int(n2)
print("The value is:",comp)

