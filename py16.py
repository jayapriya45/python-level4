print("Factorial program")
print("-----------------")
n=int(input("Enter the numbers:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print("fact:",fact)
