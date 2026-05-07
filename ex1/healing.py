#!/usr/bin/env python3

from .capabilities import HealCapability
from ex0.creatures import Creature
from ex0.factory import CreatureFactory


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class Sproutling(Creature, HealCapability):

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def heal(self) -> str:
        return (f"{self.name} heals itself for a small amount")

    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")


class Bloomelle(Creature, HealCapability):

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def heal(self) -> str:
        return (f"{self.name} heals itself and others for a large amount")

    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")
