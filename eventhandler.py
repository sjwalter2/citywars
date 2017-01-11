EVENTS_LENGTH = 10

class eventhandler(object):
        def __init__(self):
            self.eventsqueue = []

        def step(self):
            i = 0
            while i < len(self.eventsqueue):
                print self.eventsqueue[i]
                i += 1
            if len(self.eventsqueue) > EVENTS_LENGTH:
                i = 0
                diff = len(self.eventsqueue) - EVENTS_LENGTH
                tmparray = []
                while i < EVENTS_LENGTH:
                    tmparray.append(self.eventsqueue[i + diff])
                    i += 1
                self.eventsqueue = tmparray

        def append(self, event):
            self.eventsqueue.append(event)
