import random
from hangman_art import logo, stages
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_over = False
lives = 5

print(logo)
print("Guess the word by filling the blank spaces")

display = []

for _ in range(word_length):
    display += "_"
print(f"The word contains  {word_length} alphabets")

while not game_over:
    guess = input("Guess a letter : ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess} which is not in the chosen word. You lose a life!")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")

    print(f'{"".join(display)}')

    if "_" not in display:
        end_of_game = True
        print("You won!")

    print(stages[lives])