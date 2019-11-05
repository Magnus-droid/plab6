"""Motob"""
import random


class Motob:
    """Acts as interface between BBCON and motors """

    def __init__(self, motor):
        """Set the motor and the instructions for it"""
        self.motor = motor
        self.value = None
        self.instructions = {"R60": (0.4, -0.4), "R30": (0.3, -0.3), "L60": (-0.4, 0.4),
                             "L30": (-0.3, 0.3), "Backoff": (-0.5, -0.5),
                             "Forward": (0.5, 0.5), "Turn": random.choice([(1, -1), (-1, 1)])}

    def update(self, recommendation):
        """Update the information for recommended action"""
        self.value = recommendation
        self.operationsalize()

    def operationsalize(self):
        """Gives motor the recommended value of choice"""
        #print("Tuple sent to motob: ", self.value)

        """
        if self.value[0] == "R60":
            self.motor.set_value((0.4, -0.4))
        elif self.value[0] == "R30":
            self.motor.set_value((0.2, -0.2))
        elif self.value[0] == "L60":
            self.motor.set_value((-0.4, 0.4))
        elif self.value[0] == "L30":
            self.motor.set_value((-0.2, 0.2))
        elif self.value[0] == "Forward":
            self.motor.forward(.3)
        elif self.value[0] == "Backoff":   # Change
            self.motor.backward(.3)
        elif self.value[0] == "Turn":
            self.motor.set_value((0.5, -0.5))
        else:
            self.motor.stop()
        """
        self.motor.set_value(self.instructions[self.value[0]])
