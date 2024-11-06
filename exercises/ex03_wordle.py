__author__ = "730751255"


def input_guess(secret_word_length: int) -> str:
    guess: str = input(f"Enter a {secret_word_length} character word: ")
    while len(guess) != secret_word_length:
        guess = input(f"That wasn't {secret_word_length} chars! Try again: ")
    return guess


# return guess rather than printing so it is stored in the function


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    # basically a short cut for using an exit()
    index: int = 0
    while index < len(secret_word):
        if char_guess == secret_word[index]:
            return True
            exit()
        index += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    index: int = 0
    emoji_str: str = ""
    # empty string that the emojis will be cancatted with
    while index < len(secret):
        if (
            contains_char(secret_word=secret, char_guess=guess[index])
            and guess[index] == secret[index]
        ):
            emoji_str += GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            emoji_str += YELLOW_BOX
        else:
            emoji_str += WHITE_BOX
        index += 1
    return emoji_str


def main(secret: str) -> None:
    turn: int = 0
    win: bool = False
    while turn < 6 and not win:
        turn += 1
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        # parameter for input guess needs to vary. Can't always be the same
        print(emojified(guess, secret))
        if guess == secret:
            win = True

    if win:
        print(f"You won in {turn}/6 turns!")

    else:
        print("X/6 - Sorry, try again tommorow!")


if __name__ == "__main__":
    main(secret="codes")
