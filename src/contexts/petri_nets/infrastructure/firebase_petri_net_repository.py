import firebase_admin

from firebase_admin import firestore
from firebase_admin import credentials
from src.contexts.petri_nets.domain.petri_net_repository import PetriNetRepository

cred = credentials.Certificate("src/contexts/petri_nets/infrastructure/config/credentials_firebase.json")
firebase_app = firebase_admin.initialize_app(credential=cred)
db = firestore.client(firebase_app)


class FirebasePetriNetRepository(PetriNetRepository):

    petri_nets = db.collection("petri_nets")

    def list(self):
        petri_nets_ref = self.petri_nets.get()
        petri_nets_json = []
        for petri_net in petri_nets_ref:
            petri_nets_json.append(petri_net.to_dict())
        return petri_nets_json

    def create(self, petri_net):
        petri_net_document = self.petri_nets.document()
        return petri_net_document.set(petri_net)

    def find_by_id(self):
        print("searching by id")
        pass
