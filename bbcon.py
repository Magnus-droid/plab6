import sensob
import motob
import arbitrator
from time import sleep
import behavior

class Bbcon:

    """INIT"""

    def __int__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = None
        self.halt = False

    def add_behavior(self, bhv):
        """Legger til oppførsel til behaviors"""
        self.behaviors.append(bhv)

    def add_sensob(self, sensob):
        """Legger til sensor observatør til"""
        self.sensobs.append(sensob)

    def activate_behavior(self, bhv):
        if bhv in self.behaviors and bhv not in self.active_behaviors:
            self.active_behaviors.append(bhv)

    def deactive_behavior(self, bhv):
        if bhv in self.active_behaviors:
            self.active_behaviors.remove(bhv)

    def run_one_timestep(self):
        """Tick. Updates the sensobs, behaviors, motobs, arbitrator and resets sensobs at last"""
        arbi = arbitrator.Arbitrator()
        for sensob in self.sensobs:
            sensob.update()
        for behavior in self.behaviors:
            behavior.update()
        for motob in self.motobs:
            motob.update(arbi.choose_action())
            sleep(0.5)
        for sensob in self.sensobs:
            sensob.reset()


bbcon = Bbcon()
sensob1 = sensob.DistanceSensob()
sensob2 = sensob.ReflectanceSensob()
sensob3 = sensob.CameraSensob()
behav1 = behavior.AvoidCollsion()
behav2 = behavior.LineDetection()
behav3 = behavior.DetectRed()
bbcon.add_sensob(sensob1)
bbcon.add_sensob(sensob2)
bbcon.add_sensob(sensob3)
bbcon.add_behavior(behav1)
bbcon.add_behavior(behav2)
bbcon.add_behavior(behav3)
