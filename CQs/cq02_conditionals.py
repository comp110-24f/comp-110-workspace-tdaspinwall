"""2nd challenge question"""

__author__ = "730751255"


def guess_a_number() -> None:
    secret: int = 7
    guess: int = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    if guess == 7:
        print("You got it!")
    elif guess < 7:
        print("Your guess was too low! The secret number is 7")
    else:
        print("Your guess was too high! The secret number is 7")


if __name__ == "__main__":
    guess_a_number()
