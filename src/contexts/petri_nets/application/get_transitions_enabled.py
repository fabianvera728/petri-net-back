from src.contexts.petri_nets import FirebasePetriNetRepository
from src.contexts.petri_nets.infrastructure.vera_petri_net_engine import VeraPetriNetEngine


class GetTransitionsEnabled:

    def __init__(self):
        self.petri_net_engine = VeraPetriNetEngine()
        self.petri_net_repository = FirebasePetriNetRepository()
        pass

    def execute(self, petri_net_id, transitions: list, places: list):
        # petri_net = self.petri_net_repository.find_by_id()
        return self.petri_net_engine.search_transitions_enabled(petri_net_id, transitions, places)
