import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

correct_letters = []
game_over = False

# start placeholder
display = "_" * word_length
print(display)

print(logo)

while not game_over:
    print(f"\n******** {lives}/6 LIVES LEFT ********")

    guess = input("Guess a letter: ").lower()



    if guess in correct_letters:
        print(f"You've already guessed '{guess}'")
        continue

    # Add only once
    correct_letters.append(guess)

    new_display = ""

    for letter in chosen_word:
        if letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's wrong. You lose a life.")

        if lives == 0:
            print(stages[0])
            print(f"\nYOU LOSE! The word was: {chosen_word}")
            game_over = True
            break

    print(stages[lives])

    if "_" not in display:
        print(f"\nYOU WIN! The word was: {chosen_word}")
        game_over = True
