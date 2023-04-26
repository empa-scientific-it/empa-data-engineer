import pathlib
from math import lcm


class Moon:
    def __init__(self, scan: str) -> None:
        name, pos = scan.split(": ")
        self.name = name
        self.positions = [int(x[2:]) for x in pos.split(", ")]
        self.velocities = [0 for _ in range(len(self.positions))]

    def update_velocities(self, moon: "Moon") -> None:
        for n, position in enumerate(self.positions):
            if position > moon.positions[n]:
                delta = 1
            elif position < moon.positions[n]:
                delta = -1
            else:
                delta = 0

            if delta:
                self.velocities[n] -= delta
                moon.velocities[n] += delta

    def update_positions(self) -> None:
        for n in range(len(self.positions)):
            self.positions[n] += self.velocities[n]

    @property
    def abs_velocity(self) -> int:
        return sum(abs(v) for v in self.velocities)

    @property
    def abs_position(self) -> int:
        return sum(abs(p) for p in self.positions)

    @property
    def energy(self) -> int:
        return self.abs_position * self.abs_velocity

    def overlaps_with(self, other: "Moon", axis: int) -> bool:
        return (
            self.positions[axis] == other.positions[axis]
            and self.velocities[axis] == other.velocities[axis]
        )

    def __repr__(self) -> str:
        return "{}: x={}, y={}, z={}, vx={}, vy={}, vz={}".format(
            self.name, *self.positions, *self.velocities
        )


class Universe:
    def __init__(self, moons: str) -> None:
        self.moons = [Moon(moon) for moon in moons.splitlines()]

    def evolve(self) -> None:
        for n, moon_i in enumerate(self.moons[:-1]):
            for moon_j in self.moons[n + 1 :]:
                moon_i.update_velocities(moon_j)

        for moon in self.moons:
            moon.update_positions()

    @property
    def energy(self) -> int:
        return sum(moon.energy for moon in self.moons)

    @property
    def momentum(self) -> list:
        return list(map(sum, zip(*[moon.velocities for moon in self.moons])))

    def __repr__(self) -> str:
        return "\n".join(repr(moon) for moon in self.moons)


def part1(universe_conf: pathlib.Path) -> str:
    """Question 1"""
    print("  Question 1:")

    universe = Universe(universe_conf.read_text())

    for _ in range(1000):
        universe.evolve()

    return f"    Total energy: {universe.energy}\n"


def part2(universe_conf: pathlib.Path) -> str:
    """Question 2"""
    print("  Question 2:")

    universe = Universe(universe_conf.read_text())
    universe_0 = Universe(universe_conf.read_text())  # initial state

    step = 0
    AXIS = range(3)
    loops = [None for _ in AXIS]

    while True:
        step += 1
        universe.evolve()
        for axis in AXIS:
            if loops[axis]:
                continue

            for n, moon in enumerate(universe.moons):
                if not moon.overlaps_with(universe_0.moons[n], axis):
                    break
            else:
                loops[axis] = step

        if all(loops):
            break

    return f"    Initial state repeated after {lcm(*loops)} steps\n"


if __name__ == "__main__":
    path = pathlib.Path(__file__).resolve()

    for file in (path.parents[1] / "input").glob("3_*_universe.txt"):
        print(f"File: {file.name}")
        print(part1(file))
        print(part2(file))
