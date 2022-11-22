def getStateRef(stateID):
    states = "Off Idle Working Error Test".split(" ")
    if(stateID > 0 and stateID < len(states)+1):
        return states[stateID-1]
    # in the case of an error:
    print("ID not recognised\n")
    return None