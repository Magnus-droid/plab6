"""Behavior"""
import sensob


class Behavior:
    """Behavior class"""

    def __init__(self, priority, name):
        """Sets all attributes of a behaviour"""
        self.senobs = None
        self.motor_recommendation = ''
        self.active_flag = True
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
        distancesensob = sensob.DistanceSensob()
        super().__init__(1, "AvoidCollision")
        super().senobs = distancesensob

    def sense_and_act(self):
        """Caluclate match degree_based, motor requests (and halt requests) on distance"""
        distance = self.senobs.get_values()
        if distance < 0.5:      # Decide later
            self.halt_request = True



    def update(self):
        """Update senobs, call sense_and_act in order to calc self.weight"""
        self.senobs.update()
        self.sense_and_act()
        self.weight = self.match_degree * self.priority





