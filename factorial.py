#program to find factorial of a number

 

def factorial(num):
    fact=1
    for i in range(1, num+1):
        fact=fact*i
    return fact    
number=int(input(" enter any number to find factorial: "))
result=factorial(number)
print("Factorial of",number, "is",result)