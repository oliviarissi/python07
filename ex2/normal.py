#!/usr/bin/env python3

from ex0.creatures import Creature
from .strategy import BattleStrategy


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())
