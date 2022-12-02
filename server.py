''' Creates a server for the OPC-UA interface'''

from opcua import Server
from random import randint
from StatesRef import getStateRef
import datetime
from time import sleep

# define the URL to listen from
url = "opc.tcp://192.168.137.73"

# Instantate the OPCUA server object
server = Server()

# Use the url as the server endpoint
server.set_endpoint(url)

# Define the Address namespace for the server
name = "OPC-UA DEMO SERVER"
# set the address space
addrSpace = server.register_namespace(name)

# Get a reference to the servers object nodes
serverNode = server.get_objects_node()

# Add a instace of a machine to the server
machine_1 = serverNode.add_object(addrSpace, "Machine_1")

# Add the params of the machine
# 
# State
machineState = machine_1.add_variable(addrSpace, "State", 0)
# Counter
part_Counter = machine_1.add_variable(addrSpace, "Part Counter", 0)

# Set variables as writable
machineState.set_writable()
part_Counter.set_writable()

# Start the server
server.start()

print(f"Server started @ {url}")
print(server.po)
parts = 0
while True:
    try:
        stateID = randint(1,7)
        state = getStateRef(stateID)
        parts += randint(0,3)
        time  = datetime.datetime.now()
       
        sleep(1)
        if(state is not None):
            print("StateID is: \t", stateID )
            print("State: ", state, "Part Count: ", parts, "Current time: ", time, "\n")
            machineState.set_value(state)
            part_Counter.set_value(parts)
    except KeyboardInterrupt:
        server.stop()