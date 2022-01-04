 #Program to find the position of minimum and maximum elements of a list.
list=[2,3,4,5,6]
min_ele,max_ele =list[0],list[0]
for i in range(1,len(list)):
    if list[i]<min_ele:
        min_ele =list[i]
    if list[i]>max_ele:
        max_ele = list[i]
        print('Minimum Element in the list',list,'is',min_ele)
        print('Maximum Element in the list',list,'is',max_ele)