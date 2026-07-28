def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci sequence:", end=" ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def check(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    if a == num:
        print(num, "is a Fibonacci number.")
    else:
        print(num, "is NOT a Fibonacci number.")

n = int(input("How many terms? "))

if n <= 0:
    print("Error: N must be a positive integer.")
else:
    fibonacci(n)

num = int(input("Enter a number to check: "))
check(num)
