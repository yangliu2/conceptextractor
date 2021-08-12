from abc import ABC, abstractclassmethod
from typing import List


class Concept(ABC):
    """ abstract class for all concepts and entities """
    @abstractclassmethod
    def __init__(self, name: str, value: List = None):
        self._name = name
        self._value = value


class MathConcept(Concept):
    """ Define mathamatical concepts """

    def __init__(self, name: str, value: List = None):
        super().__init__(name, value)
        self._name = name
        self._value = value

    def __eq__(self, other: object) -> bool:
        return self._name == other._name and self._value == other._value

    def __str__(self):
        return self._name + " has value " + str(self._value)
