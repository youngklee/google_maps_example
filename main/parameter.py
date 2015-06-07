class Output(object):
    def __init__(self, iotype):
        self.iotype = iotype

class Input(object):

    def __init__(self, iotype, required=True, min=None, max=None, default=None):
            self.iotype = iotype
            self.is_required = required
            self._min = min
            self._max = max
            self._default = default
            self.value = None