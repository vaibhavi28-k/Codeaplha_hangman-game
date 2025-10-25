import random

# List of predefined words
words = ["apple", "table", "chair", "mouse", "phone"]

def hangman():
    word = random.choice(words)
    word_list = ["_"] * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(" ".join(word_list))

    while not guessed and tries > 0:
        guess = input("Enter a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word)
                indices = [i for i, letter in enumerate(word_as_list) if letter == guess]
                for index in indices:
                    word_list[index] = guess
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_list = list(guess)
        else:
            print("Not a valid guess.")

        print(display_hangman(tries))
        print(" ".join(word_list))

    if guessed:
        print("Congratulations, you guessed the word!")
    else:
        print("Sorry, you ran out of tries. The word was " + word)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |
