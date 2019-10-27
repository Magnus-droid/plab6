

class Arbitrator:
    """COM"""
    def choose_action(self, behaviors):
        best_choice = None
        if not behaviors:
            return None, False
        for behavior in behaviors:
            if behavior.weight > best_choice.weight:
                best_choice = behavior
        return best_choice, True
