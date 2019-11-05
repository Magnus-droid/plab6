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
            self.motor.forward(0.5)
        elif self.value[0] == "Backoff":   # Change
            self.motor.set_value((-1, -1), dur=0.5)
        elif self.value[0] == "Turn":
            print("Halla! Vi er i turn")
            self.motor.forward(.2,3)
            self.motor.backward(.2,3)
            self.motor.right(.5,3)
            self.motor.left(.5,3)
            self.motor.backward(.3,2.5)
            self.motor.set_value([.5,.1],1)
            self.motor.set_value([-.5,-.1],1)

        else:
            self.motor.stop()


instructions = {"R60": (1, 0.25), "R30": (1, 0.5), "L60": (0.25, 1), "L30": (0.5, 1), "Backoff": (-1, -1)}


