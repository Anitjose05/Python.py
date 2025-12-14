import random
small=int(input("Enter the smaller no: "))
large=int(input("Enter the larger no: "))
random_no=random.randint(small,large)
count=0
while True:
    user_no=int(input("Enter your guess: "))
    count+=1
    if user_no<random_no:
        print("Too small")
    elif user_no>random_no:
        print("Too large")
    else:
        print("Congratulations! You guessed it in",count,"tries.")
        break