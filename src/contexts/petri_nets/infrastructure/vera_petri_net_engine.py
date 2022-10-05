from petri_net_engine_fabianvera import PetriNet, PetriNetEngine as Engine
from petri_net_engine_fabianvera.domain.place import Place
from petri_net_engine_fabianvera.domain.transition import Transition

from src.contexts.petri_nets.domain import PetriNetEngine, TransitionNotEnabledException


class VeraPetriNetEngine(PetriNetEngine):

    def search_transitions_enabled(self, petri_net, transitions: list, places):
        petri = PetriNet()
        for place in petri_net['places']:
            petri.add_place(Place(place['id'], place['name'], place['tokens']))
        for transition in petri_net['transitions']:
            petri.add_transition(Transition(transition['id'], transition['name']))
        for entry in petri_net['inputs']:
            petri.add_input(entry['place'], entry['transition'], entry['number_of_inputs'])
        for output in petri_net['outputs']:
            petri.add_output(output['transition'], output['place'], output['number_of_outputs'])
        petri.generate_inputs_matrix()
        petri.generate_outputs_matrix()
        enabled_transitions = []
        petri_net_engine = Engine(petri)
        for transition in transitions:
            if petri_net_engine.is_enabled_transition(transition['id']):
                enabled_transitions.append(transition)
        return enabled_transitions

    def fire_transitions(self, petri_net, transitions, places):
        petri = PetriNet()
        for place in petri_net['places']:
            petri.add_place(Place(place['id'], place['name'], place['tokens']))
        for transition in petri_net['transitions']:
            petri.add_transition(Transition(transition['id'], transition['name']))
        for entry in petri_net['inputs']:
            petri.add_input(entry['place'], entry['transition'], entry['number_of_inputs'])
        for output in petri_net['outputs']:
            petri.add_output(output['transition'], output['place'], output['number_of_outputs'])
        petri.generate_inputs_matrix()
        petri.generate_outputs_matrix()
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
