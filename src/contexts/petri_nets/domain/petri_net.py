from . import PetriNetId

class PetriNetPlaces:
    pass

class PetriNetTransitions:
    pass

class PetriNetOutputs:
    pass


class PetriNetInputs:
    pass

class PetriNet:

    petri_net_id: PetriNetId
    places: PetriNetPlaces
    transitions: PetriNetTransitions
    outputs: PetriNetOutputs
    inputs: PetriNetInputs

    def __init__(
            self, petri_net_id: PetriNetId, 
            places: PetriNetPlaces, 
            transitions: PetriNetTransitions, 
            outputs: PetriNetOutputs, 
            inputs: PetriNetInputs
        ):
        self.petri_net_id = petri_net_id
        self.transitions = transitions
        self.outputs = outputs
        self.inputs = inputs
        self.places = places
