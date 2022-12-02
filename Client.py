from opcua import Client

from time import sleep
# Instantiate the client  ob ject for the OPCUA
_url = "opc.tcp://192.168.132.72"
client = Client(_url)

# Connect the client 
client.connect()
# Validate the connection
print("Client connected")

while True:
    try:
        # Get the node id of the state variable
        State = client.get_node("ns=2;i=2")
        # Get the node id of the part variables
        parts = client.get_node("ns=2;i=3")
        # get the current value of those nodes
        State = State.get_value()
        parts = parts.get_value()
        print("State: ", State, "\t", "Parts: ", parts)
        sleep(1)
    except KeyboardInterrupt:
        print("\n\n\nDisconnecting Client.....\n......\n......")
        client.disconnect()


