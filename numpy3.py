s=input()
alphabets=digits=special=0
for i in range(len(s)):
    if(s[i].isalpha()):
        alphabets=alphabets+1
    elif(s[i].isdigit()):
        digits=digits+1
    else:
        special=special+1
print("-Number of characters:",alphabets,"-Number of digits:",digits,"-Number of special characters:",special)
