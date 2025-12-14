for i in range(5):
    for j in range(1,6-i):
        print(j, end=' ')   
    print()



n=int(input("Enter a positive numbers: "))
even=0
odd=0
while n>0:
    digit=n%10
    if digit%2==0:
        even += 1
    else:
        odd +=  1
    n=n//10

print("Even:",even)
print("Odd:",odd)    
if(even>odd):
    print("More even digits")   
elif(odd>even):
    print("More odd digits")

else:
    print("Equal even and odd digits")
