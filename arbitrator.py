"""Chooses the most urgent request"""


class Arbitrator:
    """COM"""

    def choose_action(self, behaviors):
        """Chooses action with heaviest weight"""
        best_choice = behaviors[0]
        for behav in behaviors:
            if behav.halt_request:
                return "Stop", True
            if behav.weight >= best_choice.weight:
                best_choice = behav
        print("Message from behavior: ", best_choice.message)
        print("Name of behaviour: ", best_choice.name)
        return best_choice.motor_recommendation, False
