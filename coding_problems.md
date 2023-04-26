# Coding problems for the interview at Empa Scientific IT

## S-Expression Parser

### Introduction: S-Expressions

*S-Expressions* are an human-readable notation for nested lists, famously used to represent LISP programs.

An S-Expression consists of two entities:

- An *atom* like `1` or `+` which represents a single symbol in an expression
- A *cons cell* like `(1 2)` that represents a list containing the *atoms* `1` and `2`
  
Cons-cells can be arbitrarily nested, for example, these forms are valid S-Expressions

```scheme
(1 (2 3))
(+ 1 (- 1 2))
```

### S-Expression calculator

In this exercise, we consider a subset of S-expression (*calculator expressions*) used to represent a simple calculator. Therefore, we define:

- An valid  *atom* in is either any of these symbols `+`,`-`,`/`,`*` (*operator*) or an integer number (*integer*)
- A valid *cons cell* is:
  - An *operator* followed by two *arguments* and therefore has the form `(operator argument argument)`
- An valid *argument* is either:
  - An *integer*
  - A valid *cons cell*

Using these definitions, we can represent arbitrarily nested calculations. Some valid examples are:

```scheme
(+ 1 3)
(* 4 5)
(+ (- 3 4) 3)
(- (* 3 4) (+ 3 4))
```

while these examples are not valid s-expressions

```scheme
(a)
(2
(()3))
(+ 3)
```

The value of a calculator expression can be computed by successively computing the value of sub-expressions and replacing these values in the larger expression, until all expressions are replaced.

Examples:

```
(+ 1 3) -> 4
(* 4 5) -> 20
(+ (- 3 4) 3) -> (+ -1 3) -> 2
```

### Questions

- Write a program to validate *calculator expressions*. The program receives an expression as a string and returns a boolean indicating whether the expression is valid or not
- **Bonus**: write a program that takes a calculator expression and computes its value. If the expression is not valid, the program should stop.

## Packet analysis

You have a list of pairs of “packets”. For example:

```python
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
```

Packets consist of lists and integers. Each list starts with `[`, ends with `]`, and contains zero or more comma-separated values (either integers or other lists). Each packet is always a list and appears on its own line.

The ordering rules are the following, where “left” indicates the first value and “right” the second:

- If both values are integers, the lower integer should come first
  - If the left integer is lower than the right, they are in the correct order
  - If the left is higher than the right, the order is wrong
  - Otherwise, they must be the same, so you should continue checking the next pair
- If both values are lists, then compare element-by-element
  - If the left list runs out of items first, the inputs are in the right order
  - If the right list runs out of items first, the inputs are not in the right order
  - If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
- If exactly one value is an integer, then convert it to a list with a single element and retry the comparison (following rule #2).
  - Example: to compare `[0,0,0]` and `2`. First, convert 2 to `[2]`, then compare `[0,0,0]` and `[2]`. These pairs are not in the correct order, because the right-hand list runs out of items at the second comparison attempt.

Your tasks is  to identify how many packets are in the right order.

### Questions

Find the indexes of the packets that are in correct order. What’s the sum of those indexes?

In the above example, packets 1, 2, 4, and 6 are in the correct order. Their sum is 13.
