import json
import os

from petri_net_engine_fabianvera import PetriNetEngine as Engine, FromJsonToPetriNet, FromEventLogToPetriNet

from src.contexts.petri_nets.domain import PetriNetEngine, TransitionNotEnabledException
from src.contexts.petri_nets.infrastructure.mappers.vera_output_mapper import mapperFromInputToVeraPetriNetInput
from src.contexts.petri_nets.infrastructure.mappers.vera_output_mapper_o import mapperFromOutputToVeraPetriNetOutput


class MapperPetriNetToJson:

    def execute(self, petri_net):
        transitions_as_dict = {}
        for key, value in petri_net.transitions_as_dict.items():
            transitions_as_dict[str(key)] = {}
            transitions_as_dict[str(key)]['index'] = petri_net.transitions_as_dict[key]['index']
            transitions_as_dict[str(key)]['transition'] = petri_net.transitions_as_dict[key]['transition'].__dict__

        places_as_dict = {}
        for key, value in petri_net.transitions_as_dict.items():
            places_as_dict[key] = petri_net.places_as_dict[key].__dict__

        return {
            "name": petri_net.name,
            "description": "",
            "places": [{'id': x.place_id, 'name': x.name, 'tokens': x.tokens} for x in petri_net.places],
            "transitions": [{'id': x.transition_id, 'name': x.name} for x in petri_net.transitions],
            "inputs": [x for x in petri_net.entries],
            "outputs": [x for x in petri_net.outputs],
            "transitions_as_dict": transitions_as_dict,
            "places_as_dict": places_as_dict
        }


class VeraPetriNetEngine(PetriNetEngine):

    def from_event_log(self):
        path_tests_directory = os.path.dirname(os.path.abspath(__file__))
        event_log = FromEventLogToPetriNet()
        petri_nets = event_log.execute(path_tests_directory + '/config/running-example.csv')
        petri_nets_json = []
        mapper = MapperPetriNetToJson()
        for x in petri_nets:
            petri_nets_json.append(mapper.execute(x))
        return petri_nets_json

    def search_transitions_enabled(self, petri_net, transitions: list, places):
        petri_net['inputs'] = mapperFromInputToVeraPetriNetInput(petri_net['inputs']).toVeraPetriNetInput()
        petri_net['outputs'] = mapperFromOutputToVeraPetriNetOutput(petri_net['outputs']).toVeraOutputPetriNetOutput()
        petri = FromJsonToPetriNet().execute(petri_net)
        enabled_transitions = []
        petri_net_engine = Engine(petri)
        for transition in transitions:
            if petri_net_engine.is_enabled_transition(transition['id']):
                enabled_transitions.append(transition)
        return enabled_transitions

    def fire_transitions(self, petri_net, transitions, places):
        petri_net['inputs'] = mapperFromInputToVeraPetriNetInput(petri_net['inputs']).toVeraPetriNetInput()
        petri_net['outputs'] = mapperFromOutputToVeraPetriNetOutput(petri_net['outputs']).toVeraOutputPetriNetOutput()
        petri = FromJsonToPetriNet().execute(petri_net)
        petri_net_engine = Engine(petri)
        if not petri_net_engine.is_enabled_transition(*transitions):
            raise TransitionNotEnabledException('Transition not enabled')
        petri_net_engine.fire_transitions(*transitions)
        markings = petri_net_engine.petri_net.get_markings()
        index = 0
        while index < len(places):
            places[index]['tokens'] = int(markings[index])
            index += 1
        return places
