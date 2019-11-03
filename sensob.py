"""Class for handling input from sensors"""

from PIL import Image, ImageFilter, ImageEnhance

class Sensor:
    def get_value(self):
        return 0
    
    def update(self):
        return 0


class Sensob():
    """Container for the different sensor modules"""

    def __init__(self, sensors):
        """Initialiser interne varible (sensorer og verdier)"""
        self.sensors = sensors
        self.values = []
     
    def update(self):
        """Oppdater sensorer og lagre verdier"""
        sensor_vals = map(lambda s: s.update, self.sensors)
        self.values = self.process(sensor_vals)
    
    def get_values(self):
        """Få prosesserte verdier"""
        return self.values
    
    @staticmethod
    def process(values):
        """Prosesser input fra ulike sensorer"""
        raise NotImplementedError
        return 0

class distanceSensob(Sensob):
    def process(values):
        return values

class ReflectanceSebsob(Sebsob):
    def process(values):
        return values
