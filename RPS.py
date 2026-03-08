import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

rounds = int(input("How many rounds would you like to play? "))

print("\nStarting Rock Paper Scissors!\n")

for round_number in range(1, rounds + 1):
    print(f"Round {round_number}")
    
    player = input("Choose rock, paper, or scissors (or quit): ").lower()

    if player == "quit":
        print("Game ended early.")
        break

    if player not in choices:
        print("Invalid choice. Round skipped.\n")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

print("Final Score")
print(f"You: {player_score} | Computer: {computer_score}")

if player_score > computer_score:
    print("🏆 You won the game!")
elif computer_score > player_score:
    print("🤖 Computer won the game!")
else:
    print("It's a draw!")
