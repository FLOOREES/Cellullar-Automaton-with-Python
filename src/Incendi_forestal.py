import numpy as np
from constants import PENDENT_CREMAR, EN_PROCÉS_CREMAR ,CREMAT, red_palette, BIOMAS
import pygame
import sys

class Incendi_Forestal:
    def __init__(self, width, height, cell_size, fire_state, vegetation, humidity,bioma):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.fire_state = fire_state
        self.vegetation = vegetation
        self.humidity = humidity
        self.bioma = bioma
        self.max_vegetation = np.max(self.vegetation)
        self.max_humidity = np.max(self.humidity)

        pygame.init()
        screen_size = (self.width * self.cell_size, self.height * self.cell_size)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Simulador de Incendio Forestal")

    def update_world(self):
        burning_cells = np.where(self.fire_state == EN_PROCÉS_CREMAR)
        for i, j in zip(*burning_cells):
            propagation_factor = BIOMAS[self.bioma[i, j]]['propagacion']
            self.vegetation[i, j] -= propagation_factor
            self.fire_state[i, j] = CREMAT if self.vegetation[i, j] <= 0 else EN_PROCÉS_CREMAR
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.height and 0 <= nj < self.width:
                        if self.fire_state[ni][nj] == PENDENT_CREMAR and self.humidity[ni][nj] > 0:
                            self.humidity[ni][nj] -= 1
                            if self.humidity[ni][nj] <= 0:
                                self.fire_state[ni][nj] = EN_PROCÉS_CREMAR

    def draw_world(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                color = self.get_color(i, j)
                pygame.draw.rect(screen, color, (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))

    def get_color(self, i, j):
        if self.fire_state[i][j] == CREMAT:
            return (41, 25, 22)
        elif self.fire_state[i][j] == EN_PROCÉS_CREMAR:
            indx_fire = int(5*(self.vegetation[i][j] / self.max_vegetation))
            if indx_fire > 4:
                indx_fire = 4
            return red_palette[indx_fire]
        else:
            green_intensity = int(255 * (self.vegetation[i][j] / self.max_vegetation))
            humidity_intensity = int(255 * (self.humidity[i][j] / self.max_humidity))
            return (0, green_intensity, humidity_intensity // 1.5)

    def run_simulation(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.update_world()
            self.screen.fill((0, 0, 0))  
            self.draw_world(self.screen)
            pygame.display.flip()
            clock.tick(100)


