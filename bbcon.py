from sensob import Sensob
from motob import Motob
import arbitrator
from time import sleep

class Bbcon:

    """INIT"""

    def __int__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.metobs = []
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
        for motob in self.metobs:
            motob.update(arbi.choose_action())
            sleep(0.5)
        for sensob in self.sensobs:
            sensob.reset()
