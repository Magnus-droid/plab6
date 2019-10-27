"""Class for handling input from sensors"""

from typing import List, TypeVar
from abc import ABC, abstractmethod
from PIL import Image, ImageFilter, ImageEnhance

class Sensor:
    def get_value(self) -> float:
        return 0
    
    def update(self) -> None:
        pass

T = TypeVar('T')

class Sensob(ABC):
    """Container for the different sensor modules"""
    def __init__(self, sensors: List[Sensor]):
        self.sensors = sensors
        self.values = [] # type: List[float]
     
    def update(self):
        sensor_vals = map(lambda s: s.update, self.sensors) # type: List[T]
        self.values = self.process(sensor_vals)
    
    def get_values(self):
        return self.values
    
    @abstractmethod
    @staticmethod
    def process(values: List[T]) -> float:
        raise NotImplementedError
        return 0

class FindRed(Sensob):
    """Returns approximity of red object, 
    with negative numbers meaning left and 
    positive meaning right"""

    @staticmethod
    def process(valies: List[Image]) -> float:
        return 0
