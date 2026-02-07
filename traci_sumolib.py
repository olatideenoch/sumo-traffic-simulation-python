import os  
import sys 

# Establish path to SUMO (SUMO_HOME)
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")

import sumolib

net = sumolib.net.readNet('Traci.net.xml')

speedsum = 0
edgecount = 0
avgspeed = 0

for edge in net.getEdges():
    speedsum += edge.getSpeed()
    edgecount += 1

if edgecount > 0:
    avgspeed = speedsum / edgecount
print(f"Average speed of all edges: {avgspeed} m/s")