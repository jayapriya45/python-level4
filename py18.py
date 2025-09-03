print("FIBONSCCI SERIES")
print("----------------")
n=int(input("Enter the number:"))
print("Fibonacci series:")
a = -1
b = 1
for i in range(n):
    c=a+b
    print(c, end=" ")
    a = b
    b = c
