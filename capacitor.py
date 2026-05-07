#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_transform(factory) -> None:
    print(factory.describe())
    print(factory.attack())
    print(factory.transform())
    print(factory.attack())
    print(factory.revert())


def test_healing(factory) -> None:

    print(factory.describe())
    print(factory.attack())
    print(factory.heal())


def main() -> None:

    healing = HealingCreatureFactory()
    transforming = TransformCreatureFactory()

    print("Testing Creature with healing capability")

    print(" base:")
    test_healing(healing.create_base())

    print(" evolved:")
    test_healing(healing.create_evolved())

    print("\nTesting Creature with transform capability")

    print(" base:")
    test_transform(transforming.create_base())

    print(" evolved:")
    test_transform(transforming.create_evolved())


if __name__ == "__main__":
    main()
