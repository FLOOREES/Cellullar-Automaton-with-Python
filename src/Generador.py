from constants import PENDENT_CREMAR, EN_PROCÉS_CREMAR, WIDTH, HEIGHT, NUM_FIRE_STARTS,LAKE_CENTERS,MAX_HUMIDITY
import numpy as np
import scipy.ndimage as ndimage


def generate_humidity(width, height, lake_centers=10,max_humidity=100):

    #funcion que dibuja un circulo
    def draw_circle(matrix, x, y, radius, value):
        for i in range(max(0, y-radius), min(matrix.shape[0], y+radius+1)):
            for j in range(max(0, x-radius), min(matrix.shape[1], x+radius+1)):
                if (i-y)**2 + (j-x)**2 <= radius**2:
                    matrix[i, j] = value

    # Crear una matriz inicial con baja humedad
    humidity = np.random.randint(5, 20, (height, width))
    
    # Seleccionar puntos aleatorios para ser centros de lagos
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

    return 'Humidity Generated'

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

def generate_vegetacion(width, height):
    vegetation = np.random.randint(10, 100, (width, height))

    with open('assets/Vegetacion.img', 'w') as file:
        for row in vegetation:
            for value in row:
                file.write(f"{value}\n")

    with open('assets/Vegetacion.doc','w') as file:
        file.write(f"rows        : {HEIGHT}\n")
        file.write(f"Columns     : {WIDTH}\n")

    return 'Vegetation Generated'


#crear archivos
generate_fire(WIDTH, HEIGHT, NUM_FIRE_STARTS)
generate_humidity(WIDTH, HEIGHT,LAKE_CENTERS,MAX_HUMIDITY)
generate_vegetacion(WIDTH, HEIGHT)