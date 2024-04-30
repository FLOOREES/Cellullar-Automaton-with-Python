from Incendi_forestal import Incendi_Forestal
from constants import CELL_SIZE
import numpy as np

def leer_doc(filename):
    with open(filename, 'r') as file:         
        linea1 = file.readline().split()
        linea2 = file.readline().split()

        width = int(linea2[2])
        height = int(linea1[2])
    
    return width,height

def leer_capa(filename, rows, cols):
    matrix = np.zeros((rows, cols), dtype=int)
    with open(filename, 'r') as file:
        for i in range(rows):
            for j in range(cols):
                value = int(file.readline().strip())
                matrix[i, j] = value
    return matrix


#Initialization
width,height = leer_doc('assets/Vegetacion.doc')
fire_state = leer_capa('assets/Fuego.img',height,width)
humidity = leer_capa('assets/Humedad.img',height,width)
vegetation = leer_capa('assets/Vegetacion.img',height,width)

sim = Incendi_Forestal(width,height, CELL_SIZE, fire_state, vegetation, humidity)
sim.run_simulation()
