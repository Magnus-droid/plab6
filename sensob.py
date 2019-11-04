"""Class for handling input from sensors"""

from PIL import Image, ImageFilter, ImageEnhance
import ultrasonic
import reflectance_sensors
import camera


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

    def get_values(self):
        """Få prosesserte verdier"""
        print(self.values)
        return self.values

    @staticmethod
    def process(values):
        """Prosesser input fra ulike sensorer"""
        raise NotImplementedError

    def reset(self):
        """Reset all sensors"""
        self.sensors.reset()


class ReflectanceSensob(Sensob):
    """Reflectance Sensob"""
    def __init__(self):
        reflect = reflectance_sensors.ReflectanceSensors()
        super().__init__([reflect])

    def process(self, values):
        print(values)
        for value in values[0]:
            if value > 0.8:  # if white line
                return True
        return False


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

    def process(self, values):
        return values

