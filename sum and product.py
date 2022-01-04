#1. Accept two integer values from the user and return their product. If the product is greater than 1000, then return their sum

#Input Format:
#Line 1: 1st Number value Line 2: 2nd Number value Output Format:
#Line 1: Result of the operation

#Input:
#10
#20
#Output:
#200

#Input:
#20
#30
#Output:
#600

#Input:
#40
#30
#Output:
#70
Line1=int(input("1st number value "))
Line2=int(input("2nd number value"))
product=(Line1*Line2)
sum=(Line1+Line2)
if product<=1000:
    print(product)
else:
    print(sum)
        
    