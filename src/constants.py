# Constants for fire states
PENDENT_CREMAR = 0
EN_PROCÉS_CREMAR = 1
CREMAT = 2
red_palette = [
    (200, 60, 0),      # Rojo oscuro - fuego casi consumido, poca vegetación
    (255, 60, 0),     # Naranja oscuro
    (255, 100, 0),    # Naranja brillante
    (255, 160, 0),   # Amarillo claro
    (255, 140, 0)    # Amarillo muy claro - fuego intenso, mucha vegetación
]
BIOMAS = {
    'desierto': {'propagacion': 1, 'vegetacion': (25,50), 'humedad': (1,10), 'color': (194, 178, 128)},
    'vegetacion': {'propagacion': 2, 'vegetacion': (75,100), 'humedad': (20,30), 'color': (34, 139, 34)},
    'bosque_frondoso': {'propagacion': 3, 'vegetacion': (125,150), 'humedad': (40,50), 'color': (0, 100, 0)},
}
probabilidades = [0.3,0.4,0.3]

#Initialization
WIDTH, HEIGHT = 160,100
CELL_SIZE =5
NUM_FIRE_STARTS = 2
MAX_HUMIDITY = 160
LAKE_CENTERS=13