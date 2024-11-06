__author__ = "730751255"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    while index1 < len(xs):
        index2: int = 0
        while index2 < len(ys):
            print("(" + xs[index1] + ",", ys[index2] + ")")
            index2 += 1
        index1 += 1


if __name__ == "main":
    get_coords("hi", "bye")
