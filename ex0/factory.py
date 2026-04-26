#!/usr/bin/env python3

from ex0.creatures import Creature
from abc import ABC, abstractmethod


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass
