import pathlib


def parse(puzzle_input: str) -> list:
    """Parse input"""
    puzzle_input = puzzle_input.split("\n\n")
    puzzle_input = [p.split("\n") for p in puzzle_input]
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

    for i, pair in enumerate(data, start=1):
        if compare(*pair) < 0:
            right_order.append(i)

    return sum(right_order)


if __name__ == "__main__":
    path = pathlib.Path(__file__).resolve()

    for input_file in (path.parents[1] / "input").glob("2_*_packets.txt"):
        print(f"File: {input_file.name}")
        print(f"Solution: {solve(input_file.read_text())}\n")
