def feb_series(n):
    a,b=0,1
    if n>=1:
        print(a)
    if n>=2:
        print(b)
    for i in range(2,n):
        c=a+b
        print(c)
        a,b=b,c
n=int(input("Enter n :"))
feb_series(n)