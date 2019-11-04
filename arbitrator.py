"""Chooses the most urgent request"""
import bbcon


class Arbitrator:
    """COM"""

    def __init__(self):
        self.bbcon = bbcon.Bbcon()

    def choose_action(self):
        """Chooses action with heaviest weight"""
        behaviors = self.bbcon.behaviors
        best_choice = behaviors[0]
        for behav in behaviors:
            if behav.halt_request:
                return "Stop", True
            else:
                if behav.weight >= best_choice.weight:
                    best_choice = behav
        return best_choice.motor_recommendation, False
