"""The building blocks for wordle"""

__author__ = "730751255"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
    exit()


# must exit the function after error message so that the user input restarts


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
    exit()


# must exit the function after error message so that the user input restarts


def contains_char(word: str, letter: str) -> None:
    print("searching for " + letter + " in " + word)
    count: int = 0
    if letter == word[0]:
        print(letter + " found at index 0")
        count += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count += 1
    # check if the character matches at each index of the word
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    # I only added this for grammatic purposes. '1 instances' doesn't make sense
    else:
        print("no instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
