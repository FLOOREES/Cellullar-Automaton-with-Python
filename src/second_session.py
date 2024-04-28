import numpy as np

# Constants for fire states
PENDENT_CREMAR = 0
EN_PROCÉS_CREMAR = 1
CREMAT = 2

# Example data sizes (assuming data has been loaded with these dimensions)
height = 100
width = 100

# Assuming these arrays are filled with your loaded data
humitat = np.random.randint(0, 5, (height, width))  # Example initialization
vegetació = np.random.randint(1, 10, (height, width))  # Example initialization
foc = np.full((height, width), PENDENT_CREMAR)  # Start with all cells pending to burn
foc[50, 50] = EN_PROCÉS_CREMAR  # Example starting point for the fire

def actualitzar_estats(humitat, vegetació, foc):
    nova_humitat = humitat.copy()
    nova_vegetació = vegetació.copy()
    nou_foc = foc.copy()
    
    for i in range(1, height-1):
        for j in range(1, width-1):
            if foc[i, j] == EN_PROCÉS_CREMAR:
                if vegetació[i, j] > 0:
                    nova_vegetació[i, j] -= 1
                if vegetació[i, j] <= 1:
                    nou_foc[i, j] = CREMAT
            elif foc[i, j] == PENDENT_CREMAR:
                # Check all neighbors
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if foc[i + di, j + dj] == EN_PROCÉS_CREMAR:
                            if humitat[i, j] > 0:
                                nova_humitat[i, j] -= 1
                            if humitat[i, j] <= 1:
                                nou_foc[i, j] = EN_PROCÉS_CREMAR
                            
    return nova_humitat, nova_vegetació, nou_foc

import matplotlib.pyplot as plt

def visualitzar(foc):
    plt.imshow(foc, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.show()

# Simulació
passos = 50  # Nombre de passos de temps que volem simular
for pas in range(passos):
    if pas % 10 == 0:  # Visualitzar cada 10 passos
        visualitzar(foc)
    humitat, vegetació, foc = actualitzar_estats(humitat, vegetació, foc)