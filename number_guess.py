"""number_guess.py

Author: Juan Diego Becerra
Created: 2022-04-09
"""
import os


MAX_NUM = 1000
MIN_NUM = 1


def main():
    play()


def play():
    # Display title
    with open("assets/title.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
    print("\t      v1.0")
    print("Author: Juan Diego Becerra")
    print("GitHub: https://github.com/jbesoto\n")

    # Diplay information
    print("─────────────────────  INSTRUCTIONS  ─────────────────────")
    print("Choose a number between 1 and 1000.")
    print("Answer Yes/No questions and I will try to guess your\nnumber under 10 tries.")
    print("Type `Ctrl + C` to exit the game.")
    print("Here we go!\n")
    
    while guess():
        os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal
        play()


def guess():
    ans = input("Your number: ").strip()
    while not is_valid_number(ans):
        ans = input("Your number: ").strip()
    print()
    
    high, low = MAX_NUM, MIN_NUM
    middle = high // 2

    for attempt in range(1, 11):
        print(f"Guess #{attempt}:")
        print("──────────────────────────────────────────")
        res = input(f"Is your number greater than {middle}? (Y/n): ").strip().lower()
        while res not in ['y', 'n']:
            res = input(f"Is your number greater than {middle}? (Y/n): ").strip().lower()
        print()

        if res == 'y':
            low = middle + 1
            middle = (low + high) // 2
        elif res == 'n':
            high = middle - 1
            middle = (high + low) // 2
        if low >= high:
            print(f"Your number is {middle}!")
            break

    return True if input("Press 'S' to play again or 'Enter' to exit: ").lower() == "s" else False


def is_valid_number(ans: int) -> bool:
    try:
        ans = int(ans)
    except ValueError:
        print("Oops! Number cannot be a letter or symbol. Try again.")
        return False
    
    if not (MIN_NUM <= ans <= MAX_NUM):
        print("Oops! Number must be between 1 and 1000. Try again.") 
        return False
    
    return True


if __name__ == '__main__':
    main()