import random
from time import sleep

def welcome_screen():
    """
    Prints out a welcome message and instructions for the game.
    """
    
    sleep(0.5)
    print('''
      
      
Hello Mortal, It's me again - The Sentient Being
Let's Play a Game.
               
It's like WORDLE but for numbers.
So
       
███    ██ ██    ██ ██████  ██████  ██      ███████    
████   ██ ██    ██ ██   ██ ██   ██ ██      ██      ██ 
██ ██  ██ ██    ██ ██████  ██   ██ ██      █████      
██  ██ ██ ██    ██ ██   ██ ██   ██ ██      ██      ██ 
██   ████  ██████  ██   ██ ██████  ███████ ███████    
                                                      
 ██████  ███    ██ ██      ██    ██     ███████  ██████  ██████      ███    ██ ███████ ██████  ██████  ███████ 
██    ██ ████   ██ ██       ██  ██      ██      ██    ██ ██   ██     ████   ██ ██      ██   ██ ██   ██ ██      
██    ██ ██ ██  ██ ██        ████       █████   ██    ██ ██████      ██ ██  ██ █████   ██████  ██   ██ ███████ 
██    ██ ██  ██ ██ ██         ██        ██      ██    ██ ██   ██     ██  ██ ██ ██      ██   ██ ██   ██      ██ 
 ██████  ██   ████ ███████    ██        ██       ██████  ██   ██     ██   ████ ███████ ██   ██ ██████  ███████ 
                                                                                                                                                                
''')
    sleep(2)
    print('''

Before we begin, here are some instructions:
 -> You will first tell me how long of a number should I think of
 -> You will try to guess this number in as few guesses as possible 
 -> Each guess must be of this specified length only
 -> A symbol would appear at the digit's position to show how close your guess was to the actual number.
       ✓ means your guess's digit is at the correct position
       ? means your guess's digit is not at the correct position, but exists elsewhere in the number
       ✗ means your guess's digit is nowhere in the number
          
For Example:- 
    If the number was 65343 and your guess was 61932, you'd see:
    Your Guess: 6 1 9 3 2
    Result:     ✓ ✗ ✗ ? ✗
          
          
''')


# Defining Function to check guesses
def match_displayer(number,guess,unused_digits):
    """
    Checks each digit in the guess against the actual number and displays:
    - ✓ if the digit is correct and in the correct position. [\u2713]
    - ? if the digit is in the number but in a different position.
    - ✗ if the digit is not in the number at all. [\u2717]
    """
    #Converting both guess and numboi back to strings
    number_str = str(number)
    guess_str = str(guess)
    result_display = []
    
    for i in range(len(guess_str)):
        if guess_str[i] == number_str[i]:
            result_display.append('✓')
        elif guess_str[i] in number_str:
            result_display.append('?')
        else:
            result_display.append('✗')
            unused_digits.discard(guess_str[i])
    
    print("\nYour Guess: ", ' '.join(list(guess_str)))
    print("Result:     ", ' '.join(result_display))
    return unused_digits

def get_random_nurdle():
    """
    Prompts the user to select a digit length for a number and generates a random number of that length.
    
    Returns a tuple containing:
    - numboi: The randomly generated number.
    - numboi_length: The length of the number.
    - guess_lim: The number of attempts allowed, which is one more than the length of the number.
    """
    print("So tell me How many digit number do you want me to think of?\n")
    while True:
        try:
            numboi_length = int(input("Select something between 2-10. Because that seems like a sane range\n\n\n"))
            if 2 <= numboi_length <= 10:
                break
            else:
                print("Please choose a length between 2 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    guess_lim = numboi_length + 1
    #Getting Random Number range
    BegRng = 10**(numboi_length-1)
    EndRng = 10**numboi_length-1
    numboi = random.randint(BegRng,EndRng)
    print("\n\n\nSo you want me to think of a",numboi_length, "digit number. Okay, you get",guess_lim, "attempts to guess it.\n")
    return numboi, numboi_length, guess_lim

def replay_prompt():
    """
    Prompts the user to select whether to replay the game or not. If the user chooses to replay, the game is restarted. If the user chooses not to replay, the program is quit.
    
    Returns nothing.
    """
    while True:
        try:
            replay = input("\nWould you like to play again? (y/n):\n").lower()
            if replay == 'y':
                start_game()
            elif replay == 'n':
                print("\nWhat are you waiting here for then? Go Awwwwwayyyy.\n")
                quit()
            else:
                print("Invalid Input. Please enter 'y' or 'n'")
        except ValueError:
            print("Invalid Input. Please enter 'y' or 'n'")



def start_game():
    """
    Main game loop. Prompts the user for guesses and checks against the secret number.
    If the user guesses correctly, the game ends and the user is prompted to replay.
    If the user exhausts all their guesses, the game ends and the user is prompted to replay.
    """
    
    welcome_screen()
    sleep(2)
    nurdle, nurdle_length, guess_limit = get_random_nurdle()
    unused_digits = set("0123456789")
    print("Alright, So let's begin!\n")
    
    attempt = 1
    while attempt <= guess_limit+1:
        print(f"Make up your Guess Number using these digits:- [{' '.join(sorted(unused_digits))}]\n")
        guess = input(f"Attempt {attempt}/{guess_limit}. Enter your guess:\n")
        if len(guess) != nurdle_length:
            print(f"\nPlease enter a {nurdle_length} digit number.\n")
            continue
        else:
            if int(guess) == nurdle:
                unused_digits = match_displayer(nurdle,guess,unused_digits)
                print(f"WhooHoo! You got it in {attempt} guesses")
                break
            else:
                if attempt == guess_limit:
                    unused_digits = match_displayer(nurdle,guess,unused_digits)
                    print(f"\nOh Human, You've exhausted all your guesses.\nHard Luck\nByeBye\nGo Away Now\nBTW, The Number was {nurdle}")
                    break
                else:
                    unused_digits = match_displayer(nurdle,guess,unused_digits)
                    print(f"Whopsies, That's not the number.\nBut you still have {guess_limit-attempt} guesses remaining")
        attempt += 1
    replay_prompt()

    
start_game()