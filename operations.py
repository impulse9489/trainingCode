
class Turn(object):
    def __init__(self, turn=0):
        self.turn = turn

    def finish(self):
        self.turn += 1
