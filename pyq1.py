record={"Choco":30,"Almond":25,"Ani":20,"Bee":15}
name=input("Enter the name:")
if name in record:
    print ("Age of", name,"is", record[name])
else:
    print("Name not found")



