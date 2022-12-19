from abc import abstractmethod
from .petri_net_id import PetriNetId

class PetriNetEngine:

    @abstractmethod
    def fire_transitions(self, petri_net, transitions, places):
        raise Exception("Not implemented")

    @abstractmethod
    def search_transitions_enabled(self, petri_net, transitions, places):
        raise Exception("Not implemented")

    @abstractmethod
    def from_event_log(self):
        raise Exception("Not implemented")