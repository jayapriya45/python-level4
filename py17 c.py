print("Sum of n numbers")
print("----------------")
start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
difference=int(input("Enter the difference:"))
print("result")
print("series")
sum=0
count=0
for i in range(start,end+1,difference):
  print(i,end=" ")
  sum+=i
  count+=1
  print("\nSum value:",sum)
  print("\ncount value:",count)
