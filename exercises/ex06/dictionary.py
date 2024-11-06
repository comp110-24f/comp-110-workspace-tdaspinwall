__author__ = "730751255"


def invert(vals: dict[str, str]) -> dict[str, str]:
    inverted_vals: dict[str, str] = {}
    for key in vals:
        if vals[key] in inverted_vals:
            raise KeyError("This value is already a key in inverted dict")
        inverted_vals[vals[key]] = key
    return inverted_vals


def favorite_color(colors: dict[str, str]) -> str:
    # make a new dictionary to store each color with its count
    color_count: dict[str, int] = {}
    for name in colors:
        color = colors[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    most_popular = ""
    max_count = 0
    for name in colors:
        color = colors[name]
        if color_count[color] > max_count:
            """if the count of the current color is greater than the color with the
            greatest count"""
            most_popular = color
            max_count = color_count[color]
        elif color_count[color] == max_count and most_popular is None:
            most_popular = color
    return most_popular


def count(vals: list[str]) -> dict[str, int]:
    count_of_vals: dict[str, int] = {}
    for item in vals:
        if item in count_of_vals:
            count_of_vals[item] += 1
        else:
            count_of_vals[item] = 1
    return count_of_vals


def alphabetizer(vals: list[str]) -> dict[str, list[str]]:
    alphabet_dict: dict[str, list[str]] = {}
    for word in vals:
        first_letter = word[0].lower()
        if first_letter in alphabet_dict:
            alphabet_dict[first_letter].append(word)
        else:
            alphabet_dict[first_letter] = [word]
    return alphabet_dict


def update_attendance(
    attendance_sheet: dict[str, list[str]], new_day: str, new_student: str
) -> None:
    if new_day in attendance_sheet:
        attendance_sheet[new_day].append(new_student)
    else:
        # if the day isn't in the sheet intialize it
        attendance_sheet[new_day] = [new_student]
