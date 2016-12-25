class Clock(object):  

    def __init__(self, value_hrs, value_mins):
        self.mins = (value_mins + (value_hrs * 60)) % (60 * 24)

    def __str__(self):
        return '{:02d}:{:02d}'.format(self.hrs, self.mins)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    @property
    def mins(self):
        return self._mins % 60

    @property
    def hrs(self):
        return self._mins / 60

    @mins.setter
    def mins(self, value):
        self._mins = value

    def add(self, value):
        obj = Clock(self.hrs, self.mins + value)
        return obj