#!/usr/bin/env python3

from .factory import CreatureFactory
from ex0.creatures import Creature


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class Flameling(Creature):

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return (f"{self.name} uses Ember!")


class Pyrodon(Creature):

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return (f"{self.name} uses Flamethrower!")
