import random
class group(object):
        def __init__(self, e):
            self.e = e
        
        def getName(self):
            return self.name

        def getMembers(self):
            return self.members

        def getLeader(self):
            return self.leader

        def dies(self,victim):
            self.members.remove(victim)
            if victim == self.leader:
                self.leader = self.members[random.randint(0,len(self.members)-1)]
                self.e.append(self.leader.getName() + " is now the leader of " + self.name + "!")
