def right_star_triangle(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (i + 1))

n = int(input("Enter n: "))
right_star_triangle(n)

