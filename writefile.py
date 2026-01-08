with open ("note.txt","w") as file:
    file.write("This is a new text.\n")

with open ("note.txt", "a") as file:
    file.write("This line added to the bottom.")