"""Class for handling input from sensors"""

from PIL import Image, ImageFilter, ImageEnhance
import ultrasonic
import reflectance_sensors
import camera
from imager3 import find_color, Imager

class Sensor:
    @staticmethod
    def get_value():
        return 0

    @staticmethod
    def update():
        return 0


class Sensob:
    """Container for the different sensor modules"""

    def __init__(self, sensors):
        """Initialiser interne varible (sensorer og verdier)"""
        self.sensors = sensors
        self.values = []

    def update(self):
        """Oppdater sensorer og lagre verdier"""
        sensor_vals = list(map(lambda s: s.update(), self.sensors))
        print("Sensob update: ", sensor_vals)
        self.values = self.process(sensor_vals)
        print("Self.values: ", self.values)

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
        super().__init__([reflect])

    def process(self, values):
        for value in values[0][0:5]:
            if value < 0.2:  # if white line
                return [True]
        return [False]


class DistanceSensob(Sensob):
    """Ultrasonic Senob"""

    def __init__(self):
        ultra = ultrasonic.Ultrasonic()
        super().__init__([ultra])

    def process(self, values):
        """Returns floating point number"""
        return values


class CameraSensob(Sensob):
    """Camera Sensob"""

    def __init__(self):
        cam = camera.Camera()
        super().__init__([cam])
        self.image=None

    def process(self, values):
        self.image=values[0]
        return find_color(values[0], 10, 20, "r")

    def save_image(self):
        Imager(image=self.image).dump_image("ISEERED.png")

