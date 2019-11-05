"""Motob"""
import motors
import arbitrator


class Motob:
    """Acts as interface between BBCON and motors """

    def __init__(self):
        self.motor = motors.Motors()
        self.value = None

    def update(self, recommendation):
        self.value = recommendation
        self.operationsalize()

    def operationsalize(self):
        if self.value[0] == "R60":
            self.motor.set_value((1, 0.25))
        elif self.value[0] == "R30":
            self.motor.set_value((1, 0.5))
        elif self.value[0] == "L60":
            self.motor.set_value((0.25, 1))
        elif self.value[0] == "L30":
            self.motor.set_value((0.5, 1))
        elif self.value[0] == "Forward":
            self.motor.forward(0.5)
        elif self.value[0] == "Backoff":   # Change
            self.motor.set_value((-1, -1), 0.5)
        elif self.value[0] == "Turn":
            self.motor.set_value((1, -1), 0.5)
        else:
            self.motor.stop()




