import random
print("Welcome to rock, paper, scissors! To play enter r for rock, p for paper, or s for scissors. i assume you know the rules :3")
def myfun():
    x = input("what will it be?: ")
    c = random.randint(1, 3)
    r = 1
    p = 2
    s = 3
    if x == r and c == 1:
        print("rock and rock, its a tie!")
    elif x == r and c == 2:
        print("paper covers rock, you lose :(")
    elif x == r and c == 3:
        print("rock beats scissors, you win!")
    elif x == p and c == 2:
        print("paper and paper, its a tie!")
    elif x == p and c == 3:
        print("scissors cuts paper, you lose :(")
    elif x == p and c == 1:
        print("paper covers rock, you win!")
    elif x == s and c == 3:
        print("both chose scissors, its a tie!")
    elif x == s and c == 1:
        print("rock beats scissors, you lose :(")
    else:
        print("scissors cuts paper, you win!")
myfun()
p = input("do you want to play again? y/n: ")
while p == "y":
    myfun()
    p = input("do you want to play again? y/n: ")
else:
    print("good game!")