def transpose(matrix):
    print("\nTranspose:")
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()

def add(a, b):
    print("\nAddition:")
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j] + b[i][j], end=" ")
        print()

def multiply(a, b):
    print("\nMultiplication:")
    for i in range(len(a)):
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            print(total, end=" ")
        print()

# Part A
r = int(input("Rows: "))
c = int(input("Columns: "))

matrix = []
print("Enter the matrix:")
for i in range(r):
    matrix.append(list(map(int, input().split())))

transpose(matrix)

# Part B
print("\nEnter first matrix:")
a = []
for i in range(r):
    a.append(list(map(int, input().split())))

print("Enter second matrix:")
b = []
for i in range(r):
    b.append(list(map(int, input().split())))

add(a, b)

# Part C
r1 = int(input("\nRows of A: "))
c1 = int(input("Columns of A: "))
r2 = int(input("Rows of B: "))
c2 = int(input("Columns of B: "))

if c1 != r2:
    print("Matrices cannot be multiplied.")
else:
    print("Enter matrix A:")
    A = []
    for i in range(r1):
        A.append(list(map(int, input().split())))

    print("Enter matrix B:")
    B = []
    for i in range(r2):
        B.append(list(map(int, input().split())))

    multiply(A, B)1