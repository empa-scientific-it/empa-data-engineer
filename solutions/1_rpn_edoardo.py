import pathlib
import re
from operator import add, mul, sub, truediv

ops = {"+": add, "-": sub, "*": mul, "/": truediv}


def eval_expr(expr: str) -> str:
    pattern = r"\(([+\-*/])\s(-?\d+)\s(-?\d+)\)"

    def replace_match(match: re.Match) -> str:
        op, a, b = match.groups()
        return str(ops[op](int(a), int(b)))

    while re.search(pattern, expr):
        expr = re.sub(pattern, replace_match, expr)

    return expr


def validate(expr: str) -> bool:
    try:
        return bool(int(expr))
    except ValueError:
        return False


def print_results(results: list | set, title: str) -> None:
    print(f"{title} expressions:")
    for expr, result in results:
        print(f"  {expr} = {result}")
    print("\n")


if __name__ == "__main__":
    path = pathlib.Path(__file__).resolve()
    examples = (
        (path.parents[1] / "input/1_rpn_expressions.txt").read_text().splitlines()
    )

    results = list(zip(examples, map(eval_expr, examples)))
    valid = set(filter(lambda x: validate(x[1]), results))
    invalid = set(results) - valid

    print_results(valid, "Valid")
    print_results(invalid, "Invalid")
