
import random


words = ["banana","dracula","python"]
word_random = random.choice(words)

empty_list = []
len_word = len(word_random)

lives = 3

for _ in range(len_word):
    empty_list+="_"

end_game = False

while not sfarsit_joc:

    letter_guess = input(" Choose a letter ! : ").lower()
    for poz in range(len_word):
        letter = word_random[poz]   
        if letter == letter_guess:
            empty_list[poz] = letter

    if letter_guess not in word_random:
           lives-=1
           print(f"You're wrong! you still have {lives} live !")
           if lives ==0:
               end_game = True
               print("You lose")


    print(empty_list)

    if "_" not in empty_list:
        end_game = True
        print("You won")