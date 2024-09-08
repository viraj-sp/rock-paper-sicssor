import random

c = ["rock", "paper", "scissors"]
u_c = input("Enter a choice (rock, paper, scissors): ").lower()
c_c = random.choice(c)

print(f"\nYou chose {u_c}, computer chose {c_c}.")

if u_c == c_c:
    print("It's a tie!")
elif (u_c == "paper" and c_c == "rock"):
    print("You win!")
elif (u_c == "rock" and c_c == "scissors"):
    print("You win!")
elif (u_c == "scissors" and c_c == "paper"):
    print("You win!")
else:
    print("You lose!")