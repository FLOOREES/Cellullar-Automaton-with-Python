import pygame
import numpy as np

class WolframCellularAutomata:
    def __init__(self, rule, width=800, height=400, cell_size=4):
        self.rule = rule
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.rows = self.height // self.cell_size
        self.cols = self.width // self.cell_size
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        self.grid[0, self.cols // 2] = 1
        self.current_row = 0

    def apply_rule(self, left, center, right):
        pattern = 4 * left + 2 * center + right
        return (self.rule >> pattern) & 1

    def update(self):
        if self.current_row < self.rows - 1:
            for i in range(1, self.cols - 1):
                left = self.grid[self.current_row, (i - 1) % self.cols]
                center = self.grid[self.current_row, i]
                right = self.grid[self.current_row, (i + 1) % self.cols]
                self.grid[self.current_row + 1, i] = self.apply_rule(left, center, right)
            self.current_row += 1

    def draw(self, screen):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.grid[j, i]:
                    pygame.draw.rect(screen, (255, 255, 255), (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size))

        font = pygame.font.Font(None, 36)
        rule_text = font.render("Rule " + str(self.rule), True, (255, 255, 255))
        screen.blit(rule_text, (10, 10))

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()

            screen.fill((0, 0, 0))
            self.draw(screen)
            pygame.display.flip()
            clock.tick(50)

        pygame.quit()


# Ejemplo de como se implementarÃ­a nuestra clase:

rule = 30
width, height = 800, 400
cell_size = 5

ca = WolframCellularAutomata(rule, width, height, cell_size)
ca.run()
