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

