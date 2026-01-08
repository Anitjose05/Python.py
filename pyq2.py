
user_details={"Ram":25,"Shyam":30,"Mohan":22}
name=input("Enter the name:")
print("Age of", name,"is", user_details.get(name, "Name not found"))