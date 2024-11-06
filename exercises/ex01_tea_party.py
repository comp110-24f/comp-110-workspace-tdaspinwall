"""Program for determining the cost of a tea party"""

__author__: str = "730751255"


def main_planner(guests: int) -> None:
    """Brings everything together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    # Since I can't mannually type the number of people, the variable people must come from guests
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """determines the number of teabags based on the amount of people"""
    return people * 2


def treats(people: int) -> int:
    """determines how many treats will be needed based on amount of people and tea_bags"""
    return int((tea_bags(people=people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """computes the cost of tea bags and treats combined"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
