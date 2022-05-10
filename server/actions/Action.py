class Action:
    def __init__(self):
        self._name = 'Base action'
        self._descripption = 'Base class for actions'

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._descripption

    def perform(self):
        pass
