#Write Java Python  Program to read 5 marks subject from user and print the Average.
#Enter the 1st Subject Mark: 98 Enter the 1st Subject Mark: 87 Enter the 1st Subject Mark: 80 Enter the 1st Subject Mark: 91 Enter the 1st Subject Mark: 94 Output:
#Student Information
#Marks Secured - 98 , 87 , 80 , 91 , 94
#Total = 450
#Average Percentage is: 90
a=int(input("Enter First marks:"))
b=int(input("Enter second marks:"))
c=int(input("Enter Third marks:"))
d=int(input("Enter Fourth marks:"))
e=int(input("Enter Fifth marks:"))
print("Student Information")
print("Marks Secured - 98,87,80,91,94",sep=',')
Totalmarks=(a+b+c+d+e)
print("Totalmarks: ",Totalmarks)
Averagepercentage=(Totalmarks)/(500)*(100)
print("Averagepercentage: ",Averagepercentage)