"""challenge question 3"""

__author__ = "730751255"


def num_instances(phrase: str, search_char: str) -> None:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count += 1
        index += 1
    print(count)


num_instances("HelloHelloHello", "e")
