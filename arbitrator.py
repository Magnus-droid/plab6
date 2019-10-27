

class arbitrator:
    """COM"""
    def choose_action(self, behaviors):
        halt = False
        best_choice = None
        if not behaviors:
            return False
        for behavior in behaviors:
            if behavior.weight > best_choice.weight:
                best_choice = behavior
        return best_choice
