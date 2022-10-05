from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from starlette.responses import JSONResponse

from src.contexts.petri_nets import GetTransitionsEnabled, GetPetriNets, CreatePetriNet, RunTransitions

router = APIRouter(
    prefix='/api/petri_nets',
    tags=['petri_nets'],
    responses={404: {"Description": "Not found"}}
)


@router.get('/')
async def list_all():
    controller = GetPetriNets()
    return controller.execute()


@router.get('/{id}')
async def read_petri_net(id: str):
    if not id:
        raise HTTPException(status_code=400, detail='Petri net not found')
    return {'name': 'Petri net'}


class PetriNet(BaseModel):
    name: str
    description: str | None = None
    places: list = []
    transitions: list = []
    placesHash: dict = {}
    transitionsHash: dict = {}
    inputs: list = []
    outputs: list = []


@router.delete('/{id}')
def delete():
    pass


@router.post('/')
async def read_petri_net(petri_net: PetriNet):
    print(petri_net.dict())
    # raise  Exception("breaking before create petri net")
    creator = CreatePetriNet()
    creator.execute(petri_net.dict())
    # if not id:
    #     raise HTTPException(status_code=400, detail='Petri net not found')
    return JSONResponse(status_code=200, content={"messagge": "Petri net created"})


@router.post('/fire_transitions')
async def run_transition(transitions: list, places: list, petri_net: dict):
    # raise  Exception("breaking before create petri net")
    fire_transitions_controller = RunTransitions()
    new_marking = fire_transitions_controller.execute(petri_net, transitions, places)
    print("This a new marcation", new_marking)
    # if not id:
    #     raise HTTPException(status_code=400, detail='Petri net not found')
    return JSONResponse(status_code=200, content=new_marking)


@router.post('/get_transitions_enabled/{petri_net_id}')
async def get_transitions_enabled(petri_net_id: str, transitions: list, places: list, petri_net: dict):
    fire_transitions_controller = GetTransitionsEnabled()
    transitions_enabled = fire_transitions_controller.execute(petri_net, transitions, places)
    print("This a new transitions_enabled", transitions_enabled)
    # if not id:
    #     raise HTTPException(status_code=400, detail='Petri net not found')
    return JSONResponse(status_code=200, content=transitions_enabled)
