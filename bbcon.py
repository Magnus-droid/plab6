"""?"""
import sensob
import motob
from arbitrator import Arbitrator
from time import sleep
import behavior


class Bbcon:
    """INIT"""
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.halt = False

    def add_behavior(self, bhv):
        """Legger til oppførsel til behaviors"""
        self.behaviors.append(bhv)

    def add_sensob(self, sensob):
        """Legger til sensor observatør til"""
        self.sensobs.append(sensob)

    def activate_behavior(self, bhv):
        """Activate a behavior of choice"""
        if bhv in self.behaviors and bhv not in self.active_behaviors:
            self.active_behaviors.append(bhv)

    def deactive_behavior(self, bhv):
        """Deactivate a behavior of choice"""
        if bhv in self.active_behaviors:
            self.active_behaviors.remove(bhv)

    def run_one_timestep(self):
        """Tick. Updates the sensobs, behaviors, motobs, arbitrator and resets sensobs at last"""
        arbi = Arbitrator()
        for sensob in self.sensobs:
            sensob.update()
        for behavior in self.behaviors:
            behavior.update()
        for motob in self.motobs:
            motob.update(arbi.choose_action(self.behaviors))
            sleep(0.5)
            #test


def run():
    """Starting up the robot"""
    print("Running!")
    bbcon = Bbcon()
    sensob1 = sensob.DistanceSensob()
    sensob2 = sensob.ReflectanceSensob()
    sensob3 = sensob.CameraSensob()
    behav1 = behavior.AvoidCollsion(sensob1)
    behav2 = behavior.LineDetection(sensob2)
    behav3 = behavior.DetectRed(sensob3)
    bbcon.add_sensob(sensob1)
    bbcon.add_sensob(sensob2)
    bbcon.add_sensob(sensob3)
    bbcon.add_behavior(behav1)
    bbcon.add_behavior(behav2)
    bbcon.add_behavior(behav3)
    bbcon.run_one_timestep()


run()
