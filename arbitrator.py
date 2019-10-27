

class Arbitrator:
    """COM"""
    def __init__(self, behaviors):
        self.behaviors = behaviors
        self.halt = False

    def choose_action(self):
        best_choice = self.behaviors[0]
        for behavior in self.behaviors[1:]:
            if behavior.weight > best_choice.weight:
                best_choice = behavior

            elif behavior.weight == best_choice.weight:
                best_choice = behavior

            return best_choice
        else:
            return None, True

"hmmmm"