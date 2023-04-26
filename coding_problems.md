# Coding problems for the interview at Empa Scientific IT

## (1) S-expression Parser

### Introduction: S-expressions

_S-Expressions_ are a human-readable notation for nested lists, famously used to represent LISP programs.

A S-expression is composed of these two entities:

- An _atom_ like `1` or `+` which represents a single symbol in an expression
- A _cons cell_ like `(1 2)` that represents a list containing the _atoms_ `1` and `2`

Cons-cells can be arbitrarily nested to form more complex expressions. For example, these forms are valid S-Expressions

```scheme
(1 (2 3))
(+ 1 (- 1 2))
```

### S-expression calculator

Consider a subset of S-expressions (_calculator expressions_) used to represent a simple calculator. Therefore, we define:

- A valid _atom_ is either any of these symbols `+`,`-`,`/`,`*` (_operator_) or an integer number (_integer_)
- A valid _cons cell_ is:
  - An _operator_ followed by two _arguments_ and therefore has the form `(operator argument argument)`
- An valid _argument_ is either:
  - An _integer_
  - A valid _cons cell_

Using these definitions, we can represent arbitrarily nested calculations. Some **valid** examples are:

```scheme
(+ 1 3)
(* 4 5)
(+ (- 3 4) 3)
(- (* 3 4) (+ 3 4))
```

While these examples are **invalid**:

```scheme
(a)
(2
(()3))
(+ 3)
```

A calculator expression can be evaluated by computing the value of sub-expressions and replacing these values in the larger expression, until all expressions are replaced.

Examples:

```
(+ 1 3) = 4
(* 4 5) = 20
(+ (- 3 4) 3) = (+ -1 3) = 2
```

### Questions

- Write a program to validate _calculator expressions_. The program receives an expression as a string and returns a boolean indicating whether the expression is valid or not
- **Bonus**: Write a program that takes a calculator expression and computes its value. If the expression is not valid, the program should return the string expression itself

## (2) Packet analysis

You need to process a list data packets. The packets are always sent **in pairs**. For example:

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

- If **both values are integers**, the lower integer should come first
  - If the left integer is lower than the right, they are in the correct order
  - If the left is higher than the right, the order is wrong
  - Otherwise, they must be the same, so you should continue checking the next pair
- If **both values are lists**, then compare element-by-element
  - If the left list runs out of items first, the inputs are in the right order
  - If the right list runs out of items first, the inputs are not in the right order
  - If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
- If **exactly one value is an integer**, then convert it to a list with a single element and retry the comparison (following rule #2)
  - Example: to compare `[0,0,0]` and `2`. First, convert 2 to `[2]`, then compare `[0,0,0]` and `[2]`. These pairs are not in the correct order, because the right-hand list runs out of items at the second comparison attempt.

Your task is to identify how many packets are in the right order.

### Questions

Find the indexes of the packets that are in correct order. What’s the sum of those indexes?

#### Hints

In the above example, packets 1, 2, 4, and 6 are in the correct order. Their sum is 13.

## (3) N-body simulation

Suppose you wanted to simulate, in an approximate manner, the time-evolution of four orbiting bodies. Let's say, for example, the four largest moons of Jupiter: Io, Europa, Ganymede, and Callisto.

Start from the initial positions of each moon in **3-dimensional space** and set their **initial velocities to zero**. You can then simulate the motion of the moons over time by updating their velocities at each time step based on the gravity interaction with the other moons, and then updating their positions by applying their velocities.

For example, consider the following starting configuration:

```
Ganymede: x=-1, y=0, z=2
Io: x=2, y=-10, z=-7
Europa: x=4, y=-8, z=8
Callisto: x=3, y=5, z=-1
```

To perform the simulation, start by considering every pair of moons. On each axis, the velocity changes by **exactly** `+1` or `-1`. The sign of the velocity change is determined by comparing the positions of the two moons on that axis.

For example, if Ganymede's x position (`G_x`) is 5 and Callisto's x position (`C_x`) is 3, then Ganymede's `x` velocity changes by `+1` (because `G_x > C_x`), and Callisto's `x` velocity must change by `-1` (because `C_x < G_x`).

If the positions of the two moons on a given axis are the same, then the velocity on that axis doesn't change at all. For instance, if Europa and Ganymede have the same `y` position, then the `y` component of their velocities remains **unchanged**.

Once the gravity has been calculated and the velocity updated, you should also update the position of each moon by adding its velocity to its current position. For example, if Europa's position is `x=1, y=2, z=3` and its velocity is `x=-2, y=0, z=3`, then its new position would be `x=-1, y=2, z=6`.

You now need to compute the **total energy of the system**: the **product** of the kinetic energy and the potential energy.

- The **kinetic energy** of a single moon is defined as the sum of the absolute values of its velocity components. For example, if a moon has a velocity of `vx=3, vy=-2, vz=1`, its kinetic energy would be `|3| + |-2| + |1| = 6`.
- The **potential energy** of a single moon is defined as the sum of the absolute values of its positional coordinates. For example, if a moon is located at `x=-1, y=0, z=2`, its potential energy would be `|-1| + |0| + |2| = 3`.

For example, if we start from the configuration above and run the simulation for **10 time steps**, the new configuration will be

```
Ganymede: x= 2, y= 1, z=-3, vx=-3, vy=-2, vz=1
Io: x= 1, y=-8, z= 0, vx=-1, vy= 1, vz=3
Europa: x= 3, y=-6, z= 1, vx= 3, vy= 2, vz=-3
Callisto: x= 2, y= 0, z= 4, vx= 1, vy=-1, vz=-1
```

And the potential and kinetic energies of the four moons will be

| moon     | potential energy | kinetic         | total         |
| -------- | ---------------- | --------------- | ------------- |
| Ganymede | `2 + 1 + 3 = 6`  | `3 + 2 + 1 = 6` | `6 * 6 = 36`  |
| Io       | `1 + 8 + 0 = 9`  | `1 + 1 + 3 = 5` | `9 * 5 = 45`  |
| Europa   | `3 + 6 + 1 = 10` | `3 + 2 + 3 = 8` | `10 * 8 = 80` |
| Callisto | `2 + 0 + 4 = 6`  | `1 + 1 + 1 = 3` | `6 * 3 = 18`  |

Thus, the total energy `36 + 45 + 80 + 18 = 179`

### Questions

- Calculate the total energy of the systems given in your input files after simulating the evolution for **1000 time steps**
- **Bonus:** Determine the number of steps that must occur before all of the moons' positions and velocities exactly match a previous point in time

#### Hints

A note about the **Bonus** question. If we consider the example configuration, it requires `2772` steps before **all** the moons match their intial state. With "match" we mean that both positions and velocities are the same.

If we start from an alternative initial state

```
Ganymede: x=-8, y=-10, z=0
Io: x=5, y=5, z=10
Europa: x=2, y=-7, z=3
Callisto: x=9, y=-8, z=-3
```

Then this set of initial coordinates takes `4686774924` steps before it repeats!

Of course, the system is **periodic**, so once you found that the period is `N`, you are guaranteed that, after any multiple of those `N` steps, the system will recover its initial state.
