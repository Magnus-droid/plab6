import behavior

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


beh1 = behavior.Behavior(1, "AvoidFallingOff")
beh2 = behavior.Behavior(0.6, "RamIntoRed")
beh3 = behavior.Behavior(0.7, "AvoidCollision")
beh3.update()
beh1.update()
beh2.update()
arb = Arbitrator([beh1, beh2, beh3])
print(arb.choose_action().get_name())
