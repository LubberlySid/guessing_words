"""
In this game you need to guess the word from list(the word is chosen randomly)
"""
import random


def word_formation(word, guessed_letters):
    """
    This function form a string with displayed letters and unguessed letters marked as *
    """
    result = ""

    for letter in word:
        if letter in guessed_letters:
            result += letter

        else:
            result += "*"

    return result


def main():
    """
    This is main function for our game
    """
    list_of_words = ["smartphone", "ice-cream", "sun", "book", "table", "apple"]

    selected_word = random.choice(list_of_words)
    guessed_letters = []

    number_of_attempts = int(input("\nEnter the number: "))

    if number_of_attempts <= 0:
        print("You enter wrong value")

    elif number_of_attempts == 1:
        print(f"You have {number_of_attempts} chance to guess the word")

    else:
        print(f"You have {number_of_attempts} chances to guess the word")

    while True:
        display = word_formation(selected_word, guessed_letters)
        print(display)

        if "*" not in display:
            print(f"Congratulations! You guess the word: {selected_word}")
            break

        if number_of_attempts <= 0:
            print(f"You've run out of attempts. The word was {selected_word}")

        user_input = input("Enter the word/letter: ").lower()

        if len(user_input) != 1 or not user_input.isalpha():
            print("Enter the single letter")

        if user_input in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.append(user_input)

        if user_input in selected_word:
            print("Correct!")

        else:
            number_of_attempts -= 1
            print(f"Wrong! You have {number_of_attempts} attemtp(-s) left")


main()
