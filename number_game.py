import random
number = random.randint(1, 10)
n=5
for i in range(n):
    print("range is 1 to 10")
   
    guess_number=int(input("enter a number : "))
    if guess_number<number:
        print("Go Higher!!!")
    elif guess_number>number:
        print("Go Slower!!!")
    else:
        print("YOU WON THE GAME!!!!!!")



