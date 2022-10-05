from dataclasses import dataclass


@dataclass(frozen=True)
class ValueObject:
    pass


class PetriNetId(ValueObject):

    _value: str

    def __init__(self, value: str):
        self._value = value

    def value(self):
        return self._value

