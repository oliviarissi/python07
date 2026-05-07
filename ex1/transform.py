#!/usr/bin/env python3

from .capabilities import TransformCapability
from ex0.creatures import Creature
from ex0.factory import CreatureFactory


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()


class Shiftling(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._transformed = True
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        self._transformed = False
        return (f"{self.name} returns to normal.")

    def attack(self) -> str:
        if self._transformed:
            return (f"{self.name} performs a boosted strike!")
        else:
            return (f"{self.name} attacks normally.")


class Morphagon(Creature, TransformCapability):

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._transformed = True
        return (f"{self.name} morphs into a dragonic battle form!")

    def revert(self) -> str:
        self._transformed = False
        return (f"{self.name} stabilizes its form.")

    def attack(self) -> str:
        if self._transformed:
            return (f"{self.name} unleashes a devastating morph strike!")
        else:
            return (f"{self.name} attacks normally.")
