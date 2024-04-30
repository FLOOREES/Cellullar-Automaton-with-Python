from second_session import Incendi_Forestal
from constants import WIDTH, HEIGHT, CELL_SIZE, fire_state, vegetation, humidity

sim = Incendi_Forestal(WIDTH, HEIGHT, CELL_SIZE, fire_state, vegetation, humidity)
sim.run_simulation()