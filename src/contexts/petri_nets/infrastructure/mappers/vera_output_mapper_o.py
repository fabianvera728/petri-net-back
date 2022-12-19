class mapperFromOutputToVeraPetriNetOutput:
    def __init__(self, outputs):
        self.outputs = outputs

    def toVeraOutputPetriNetOutput(self):
        return [
            {
                "place_id": x['place'],
                "transition_id": x['transition'],
                'number': x['number_of_outputs']
            } for x in self.outputs
        ]
