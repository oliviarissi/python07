#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory


def test_factory(factory) -> None:

    print("Testing factory")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1, factory2) -> None:

    print("Testing battle")

    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(f"{c1.describe()}\n vs.\n{c2.describe()}\n fight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:

    flame = FlameFactory()
    aqua = AquaFactory()

    test_factory(flame)
    print()
    test_factory(aqua)
    print()

    battle(flame, aqua)


if __name__ == "__main__":
    main()
