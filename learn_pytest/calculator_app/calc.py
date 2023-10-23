from icecream import ic


def simple_calculator(
    num_1: float | int, num_2: float | int, operation: str
) -> float | int:
    match operation:
        case ("/"):
            return num_1 / num_2
        case ("*"):
            return num_1 * num_2
        case ("+"):
            return num_1 + num_2
        case ("-"):
            return num_1 - num_2


if __name__ == "__main__":
    ic(simple_calculator(2, 3, "/"))
