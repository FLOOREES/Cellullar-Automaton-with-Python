import pygame
import sys
import numpy as np

# Constants for fire states
PENDENT_CREMAR = 0
EN_PROCÉS_CREMAR = 1
CREMAT = 2

class Incendi_Forestal:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Inicialización con dimensiones y valores aleatorios para humedad y vegetación
        self.humidity = np.random.randint(20, 100, (height, width))  # Humedad del 20% al 100%
        self.vegetation = np.random.randint(10, 100, (height, width))  # Vegetación del 10% al 100%
        self.fire_state = np.full((height, width), PENDENT_CREMAR)  # Todo pendiente de quemar
        # Punto de inicio del fuego
        self.fire_state[height // 2][width // 2] = EN_PROCÉS_CREMAR

    def update_world(self):
        new_fire_state = self.fire_state.copy()
        for i in range(self.height):
            for j in range(self.width):
                if self.fire_state[i][j] == EN_PROCÉS_CREMAR:
                    # Reducir la vegetación de la célula que se está quemando
                    if self.vegetation[i][j] > 0:
                        self.vegetation[i][j] -= 1
                    # Si la vegetación llega a 0, la célula se ha quemado completamente
                    if self.vegetation[i][j] <= 0:
                        new_fire_state[i][j] = CREMAT
                    # Propagar el fuego a células vecinas, reduciendo la humedad primero
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < self.height and 0 <= nj < self.width:
                                if self.fire_state[ni][nj] == PENDENT_CREMAR:
                                    if self.humidity[ni][nj] > 0:
                                        self.humidity[ni][nj] -= 1  # Reducir la humedad
                                    if self.humidity[ni][nj] <= 0:
                                        new_fire_state[ni][nj] = EN_PROCÉS_CREMAR  # Empezar a quemarse si la humedad es 0
        self.fire_state = new_fire_state

    def draw_world(self, screen):
        # Dibuja el mundo con colores dinámicos basados en el estado de la vegetación
        for i in range(self.height):
            for j in range(self.width):
                if self.fire_state[i][j] == CREMAT:
                    color = (41,25,22)  # Marrón oscuro para las áreas quemadas
                elif self.fire_state[i][j] == EN_PROCÉS_CREMAR:
                    color = (255, 140, 0)  # Naranja para áreas que están ardiendo
                else:
                    # Vegetación no quemada: ajustar verde según el máximo inicial
                    green_intensity = int(255 * (self.vegetation[i][j] / self.vegetation.max()))
                    humidity_intensity = int(255 * (self.humidity[i][j] / self.humidity.max()))
                    color = (0, green_intensity, humidity_intensity//1.5)  # Escala de verdes según la vegetación restante
                cell_size = 10  # Aumenta esto para hacer cada celda más grande
                pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

    def run_simulation(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width * 10, self.height * 10))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.update_world()
            self.draw_world(screen)
            pygame.display.flip()
            clock.tick(30)  # Aumenta la frecuencia de actualización para que el fuego avance más rápido

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    sim = Incendi_Forestal(100, 100)  # Define las dimensiones como 100x100
    sim.run_simulation()