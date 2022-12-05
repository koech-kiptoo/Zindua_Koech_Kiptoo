import random

dict = {
    "animals": ['cat', 'dog', 'elephant', 'monkey', 'lion', 'zebra'],
    "cars": ['toyota', 'nissan', 'mazda', 'bmw', 'suzuki', 'kia'],
    "weather": ['rainny', 'sunny', 'muddy', 'hot', 'cold', 'warm', 'sunset']
}


def get_nth_key(dictionary, n=1):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")


#print(get_nth_key(dict, n=random.randint(1, len(dict)) - 1))
#print(random.choice(dict[get_nth_key(dict)]))

def get_word():
    word = random.choice(dict[get_nth_key(dict)])
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    fully_guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 5
    print("Lets Play Hangman!")
    print(display_hangman(attempts))
    print(word_completion)
    print("\n")
    while not fully_guessed and attempts >= 0:
        guess = input("Please guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, " is not in the word")
                attempts -= 1
                guessed_letters.append(guess)
                print(display_hangman(attempts))

            else:
                print("Great, ", guess, " is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)

                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                print(word_completion)
                if "_" not in word_completion:
                    fully_guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word...", guess)
            elif guess != word:
                print(guess, "is not the word.")
                attempts -= 1
                guessed_words.append(guess)
                print(display_hangman(attempts))
            else:
                fully_guessed = True
                word_completion = word

    else:
        print("Not a valid guess.")
        print(display_hangman(attempts))
        print(word_completion)
        print("\n")
        if fully_guessed:
            print("Congrats You Win, the word was", word)
        else:
            print("You Lost, the word was ", word)


def display_hangman(tries):
    stages = [
        """
        -----------
        |          |
        |          o
        |         -|-
        |         / \
        |
        """
        ,
        """
        -----------
        |          |
        |          o
        |          |
        |         / \
        |
        """
        ,
        """
        -----------
        |          |
        |          o
        |          |
        |          |
        |
        |
        """
        ,
        """
        -----------
        |          |
        |          o
        |          |
        |
        |
        """
        ,
        """
        - ----------
        |          |
        |          o
        |
        |
        |

        """
        ,
        """
        -----------
        |         |
        |
        |
        |
        |
        """
    ]
    return stages[tries]


def main():
    test = get_word()
    play(test)


if __name__ == "__main__":
    main()
