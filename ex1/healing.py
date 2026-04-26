#!/usr/bin/env python3

from .capabilities import HealCapability
from ex0.creatures import Creature
from ex0.factory import CreatureFactory

class Sproutling(Creature, HealCapability):

    @abstractmethod
    def heal(self, target) -> str:
        pass
