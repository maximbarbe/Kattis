import random 


for i in range(1000):
    guess = chr(ord('A') + (random.randint(0, 2) %3))
    print(guess)
    data = input().split(" ")
    if data[1] == "1":
        print(data[0])
    else:
        if data[0] == "A":
            if guess == "B":
                print("C")
            else:
                print("B")
        elif data[0] == "B":
            if guess == "A":
                print("C")
            else:
                print("A")
        else:
            if guess == "A":
                print("B")
            else:
                print("A")
    input()