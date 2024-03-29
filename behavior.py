"""Behavior"""
import sensob


class Behavior:
    """Behavior class"""

    def __init__(self, priority, name, sensob):
        """Sets all attributes of a behaviour"""
        self.senob = sensob
        self.motor_recommendation = ''
        self.active_flag = True
        self.halt_request = False
        self.priority = priority
        self.match_degree = 0
        self.weight = 0
        self.name = name
        self.message = ""

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

    def __init__(self, sensob):
        super().__init__(0.6, "AvoidCollision", sensob)

    def sense_and_act(self):
        """Caluclate match degree_based, motor requests (and halt requests) on distance"""
        distance = self.senob.get_values()[0]
        if distance >= 50:                  # Decide later
            self.motor_recommendation = "Forward"
            self.match_degree = 0.01
        elif 10 <= distance < 50:
            self.motor_recommendation = "Forward"
            self.match_degree = 1-(distance/50)
        else:
            self.motor_recommendation = "Turn"
            self.match_degree = 1
            self.message = "TOO CLOSE"


class LineDetection(Behavior):
    """Detects white lines"""

    def __init__(self, sensob):
        super().__init__(10, "LineDetection", sensob)

    def sense_and_act(self):
        """Don't drive across white lines"""
        black = self.senob.get_values()[0]
        if black:
            self.motor_recommendation = "Backoff"
            self.match_degree = 1
            self.message = "ON A LINE"
        else:
            self.motor_recommendation = "Forward"
            self.match_degree = 0.001
            self.message = "NOT ON A LINE"


class DetectRed(Behavior):
    """Detects red objects"""

    def __init__(self, sensob):
        super().__init__(0.75, "DetectRed", sensob)

    def sense_and_act(self):
        """Look for red"""
        red_array = self.senob.get_values()
        intensity = red_array[1]
        if (-1 <= red_array[0] < -0.6) and intensity >= 85:
            self.motor_recommendation = "L60"
            self.match_degree = intensity/150
            self.senob.save_image()

        elif (-0.6 <= red_array[0] <= -0.2) and intensity >= 85:
            self.motor_recommendation = "L30"
            self.match_degree = intensity/150
            self.senob.save_image()

        elif (0.6 < red_array[0] <= 1) and intensity >= 85:
            self.motor_recommendation = "R60"
            self.match_degree = intensity/150
            self.senob.save_image()

        elif (0.2 <= red_array[0] < 0.6) and intensity >= 85:
            self.motor_recommendation = "R30"
            self.match_degree = intensity/150
            self.senob.save_image()

        elif (-0.2 < red_array[0] < 0.2) and intensity >= 85:
            self.motor_recommendation = "Forward"
            self.match_degree = intensity/150
            self.senob.save_image()
            self.message = "RED IN FRONT OF ME!!"

        else:
            self.match_degree = 0.01



