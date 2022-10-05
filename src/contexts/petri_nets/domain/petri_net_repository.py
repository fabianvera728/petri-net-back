from abc import ABC, abstractmethod
from .petri_net_id import PetriNetId

class PetriNetRepository(ABC):

    @abstractmethod
    def create(self, petri_net):
        raise Exception("Not implemented")

    @abstractmethod
    def list(self):
        raise Exception("Not implemented")

    @abstractmethod
    def find_by_id(self):
        raise Exception("Not implemented")
