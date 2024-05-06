from constants import PENDENT_CREMAR, EN_PROCÉS_CREMAR, WIDTH, HEIGHT, NUM_FIRE_STARTS,LAKE_CENTERS,MAX_HUMIDITY, BIOMAS, probabilidades
import numpy as np
import scipy.ndimage as ndimage


def generate_bioma(width, height): 

    section_width = width // 4
    section_height = height // 4

    bioma_layer = np.empty((height, width), dtype=object)

    for i in range(4):
        for j in range(4):
            chosen_bioma = np.random.choice(list(BIOMAS.keys()), p=probabilidades)
            for sub_i in range(i*section_height, (i+1)*section_height):
                for sub_j in range(j*section_width, (j+1)*section_width):
                    bioma_layer[sub_i, sub_j] = chosen_bioma

    with open('assets/Biomas.img', 'w') as file:
        for y in range(height):
            for x in range(width):
                file.write(f"{bioma_layer[y, x]}\n")
    
    with open('assets/Biomas.doc','w') as file:
        file.write(f"rows        : {HEIGHT}\n")
        file.write(f"Columns     : {WIDTH}\n")

    return bioma_layer

def generate_fire(width, height, num_fire_starts=2):
    fire_state = np.full((height, width), PENDENT_CREMAR)
    
    fire_starts = np.random.choice(width * height, num_fire_starts, replace=False)
    fire_y, fire_x = np.divmod(fire_starts, width)
    
    fire_state[fire_y, fire_x] = EN_PROCÉS_CREMAR

    with open('assets/Fuego.img', 'w') as file:
        for row in fire_state:
            for value in row:
                file.write(f"{value}\n")
    
    with open('assets/Fuego.doc','w') as file:
        file.write(f"rows        : {HEIGHT}\n")
        file.write(f"Columns     : {WIDTH}\n")

    return 'Fire Generated'

def generate_vegetacion_humedad(width,height,lake_centers,max_humidity, bioma_layer):

    def draw_circle(matrix, x, y, radius, value):
        for i in range(max(0, y-radius), min(matrix.shape[0], y+radius+1)):
            for j in range(max(0, x-radius), min(matrix.shape[1], x+radius+1)):
                if (i-y)**2 + (j-x)**2 <= radius**2:
                    matrix[i, j] = value

    vegetation = np.zeros((height, width), dtype=int)
    for i in range(height):
        for j in range(width):
            bioma = BIOMAS[bioma_layer[i,j]]
            vegetation[i,j] = np.random.randint(bioma['vegetacion'][0],bioma['vegetacion'][1])
    
    with open('assets/Vegetacion.img', 'w') as file:
        for row in vegetation:
            for value in row:
                file.write(f"{value}\n")

    with open('assets/Vegetacion.doc','w') as file:
        file.write(f"rows        : {HEIGHT}\n")
        file.write(f"Columns     : {WIDTH}\n")
    
    humidity = np.zeros((height, width), dtype=int)
    for i in range(height):
        for j in range(width):
            bioma = BIOMAS[bioma_layer[i,j]]
            humidity[i,j] = np.random.randint(bioma['humedad'][0],bioma['humedad'][1])
    
    for _ in range(lake_centers):
        cx, cy = np.random.randint(0, width), np.random.randint(0, height)
        radius = np.random.randint(5, 15)  
        draw_circle(humidity, cx, cy, radius, max_humidity)
    
    humidity = ndimage.gaussian_filter(humidity, sigma=3)

    with open('assets/Humedad.img', 'w') as file:
        for row in humidity:
            for value in row:
                file.write(f"{value}\n")

    with open('assets/Humedad.doc','w') as file:
        file.write(f"rows        : {HEIGHT}\n")
        file.write(f"Columns     : {WIDTH}\n")

generate_fire(WIDTH, HEIGHT, NUM_FIRE_STARTS)
bioma_layer = generate_bioma(WIDTH, HEIGHT)
generate_vegetacion_humedad(WIDTH, HEIGHT,LAKE_CENTERS,MAX_HUMIDITY,bioma_layer)
