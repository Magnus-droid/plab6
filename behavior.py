"""Behavior"""
import sensob


class Behavior:
    """Behavior class"""

    def __init__(self, priority, name):
        """Sets all attributes of a behaviour"""
        self.senobs = None
        self.motor_recommendation = ''
        self.active_flag = False
        self.halt_request = False
        self.priority = priority
        self.match_degree = 0
        self.weight = 0
        self.name = name

    def consider_deactivation(self):
        """Check if a behaviour should deactivate"""
        raise NotImplementedError

    def consider_activation(self):
        """Checks if a behaviour should activate"""
        raise NotImplementedError

    def update(self):
        """Does everything"""
        raise NotImplementedError

    def sense_and_act(self):
        """Calculate motor recommendations and halt requests"""
        raise NotImplementedError

    def get_name(self):
        """Returns name of behaviour"""
        return self.name


class AvoidCollsion(Behavior):
    """Subclass to avoid collision """

    def __init__(self):
        ultrasensob = sensob.DistanceSensob()
        super().__init__(1, "AvoidCollision")
        super().senobs = ultrasensob

    def sense_and_act(self):
        """"""
        self.senobs.update()
        distance = self.senobs.get_values()



