import os 
import sys

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

import traci

# Define SUMO Configuration
Sumo_config = [
    'sumo-gui',
    '-c', 'Traci.sumocfg',
    '--step-length', '0.05',
    '--delay', '1000',
    '--lateral-resolution', '0.1'
]

# Open Connection between SUMO and Traci
traci.start(Sumo_config)

# Define variables 
vehicle_speed = 0
vehicle_position = (0.0, 0.0) # vehicle_position is a tuple (x, y)
total_speed = 0

# Define Functions
def update_speed():
    global vehicle_speed, total_speed, vehicle_position
    # Decide what to do with simulation data at each step
    if 'veh1' in traci.vehicle.getIDList():
        vehicle_speed = traci.vehicle.getSpeed('veh1')
        vehicle_position = traci.vehicle.getPosition('veh1')  # (x, y)
        total_speed = total_speed + vehicle_speed
    print(f"Vehicle speed: {vehicle_speed} m/s || Vehicle position: {vehicle_position}")

def process_vehicle_data():
    # This function can be used to process vehicle data further, such as calculating average speed, distance traveled, etc.
    if 'veh1' in traci.vehicle.getIDList():
        traci.vehicle.moveToXY('veh1', 'E0.62', '0', -10, -38, 0, keepRoute=2) # Move vehicle to a specific positions
        position = traci.vehicle.getPosition('veh1')
        angle = traci.vehicle.getAngle('veh1')
        print(f"Vehicle ID: {'veh1'} || Vehicle position: {position} || Vehicle angle: {angle}")
    
def vehicle_distance_traveled():
    if 'veh1' in traci.vehicle.getIDList():
        distance_traveled = traci.vehicle.getDistance('veh1')
        print(f"Vehicle distance traveled: {distance_traveled} m")


# Take Simulation steps until there are no more vehicles in the network
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep() # move simulation forward 1 step
    update_speed()
    # process_vehicle_data()
    vehicle_distance_traveled()
    

# Close connection between SUMO and Traci
traci.close()