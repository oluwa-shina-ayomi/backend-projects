import random
from datetime import datetime
def main():
    print("""Welcome to thhe number guessing game!
    I'm thinking of a number betweeen 1 and 100

    Please select a difficulty level
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
        
    """)
    level = choose_level()
    print()
    if level == 1:
        print("Great! you have selected the Easy difficulty level")
        play(10)
    elif level == 2:
        print("Great! you have selected the Medium difficulty level")
        play(5)
    elif level == 3:
        print("Great! you have selected the Hard difficulty level")
        play(3)

def choose_level():
    while True:
        try:
            level = int(input("Enter your choice (level 1, 2 or 3): ").strip())
        except ValueError:
            print("Enter a valid number")
        else:
            if 1 <= level <= 3:
                return level
            else:
                print("Choose between 1-3")

def play(level):
    start_time = datetime.now()
    tries = 0
    number = random.randint(1, 100)
    print(number)
    print("Let's start the game!")
    print()
    for _ in range(level):
        try:
            guess = int(input("Enter your guess: ")) 
            tries += 1
        except ValueError:
            tries +=1
            print("Incorrect you did'nt enter a number") 
            print()
            continue   
        else:
            if number == guess:
                print(f"Congratulations! You guessed the correct number in {tries} attempts")
                print()
                end_time = datetime.now()
                elapsed = end_time - start_time
                total_seconds = elapsed.total_seconds()

                hours = total_seconds // 3600
                minutes = (total_seconds % 3600) // 60
                seconds = total_seconds % 60

                print(f"Elapsed time: {hours}h {minutes}m {seconds:.2f}s")
                keep_playing()
                break
            elif guess > number:
                print(f"Incorrect! The number is less than {guess}.")
                print()
            else:
                print(f"Incorrct! The number is greater than {guess}.")
                print()

    else:
        print("Sorry, you lose - you've ran out of tries")
        print()
        keep_playing()

def keep_playing():
    response = input("wanna keep playing, yes or no? ").strip().lower()
    if response == "yes":
        level = choose_level()
        if level == 1:
            play(10)
        elif level == 2:
            play(5)
        elif level == 3:
            play(10)
    else:
        print("Byeeeeeee")
    
if __name__ == "__main__":
    main()