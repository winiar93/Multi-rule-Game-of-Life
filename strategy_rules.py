from abc import ABC, abstractmethod
import numpy as np


class GameOfLifeRule(ABC):
    @abstractmethod
    def apply(self, cells, row, col):
        pass


class DayAndNightRule(GameOfLifeRule):
    def apply(self, cells, row, col):
        alive_cells = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        if cells[row, col] == 1:
            if alive_cells in {3, 4, 6, 7, 8}:
                return 1
            else:
                return 0
        else:
            if alive_cells in {3, 6, 7, 8}:
                return 1
        return 0

class StandardRule(GameOfLifeRule):
    def apply(self, cells, row, col):
        alive_cells = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        if cells[row, col] == 1:
            if alive_cells < 2 or alive_cells > 3:
                return 0
            elif 2 <= alive_cells <= 3:
                return 1
        else:
            if alive_cells == 3:
                return 1
        return 0


class RuleFactory(ABC):
    @abstractmethod
    def create_rule(self):
        pass


class StandardRuleFactory(RuleFactory):
    def create_rule(self):
        return StandardRule()


class DayAndNightRuleFactory(RuleFactory):
    def create_rule(self):
        return DayAndNightRule()


rule_mapping = {
    'standard': StandardRuleFactory,
    'dayandnight': DayAndNightRuleFactory,
}