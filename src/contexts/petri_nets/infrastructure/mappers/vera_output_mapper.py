class mapperFromInputToVeraPetriNetInput:
    def __init__(self, inputs):
        self.inputs = inputs

    def toVeraPetriNetInput(self):
        return [
            {
                "place_id": x['place'],
                "transition_id": x['transition'],
                'number': x['number_of_inputs']
            } for x in self.inputs
        ]
