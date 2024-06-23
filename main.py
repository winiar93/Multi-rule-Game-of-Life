import pygame
import numpy as np
import sys
from color_strategy import StandardColorStrategy, GRAY, BLACK
from strategy_rules import rule_mapping
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()


def draw_grid(grid, color_strategy):
    for y in range(GRID_SIZE[1]):
        for x in range(GRID_SIZE[0]):
            color = color_strategy.get_color(grid[y, x])
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw grid lines
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def update_grid(grid, rule_strategy):
    new_grid = grid.copy()
    for y in range(GRID_SIZE[1]):
        for x in range(GRID_SIZE[0]):
            new_grid[y, x] = rule_strategy.apply(cells=grid, row=y, col=x)
    return new_grid


def main(rule_name):
    grid = np.zeros(GRID_SIZE, dtype=int)

    rule_factory = rule_mapping.get(rule_name, 'standard')

    rule = rule_factory()
    rule_strategy = rule.create_rule()
    color_strategy = StandardColorStrategy()

    running = True
    toggle = False
    while running:
        screen.fill(BLACK)
        draw_grid(grid, color_strategy)
        pygame.display.flip()

        new_grid = grid.copy()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    x, y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
                    new_grid[y, x] = 1

                elif pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    x, y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
                    new_grid[y, x] = 0

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    toggle = not toggle
                elif event.key == pygame.K_RETURN:
                    new_grid = np.random.choice([0, 1], GRID_SIZE[0] * GRID_SIZE[1], p=[0.9, 0.1]).reshape(GRID_SIZE)

        if toggle:
            new_grid = update_grid(new_grid, rule_strategy)

        grid = new_grid
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    rule_name = sys.argv[1] if len(sys.argv) > 1 else 'standard'
    main(rule_name)
