def amstrong(n):
    p=len(str(n))
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**p
        temp=temp//10
    if n==sum:
        print("Amstrong")
    else:
        print("Not Amstrong")

n=int(input("Enter n"))
amstrong(n)


