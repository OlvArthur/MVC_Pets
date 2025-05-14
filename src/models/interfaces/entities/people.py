from typing import Protocol, runtime_checkable

@runtime_checkable
class PeopleInterface(Protocol):
    @property
    def id(self): pass

    @property
    def first_name(self): pass

    @property
    def last_name(self): pass

    @property
    def age(self): pass

    @property
    def pet_id(self): pass
