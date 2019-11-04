"""Motob"""
import motors


class Motob:
    """Acts as interface between BBCON and motors """

    def __init__(self):
        motor = motors.Motors()
        motor.setup()
        self.motor = motor
        self.value = None

    def update(self, recommendation):
        self.value = recommendation
        self.operationalize()


