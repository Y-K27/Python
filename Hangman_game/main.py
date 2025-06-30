import random 
import os
from pathlib import Path
from state_stages import stage_list, the_game_over_print, logo


file_path =Path("word_base.csv")
with open(file_path, 'r') as words_list:                                                                                    #import our words from .csv file in root folder
    words = [el.split(',') for el in words_list.readlines()][0]
    


def phrase_input(gamer_input):
    cmd, *args = gamer_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def game_body():
#create hidden word, every char will be changed to "_" 
    hidden_word =''
    history_letter_list = []
    chosen_word = random.choice(words).lower()
    for letter in chosen_word:                                                                                              # change all characters in the chosen word to the symbol  "_"
        hidden_word+="_"
    hidden_word = list(hidden_word)
    try_count = 1                                                                                                           # attempt count 
    max_try = len(stage_list)
    game_over = False
    inputted_letters = False
    print(stage_list[0])
    while not game_over:
        os.system("cls")                                                                                                    # clear CLI (only for Windows/for Linux need change "cls" -> "clear")
        print("-----------------------------  YOUR LIFE  -------------------------------")                                  # print how many lives are left/total 
        print(f"--------------------------------  {max_try-try_count}/{max_try-1}  ----------------------------------")
        print(stage_list[try_count-1])
        print("".join(hidden_word))                                                                                         # print chosen word with hidden chars 
        print(f"History: [ {" ".join(history_letter_list)} ]")
        if inputted_letters:
            print("You've already entered that letter, please try again.")
            inputted_letters = False
        inputted_letter = input("Guess a letter: ").lower()
        if len(inputted_letter) == 1 and inputted_letter.isalpha():                                                         # check if the inputted symbol is a letter 
            if inputted_letter not in history_letter_list:
                history_letter_list.append(inputted_letter)
                if inputted_letter in chosen_word:                                                                              # check if the inputted symbol is in the chosen word:
                    for char in range(len(chosen_word)):
                        if chosen_word[char] == inputted_letter:
                            hidden_word[char]=inputted_letter
                else:
                    if try_count <= (len(stage_list)-1):                                                                        # print new/current stage of game
                        print(stage_list[try_count])
                    try_count+=1
                if try_count >= max_try:                                                                                        # clear CLI & if "life" is over print element from the_game_over_print & ended the loop 
                    os.system("cls")
                    print(f"{the_game_over_print[1]}\n\nThe hidden word is {chosen_word}")
                    game_over = True

                if "_" not in hidden_word:                                                                                      # when all the letters have been guessed, & clear CLI &  it displays the text "you win!"
                    os.system("cls")
                    print(f"{the_game_over_print[0]}\n\nThe hidden word is {chosen_word}")
                    game_over = True
            else:
                inputted_letters =True
        else:
            print("You entered an invalid character. Please enter a letter.")

def main():
    print(logo)
    game = True
    while game:
        print("For starting new game enter \"start\"")
        gamer_input = input("Please enter a command: ")
        command, *args = phrase_input(gamer_input)                                                                          # clear inputted command & split it 
        
        if command in ["close", "exit"]:
            print("Good bye!")
            game = False
        elif command == "start":
            print("The game begin:")
            game_body()
            print("\nThe game is over.\nTo exit the program, enter \"exit\".\n")
        else:
            print('\nThe entered command is incorrect.\nTo start the game, enter "start".\nTo exit the program, enter "exit".\n')
            
if __name__ == "__main__":
    os.system("cls")
    main()
