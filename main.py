import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Hádej písmeno: ").lower()

    clear()

    if guess in display:
        print(f"Písmeno --> {guess.upper()} <-- jsi už hádal!")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"Hádáš písmeno --> {guess.upper()} <--, toto písmeno ve slově není! Ztráčíš 1 život!")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("Prohrál jsi!")
    
    if not "_" in display:
        game_is_finished = True
        print("Vyhrál jsi!")

    print(stages[lives])
