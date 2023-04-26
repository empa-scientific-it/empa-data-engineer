import enum
import operator
from typing import Callable


class Operators(enum.Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"


class Delimiters(enum.Enum):
    OPEN = "("
    CLOSE = ")"


def map_operator(symbol: Operators) -> Callable[[int, int], int]:
    """Maps symbol to python operator function"""
    match symbol:
        case Operators.ADD:
            return operator.add
        case Operators.SUB:
            return operator.sub
        case Operators.MUL:
            return operator.mul
        case Operators.DIV:
            return operator.floordiv
        case _:
            raise ValueError(f"Invalid operator {symbol}")


def parse_rpn(expr: str) -> int:
    """Parse RPN expression and return the accumulated value"""
    stack = []
    for symbol in expr:
        match symbol:
            case (
                Operators.ADD.value
                | Operators.SUB.value
                | Operators.MUL.value
                | Operators.DIV.value
            ) as op:
                stack.append(op)
            case _ if symbol.isnumeric():
                stack.append(int(symbol))
            case Delimiters.OPEN.value:
                pass
            case Delimiters.CLOSE.value if len(stack) > 0:
                arg2, arg1, op = [stack.pop(), stack.pop(), stack.pop()]
                stack.append(map_operator(Operators(op))(arg1, arg2))
            case " ":
                pass
    return stack.pop()


print(parse_rpn("(- (+ 2 2) (+ 2 2))"))
