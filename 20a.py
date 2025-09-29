print("prime number checking")
print("--------------------")
n=int(input("Enter the number:"))
print("Result")
if n<=1:
    print(n,"is not a prime")
else:
    count=0
    for i in range(2,n):
        if n%i==0:
            copunt+=1
            break
        if count ==0:
            print(n,"is a prime")
        else:
                print(n,"is not a prime")
