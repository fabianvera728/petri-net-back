from src.contexts.petri_nets import FirebasePetriNetRepository
from src.contexts.petri_nets.infrastructure.vera_petri_net_engine import VeraPetriNetEngine


class BuildPetriNetFromEventLog:

    def __init__(self):
        self.petri_net_engine = VeraPetriNetEngine()
        # self.petri_net_repository = FirebasePetriNetRepository()

    def execute(self):
        return self.petri_net_engine.from_event_log()
