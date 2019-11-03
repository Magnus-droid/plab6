"""Behavior"""
import sensob
from math import floor


class Behavior:
    """Behavior class"""

    def __init__(self, priority, name):
        """Sets all attributes of a behaviour"""
        self.senob = None
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
        """Updates"""
        self.sense_and_act()
        self.weight = self.match_degree * self.priority

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
        super().__init__(0.6, "AvoidCollision")
        super().senob = distancesensob

    def sense_and_act(self):
        """Caluclate match degree_based, motor requests (and halt requests) on distance"""
        distance = self.senob.get_values()[0]
        if distance >= 50:                  # Decide later
            self.motor_recommendation = "Same"
            self.match_degree = 0
        elif 1 <= distance < 50:
            self.motor_recommendation = "Same"
            self.match_degree = 1-(distance/50)
        else:
            self.motor_recommendation = "Halt"
            self.match_degree = 1


class LineDetection(Behavior):
    """Detects white lines"""

    def __init__(self):
        refelectsensob = sensob.ReflectanceSensob()
        super().__init__(1, "LineDetection")
        super().senob = refelectsensob

    def sense_and_act(self):
        """Don't drive across white lines"""
        white = self.senob.get_values()[0]
        if white:
            self.motor_recommendation = "Halt"
            self.match_degree = 1
        else:
            self.motor_recommendation = "Same"
            self.match_degree = 0

class DetectRed(Behavior):
    """Detects red objects"""

    def __init__(self):
        camsensob = sensob.CameraSensob()
        super().__init__(0.75, "DetectRed")
        super().senob = camsensob

    def sense_and_act(self):
        """Look for red"""
        red_array = self.senob.get_values()[0]
        intensity = red_array[1]
        if (-1 <= red_array[0] < -0.6) and intensity >= 50:
            self.motor_recommendation = "Turn left 60"
            self.match_degree = intensity/121

        elif (-0.6 <= red_array[0] <= -0.2) and intensity >= 50:
            self.motor_recommendation = "Turn left 30"
            self.match_degree = intensity/121

        elif (0.6 < red_array[0] <= 1) and intensity >= 50:
            self.motor_recommendation = "Turn right 60"
            self.match_degree = intensity/121

        elif (0.2 <= red_array[0] < 0.6) and intensity >= 50:
            self.motor_recommendation = "Turn right 30"
            self.match_degree = intensity/121
        elif (-0.2 < red_array[0] < 0.2) and intensity >= 50:
            self.motor_recommendation = "Same"
            self.match_degree = intensity/121
