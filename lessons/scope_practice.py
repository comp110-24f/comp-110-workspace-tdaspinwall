def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if char != msg[index]:
            copy = copy + msg[index]
        index += 1
    return copy


word: str = "yoyo"
(remove_chars(word, "o"))

print(copy)
