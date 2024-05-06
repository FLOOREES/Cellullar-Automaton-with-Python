PENDENT_CREMAR = 0
EN_PROCÉS_CREMAR = 1
CREMAT = 2
red_palette = [
    (200, 60, 0),      
    (255, 60, 0),     
    (255, 100, 0),   
    (255, 160, 0),   
    (255, 140, 0)   
]
BIOMAS = {
    'desierto': {'propagacion': 1, 'vegetacion': (25,50), 'humedad': (1,10), 'color': (250, 255, 140)},
    'vegetacion': {'propagacion': 2, 'vegetacion': (75,100), 'humedad': (20,30), 'color': (150, 255, 0)},
    'selva': {'propagacion': 3, 'vegetacion': (125,150), 'humedad': (40,50), 'color': (20, 162, 0)},
}
probabilidades = [0.1,0.6,0.3]

WIDTH, HEIGHT = 160,100
CELL_SIZE =5
NUM_FIRE_STARTS = 2
MAX_HUMIDITY = 160
LAKE_CENTERS=13