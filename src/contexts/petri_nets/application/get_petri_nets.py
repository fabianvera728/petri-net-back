from src.contexts.petri_nets import PetriNetRepository
from src.contexts.petri_nets.infrastructure import FirebasePetriNetRepository


class GetPetriNets:

    # def __init__(self, petri_net_repository: PetriNetRepository):
    def __init__(self):
        self.petri_net_repository = FirebasePetriNetRepository()

    def execute(self):
        return self.petri_net_repository.list()
