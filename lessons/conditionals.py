def less_than_10(num: int) -> bool:
    """Tell us if num < 10"""
    if num < 10:
        return True
    else:
        return False


def wake_up(alarm: bool) -> str:
    if alarm:
        return "wake up!"
    else:
        return "Keep sleeping"


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match"
    else:
        return "no match"


print(check_first_letter(word="letter", letter="h"))
