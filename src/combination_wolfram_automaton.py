import pygame
import numpy as np

class WolframCellularAutomataCombo:
    def __init__(self, rule1, rule2, mode='union', width=1200, height=400, cell_size=4):
        self.rule1 = rule1
        self.rule2 = rule2

        self.mode = mode
        self.width = width
        self.height = height

        self.cell_size = cell_size
        self.rows = self.height // self.cell_size
        self.cols = self.width // (3 * self.cell_size)  

        self.grid1 = np.zeros((self.rows, self.cols), dtype=int)
        self.grid2 = np.zeros((self.rows, self.cols), dtype=int)
        self.combined_grid = np.zeros((self.rows, self.cols), dtype=int)

        self.grid1[0, self.cols // 2] = 1
        self.grid2[0, self.cols // 2] = 1
        self.combined_grid[0, self.cols // 2] = 1
        self.current_row = 0

    def apply_rule(self, rule, left, center, right):
        pattern = 4 * left + 2 * center + right
        return (rule >> pattern) & 1

    def update(self):
        if self.current_row < self.rows - 1:
            for i in range(1, self.cols - 1):
                left1 = self.grid1[self.current_row, (i - 1) % self.cols]
                center1 = self.grid1[self.current_row, i]
                right1 = self.grid1[self.current_row, (i + 1) % self.cols]
                self.grid1[self.current_row + 1, i] = self.apply_rule(self.rule1, left1, center1, right1)
                
                left2 = self.grid2[self.current_row, (i - 1) % self.cols]
                center2 = self.grid2[self.current_row, i]
                right2 = self.grid2[self.current_row, (i + 1) % self.cols]
                self.grid2[self.current_row + 1, i] = self.apply_rule(self.rule2, left2, center2, right2)

                if self.mode == 'union':
                    self.combined_grid[self.current_row + 1, i] = max(self.grid1[self.current_row + 1, i], self.grid2[self.current_row + 1, i])
                elif self.mode == 'intersection':
                    self.combined_grid[self.current_row + 1, i] = min(self.grid1[self.current_row + 1, i], self.grid2[self.current_row + 1, i])

            self.current_row += 1

    def draw(self, screen):
        for i in range(self.cols):
            for j in range(self.rows):
                # Dibuja la primera capa (rule1)
                if self.grid1[j, i]:
                    pygame.draw.rect(screen, (255, 0, 0), (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size))
                # Dibuja la segunda capa (rule2)
                if self.grid2[j, i]:
                    pygame.draw.rect(screen, (0, 255, 0), ((i + self.cols) * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size))
                # Dibuja la tercera capa (combinada)
                if self.combined_grid[j, i]:
                    pygame.draw.rect(screen, (0, 0, 255), ((i + 2 * self.cols) * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size))
        
        # Dibuja líneas de separación entre las capas
        pygame.draw.line(screen, (255, 255, 255), (self.cols * self.cell_size - 1, 0), (self.cols * self.cell_size - 1, self.height))
        pygame.draw.line(screen, (255, 255, 255), ((2 * self.cols) * self.cell_size - 1, 0), ((2 * self.cols) * self.cell_size - 1, self.height))
        
        #Texto que indica cada regla
        font = pygame.font.Font(None, 24)
        rule1_text = font.render("Rule " + str(self.rule1), True, (255, 255, 255))
        rule2_text = font.render("Rule " + str(self.rule2), True, (255, 255, 255))
        combined_text = font.render("Combined: "+ str(self.mode), True, (255, 255, 255))
        screen.blit(rule1_text, (10, 10))
        screen.blit(rule2_text, (self.cols * self.cell_size + 10, 10))
        screen.blit(combined_text, ((2 * self.cols) * self.cell_size + 10, 10))

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
            clock.tick(60)

        pygame.quit()


# Ejemplo de como se implementaría nuestra clase:

rule1 = 238
rule2 = 90
mode = 'union'  

width, height = 1200, 400  
cell_size = 2

ca = WolframCellularAutomataCombo(rule1, rule2, mode, width, height, cell_size)
ca.run()