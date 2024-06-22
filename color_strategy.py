from abc import ABC, abstractmethod


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (24, 25, 26)

class ColorStrategy(ABC):
    @abstractmethod
    def get_color(self, cell_state):
        pass

class StandardColorStrategy(ColorStrategy):
    def get_color(self, cell_state):
        return WHITE if cell_state == 1 else BLACK