#alternate prime
from math import sqrt  
def isPrime(num):
   for i in range(2,int(sqrt(num))+1):
       if num % i == 0:
           return False
   return True
count = 1
for num in range(2,500):   
   if isPrime(num):   
       count += 1
       if count % 2 == 0: 
           print(num)

