#Strings
str1 = 'keerthi'
str2 = 'shiva'
l = len(str1)//2
str3 = str1[0:l] + str2 + str1[l::] 
print(str3)