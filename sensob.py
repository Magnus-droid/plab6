"""Class for handling input from sensors"""

from typing import List, TypeVar
from abc import ABC, abstractmethod
from PIL import Image, ImageFilter, ImageEnhance

class Sensor:
    def get_value(self) -> float:
        return 0
    
    def update(self) -> None:
        return 0

T = TypeVar('T')

class Sensob(ABC):
    """Container for the different sensor modules"""

    def __init__(self, sensors: List[Sensor]):
        """Initialiser interne varible (sensorer og verdier)"""
        self.sensors = sensors
        self.values = [] # type: List[float]
     
    def update(self):
        """Oppdater sensorer og lagre verdier"""
        sensor_vals = map(lambda s: s.update, self.sensors) # type: List[T]
        self.values = self.process(sensor_vals)
    
    def get_values(self):
        """Få prosesserte verdier"""
        return self.values
    
    @abstractmethod
    @staticmethod
    def process(values: List[T]) -> float:
        """Prosesser input fra ulike sensorer"""
        raise NotImplementedError
        return 0

class FindRed(Sensob):
    """Filtrer ut alt som ikke er rødt fra et bilde"""

    @staticmethod
    def process(valies: List[Image]) -> float:
        """Prosesser bildet og filtrer ut alt som ikke er hvitt"""
        return 0
