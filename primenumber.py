def prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime")

n = int(input("Enter n: "))
prime_num(n)



