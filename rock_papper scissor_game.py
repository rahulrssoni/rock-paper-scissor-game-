import random
 
choices = ["rock", "paper", "scissors"]
 
print("Rock Paper Scissors!")
print("Enter rock, paper, or scissors. Type 'quit' to exit.")
 
user_score = 0
cpu_score = 0
 
while True:
    user_choice = input("Your choice:").strip().lower()
    if user_choice == "quit":
        print(f"\nFinal Score — You: {user_score} | CPU: {cpu_score}")
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue
 
    cpu_choice = random.choice(choices)
    print(f"CPU chose: {cpu_choice}")
 
    if user_choice == cpu_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and cpu_choice == "scissors") or \
         (user_choice == "scissors" and cpu_choice == "paper") or \
         (user_choice == "paper" and cpu_choice == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("CPU wins this round!")
        cpu_score += 1
 
    print(f"Score — You: {user_score} | CPU: {cpu_score}")