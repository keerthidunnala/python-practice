#Program to create two lists with EVEN numbers and ODD numbers from a list.
list=[2,3,4,5,6,7,8]
listOdd=[]
listEven=[]
for num in list:
 if num%2 ==0:
     listEven.append(num)
 else:
     listOdd.append(num)
     print("list: ",list)
     print("listEven:",listEven)
     print("listOdd: ",listOdd)

