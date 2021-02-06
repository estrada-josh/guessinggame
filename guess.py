import time

def guessing_game(secret_int):
    user_guess = 0
    while user_guess != secret_int:
        user_guess = input("\nWhat number am I thinking of?... ")
        guess = int(user_guess)
        if guess == secret_int:
            print("\nYOU WIN!!\n")
            time.sleep(1)
            print("Goodbye.")
            time.sleep(1)
            exit()
        if (guess == secret_int + 1) or (guess == secret_int - 1):
            print("\nYou are warm...")
            time.sleep(1)
            print("\n...but...")
            time.sleep(1)
            print("\nWRONG! Try again")
            time.sleep(1)
            continue
        print("\nWRONG! Try again")
        time.sleep(1)
        continue

print("Hello...\n")
time.sleep(1)
print("Welcome to the guessing game...\n")
time.sleep(1)
print("Pick your difficulty\n")
user_pick = input("Easy, Medium, or Hard?... ")

easy = "Easy"
low_easy = "easy"
med = "Medium"
low_med = "medium"
hard = "Hard"
low_hard = "hard"

if (user_pick == easy) or (user_pick == low_easy):
    guessing_game(7)

if (user_pick == med) or (user_pick == low_med):
    guessing_game(17)

if (user_pick == hard) or (user_pick == low_hard):
    guessing_game(77)
