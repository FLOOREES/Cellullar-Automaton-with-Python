# Cellullar-Automaton-with-Python

# Simulación de Incendios Forestales

Este proyecto es una simulación interactiva que modela la propagación de incendios forestales en diferentes entornos y condiciones ambientales. Utiliza un enfoque basado en autómatas celulares para simular dinámicamente cómo el fuego se propaga en función de la vegetación, la humedad y los tipos de bioma.

## Características

- **Visualización Dinámica**: Observa en tiempo real cómo el fuego se expande o es contenido, dependiendo de las condiciones ambientales modificadas.
- **Interacción del Usuario**: Interactúa con la simulación a través de controles que permiten pausar, reanudar y ajustar la velocidad de la simulación.
- **Flexibilidad**: Experimenta con diferentes escenarios cambiando los parámetros iniciales como la densidad de la vegetación, la humedad y los puntos de inicio del fuego.

## Tecnologías Utilizadas

- Python 3.x
- Pygame para la visualización
- NumPy para el manejo de datos y cálculos

## Estructura del Proyecto

- `constants.py`: Define las constantes, parámetros y configuraciones iniciales.
- `generador.py`: Scripts para generar el estado inicial del mundo, incluyendo biomas, fuego y condiciones ambientales.
- `main.py`: El script principal que ejecuta la simulación, cargando los datos generados y utilizando la clase `Incendi_Forestal`.
- `Incendi_Forestal.py`: Clase que maneja la lógica de la simulación y la visualización.

## Configuración

Para configurar y ejecutar el proyecto en tu entorno local, sigue estos pasos:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio

2. **Instala las dependencias**:
  pip install pygame numpy
3. **Ejecuta la simulación**:
  python main.py

## Contribuciones
Las contribuciones son siempre bienvenidas. Si deseas contribuir al proyecto, puedes empezar por clonar este repositorio, hacer tus cambios y enviar un pull request. Nos esforzamos por mantener un entorno inclusivo y colaborativo. Por favor, asegúrate de seguir las directrices de contribución y conducta.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
