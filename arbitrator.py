

class Arbitrator:
    """COM"""
    def __init__(self, behaviors):
        self.behaviors = behaviors
        self.halt = False

    def choose_action(self):
        best_choice = None
        for behavior in self.behaviors:
            if behavior.weight > best_choice.weight:
                best_choice = behavior

            elif behavior.weight == best_choice.weight:
                best_choice = behavior

            return best_choice, False
        else:
            return None, True
