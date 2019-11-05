"""Motob"""
import motors
import arbitrator


class Motob:
    """Acts as interface between BBCON and motors """

    def __init__(self, motor):
        self.motor = motor
        self.value = None

    def update(self, recommendation):
        self.value = recommendation
        self.operationsalize()

    def operationsalize(self):
        print("Tuple sent to motob: ", self.value)
        if self.value[0] == "R60":
            self.motor.set_value((1, 0.25))
        elif self.value[0] == "R30":
            self.motor.set_value((1, 0.5))
        elif self.value[0] == "L60":
            self.motor.set_value((0.25, 1))
        elif self.value[0] == "L30":
            self.motor.set_value((0.5, 1))
        elif self.value[0] == "Forward":
            self.motor.forward(.3, 0.5)
        elif self.value[0] == "Backoff":   # Change
            self.motor.backward(.3, 0.5)
        elif self.value[0] == "Turn":
            print("Halla! Vi er i turn")
            self.motor.right(.3,3)

        else:
            self.motor.stop()


instructions = {"R60": (1, 0.25), "R30": (1, 0.5), "L60": (0.25, 1), "L30": (0.5, 1), "Backoff": (-1, -1)}


