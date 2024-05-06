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
            bioma = self.bioma[i, j]
            color = BIOMAS[bioma]['color']
            vegetation = self.vegetation[i][j]
            humidity = self.humidity[i][j]
            if bioma == 'desierto':
                return (max(0, min(255, color[0] + humidity)),
                        max(0, min(255, color[1] + humidity)),
                        max(0, min(255, color[2] - (vegetation//5 + humidity))))
            elif bioma == 'vegetacion':
                return (max(0, min(255, color[0] - humidity)),
                        max(0, min(255, color[1] - vegetation)),
                        max(0, min(255, color[2] + humidity)))
            elif bioma == 'selva':
                return (max(0, min(255, color[0] - humidity // 5)),
                        max(0, min(255, color[1] - vegetation // 3)),
                        max(0, min(255, color[2] + humidity)))

    def run_simulation(self):
        clock = pygame.time.Clock()
        running = True
        paused = False
        frame_rate = 30 

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused 
                    elif event.key == pygame.K_UP:
                        frame_rate = min(60, frame_rate + 5) 
                    elif event.key == pygame.K_DOWN:
                        frame_rate = max(5, frame_rate - 5) 

            if not paused:
                self.update_world()
                self.screen.fill((0, 0, 0))
                self.draw_world(self.screen)
                pygame.display.flip()

            clock.tick(frame_rate) 

        pygame.quit()
        sys.exit()


