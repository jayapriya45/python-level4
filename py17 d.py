print("Sum of n numbers")
print("----------------")
sn=int(input("Enter the starting number :"))
en=int(input("Enter the ending number:"))
print("result")
print("series:",end=" ")
sum=0
count=0
for i in range(sn,en+1):
    if(i %5 == 0) and (i %3 == 0):
        print(i, end=" ")
        sum+=i
        count+=1
        print("\n\n su value:",sum)
        print("count values:",count)
