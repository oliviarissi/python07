#!/usr/bin/env python3

from .factory import CreatureFactory
from ex0.creatures import Creature


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()


class Aquabub(Creature):

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return (f"{self.name} uses Water Gun!")


class Torragon(Creature):

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return (f"{self.name} uses Hydro Pump!")
