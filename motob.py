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
        elif self.value[0] == "Same":
            self.motor.forward(0.5)
        elif self.value[0] == "Halt":   # Change
            self.halt_and_change()
        else:
            self.motor.stop()




    #def stay_same(self):
     #   if self.prev is None:
      #      self.motor.forward(1)
      #  else:
       #     self.value = self.prev
        #    self.operationsalize()

    def halt_and_change(self):
        self.motor.backward(0.5, 1)
        self.motor.set_value((1, -1), 0.25)


