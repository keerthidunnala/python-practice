#num
p=int(input('start='))
n=int(input('end='))
if p<n:
    for i in range(p,n):
        print(i)
elif p>n:
    for i in range(n-1,p):
        print(p)
        p=p-1