"""Chooses the most urgent request"""


class Arbitrator:
    """COM"""

    def choose_action(self, behaviors):
        """Chooses action with heaviest weight"""
        best_choice = behaviors[0]
        for behav in behaviors:
            if behav.halt_request:
                return "Stop", True
            else:
                if behav.weight >= best_choice.weight:
                    best_choice = behav
        return best_choice.motor_recommendation, False
