"""Class for handling input from sensors"""

from PIL import Image, ImageFilter, ImageEnhance
import ultrasonic
import reflectance_sensors


class Sensor:
    def get_value(self):
        return 0

    def update(self):
        return 0


class Sensob:
    """Container for the different sensor modules"""

    def __init__(self, sensors):
        """Initialiser interne varible (sensorer og verdier)"""
        self.sensors = sensors
        self.values = []

    def update(self):
        """Oppdater sensorer og lagre verdier"""
        sensor_vals = list(map(lambda s: s.update, self.sensors))
        self.values = self.process(sensor_vals)

    def get_values(self):
        """Få prosesserte verdier"""
        return self.values

    @staticmethod
    def process(values):
        """Prosesser input fra ulike sensorer"""
        raise NotImplementedError


class ReflectanceSensob(Sensob):
    """Reflectance Sensob"""
    def __init__(self):
        reflect = reflectance_sensors.ReflectanceSensors()
        super().__init__(reflect)

    def process(self, values):
        for value in values[0]:
            if value > 0.8:  # if white line
                return True
        return False


class DistanceSensob(Sensob):
    """Ultrasonic Senob"""

    def __init__(self):
        ultra = ultrasonic.Ultrasonic()
        super().__init__(ultra)

    def process(self, values):
        """Returns floating point number"""
        return values



