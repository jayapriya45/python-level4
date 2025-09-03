print("Sum of n numbers")
print("----------------")
start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
print("result")
total=0
for i in range(start,end+1):
    print("+" ,i,end=" ")
    total +=i
print("sum of values:",total)
