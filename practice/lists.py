game_points: list[int] = [102, 86, 94]


def display(game_points) -> None:
    index: int = 0
    while index < len(game_points):
        print(game_points[index])
        index += 1


display(game_points)
