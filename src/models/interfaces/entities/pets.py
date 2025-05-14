from typing import Protocol, runtime_checkable

@runtime_checkable
class PetsInterface(Protocol):
    @property
    def id(self): pass

    @property
    def name(self): pass

    @property
    def type(self): pass
