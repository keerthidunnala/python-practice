#Python program to check if an element is present in list.
test_list = [1, 6, 3, 5, 3 , 4]

print("Checking if 5 exists in list (using loop) : ")
for i in test_list:
    if(i==5) :
        print("Element Exists")
        
print("Checking if 5 exists in list (using in ): ")
if(5 in test_list):
    print("Element Exists")