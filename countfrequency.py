inputString=input("Enter the string:")
li=inputString.split()
freq={}
for item in li:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
print(freq)