print("Prime number checking")
print("---------------------")
sn=int(input("enter the starting number:"))
en=int(input("enter the ending number:"))
print("result")
for n in range(sn,en+1):
    if n<=1:
        print(n,"is not a prime")
        count=0
        for i in range(2,int(n**0.5)+1):
            count+=1
            breaki
            if count==0:
                print(n,"is a prime")
            else:
                    print(n,"is not a prime")
