"""Behavior"""
import Bbcon


class Behavior:
    """Behavior class"""

    def __init__(self, priority):
        """Sets all attributes of a behaviour"""
        self.bbcon = Bbcon.Bbcon()
        self.senobs = []
        self.motor_recommendations = []
        self.active_flag = False
        self.halt_request = False
        self.priority = priority
        self.match_degree = 0
        self.weight = 0

    def consider_deactivation(self):
        """Check if a behaviour should deactivate"""
        if self.active_flag:
            pass
        pass

    def consider_activation(self):
        """Checks if a behaviour should activate"""
        if not self.active_flag:
            pass
        pass

    def update(self):
        #Update self.active_flag
        self.sense_and_act()
        self.weight = self.priority * self.match_degree
        pass

    def sense_and_act(self):
        #Gather information from used senobs and Bbcon
        #and determine a recommendation
        recommendation = (0, 0)
        self.motor_recommendations.append(recommendation)



