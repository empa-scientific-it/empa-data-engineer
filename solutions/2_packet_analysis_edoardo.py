import pathlib

# check out: https://docs.python.org/3/library/functools.html#functools.cmp_to_key
from functools import cmp_to_key

# check out: https://docs.python.org/3/library/itertools.html?itertools.chain#itertools.chain
from itertools import chain


def parse(puzzle_input: str) -> list:
    """Parse input"""
    puzzle_input = [p.split("\n") for p in puzzle_input.split("\n\n")]
    return [list(map(eval, p)) for p in puzzle_input]


def compare(p1: list | int, p2: list | int) -> int:
    """Compare two packets"""
    # (1) check if both args are integers
    if isinstance(p1, int):
        if isinstance(p2, int):
            # < 0 means correct ordering
            # 0 means undefined
            # > 0 wrong ordering
            return p1 - p2
        # (2a) 'p2' must be a list, but 'p1' is not
        p1 = [p1]

    # (2b) 'p1' must be a list; 'p2' must be as well if it's not already
    if isinstance(p2, int):
        p2 = [p2]

    # (3) recursively compare two lists
    for x, y in zip(p1, p2):
        if r := compare(x, y):
            return r

    # (4) compare lengths
    return len(p1) - len(p2)


def solve(input_data: str) -> int:
    """Solve problem for a given input"""
    data = parse(input_data)

    right_order = []

    for i, (p_1, p_2) in enumerate(data, start=1):
        if compare(p_1, p_2) < 0:
            right_order.append(i)

    return sum(right_order)


def solve_bonus(input_data: str) -> tuple:
    """Bonus: sorting the packets"""
    extra = [[[2]], [[6]]]
    data = list(chain.from_iterable(parse(input_data)))  # unroll the list
    data.extend(extra)  # add the extra packets
    data.sort(key=cmp_to_key(compare))  # sort the packets
    return tuple(data.index(p) + 1 for p in extra)  # find and return the indexes


if __name__ == "__main__":
    path = pathlib.Path(__file__).resolve()

    for input_file in (path.parents[1] / "input").glob("2_*_packets.txt"):
        input_data = input_file.read_text()
        print(f"File: {input_file.name}\n")
        print(f"  Solution: {solve(input_data)}\n")
        print(f"  Bonus: {solve_bonus(input_data)}\n")
