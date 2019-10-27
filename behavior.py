"""Behavior"""
#import bbcon


class Behavior:
    """Behavior class"""

    def __init__(self, priority, name):
        """Sets all attributes of a behaviour"""
        #self.bbcon = bbcon.Bbcon()
        self.senobs = []
        self.motor_recommendation = ''
        self.active_flag = False
        self.halt_request = False
        self.priority = priority
        self.match_degree = 0
        self.weight = 0
        self.name = name

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
        print("Update active_flag")
        self.active_flag = True
        self.sense_and_act()
        self.weight = self.priority * self.match_degree

    def sense_and_act(self):
        #Gather information from used senobs and Bbcon
        #and determine a recommendation
        print("Gathering information form senobs and computing recommendation (Here: (1, 1))")
        recommendation = (1, 1)
        self.motor_recommendation = recommendation
        print("Compute match degree (set to 1 here)")
        self.match_degree = 1
        if self.check_halt():
            self.halt_request = True

    def check_halt(self):
        #Check if run should halt (time limit, reached goal)
        print("Check if behaviour should halt (here: False)\n")
        return False

    def get_name(self):
        return self.name


