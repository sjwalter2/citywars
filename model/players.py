import random

class ATTR_TYPE:
    INERTIA = 'Inertia'
    HONOR = 'Honor'
    HEAT = 'Heat'
    NOTORIETY = 'Notoriety'

class Attribute:

    def __init__(self, min, max):
        self.__value = random.randint(min, max)

    def increase(self, increase):
        self.__value += increase
        return self.__value

    def decrease(self, decrease):
        self.__value -= decrease
        return self.__value

    def getValue(self):
        return self.__value

    def __repr__(self):
        return str(self.getValue())

class Member:

    def __init__(self, e, name, gang, isLeader = False):
        self.__e = e
        self.__name = name
        self.__gang = gang
        if isLeader:
            self.__attributes = self.buildLeaderAttributes()
        else:
            self.__attributes = self.buildAttributes()

    def buildAttributes(self):
        attributes = {
            ATTR_TYPE.INERTIA: Attribute(1, 3),
            ATTR_TYPE.HONOR: Attribute(90, 100),
            ATTR_TYPE.HEAT: Attribute(0, 100),
            ATTR_TYPE.NOTORIETY: Attribute(0, 20)
        }
        return attributes

    def buildLeaderAttributes(self):
        attributes = {
            ATTR_TYPE.INERTIA: Attribute(1, 3),
            ATTR_TYPE.HONOR: Attribute(90, 100),
            ATTR_TYPE.HEAT: Attribute(0, 100),
            ATTR_TYPE.NOTORIETY: Attribute(18, 30)
        }
        return attributes

    def step(self):
        if self.__attributes[ATTR_TYPE.HEAT].getValue() > 0:
            self.__attributes[ATTR_TYPE.HEAT].decrease(1)
        if random.randint(0, self.__attributes[ATTR_TYPE.HEAT].getValue()) < (self.__attributes[ATTR_TYPE.INERTIA].getValue() * 2):
            self.__attributes[ATTR_TYPE.HEAT].increase(10)
            return 1
        return 0

    def getName(self):
        return self.__name

    def getAttributes(self):
        return self.__attributes

    def getGroup(self):
        return self.__gang

    def applyBonusGangDestroyed(self):
        self.__attributes[ATTR_TYPE.NOTORIETY].increase(30)

    def kill(self, targetgang):
        target = targetgang.getMembers()[random.randint(0,len(targetgang.getMembers())-1)]
        if target.getAttributes()[ATTR_TYPE.NOTORIETY].getValue() == 0:
            chance = 100
        else:
            chance = self.__attributes[ATTR_TYPE.NOTORIETY].getValue() / (target.getAttributes()[ATTR_TYPE.NOTORIETY].getValue() * 2)
        if chance == 0:
            chance = 0.01
        if random.random() < chance:
            #TODO: Only for Generic Gangs
            self.getGroup().appeal += 1
            targetgang.dies(target)
            self.__attributes[ATTR_TYPE.NOTORIETY].increase(target.getAttributes()[ATTR_TYPE.NOTORIETY].getValue() // 3)
            self.__e.append('{}({}) of {} killed {}({}) of {}'.format(self.__name, \
                self.__attributes[ATTR_TYPE.NOTORIETY].getValue(), self.__gang.getName(), target.getName(), \
                target.getAttributes()[ATTR_TYPE.NOTORIETY].getValue(), targetgang.getName()))
            if len(targetgang.getMembers()) == 0:
                self.applyBonusGangDestroyed()
                self.__e.destroyGang(targetgang)
                return
            if target == targetgang.getLeader():
                targetgang.setLeader(targetgang.getMembers()[random.randint(0,len(targetgang.getMembers())-1)])
                self.e.append('{} is now the leader of {}!'.format(targetgang.getLeader().getName(), targetgang.getName()))
        else:
            #self.__e.append(self.name + " of " + self.getGroup().getName() + " failed to kill " + target.getName() + " of " + targetgang.getName() + "!")
            if self.__attributes[ATTR_TYPE.NOTORIETY].getValue() == 0:
                chance = 100
            else:
                chance = target.getAttributes()[ATTR_TYPE.NOTORIETY].getValue() / (self.__attributes[ATTR_TYPE.NOTORIETY].getValue() * 5)
            if chance == 0:
                chance = 0.01
            if random.random() < chance:
                self.__e.append('{} of {} was killed by {} in self-defense!'.format(self.__name, self.__gang.getName(),\
                    target.getName(), targetgang.getName()))
                target.getAttributes()[ATTR_TYPE.NOTORIETY].increase(self.__attributes[ATTR_TYPE.NOTORIETY].getValue() // 3)
                self.__gang.dies(self)
                if len(self.__gang.getMembers()) == 0:
                    target.getAttributes()[ATTR_TYPE.NOTORIETY].increase(30)
                    self.__e.destroyGang(self.__gang)

class Officer(Member):

    def __init__(self, e, name, gang, isLeader = False):
        Member.__init__(e, name, gang, isLeader)

    def buildAttributes(self):
        attributes = {
            ATTR_TYPE.INERTIA: Attribute(0, 5),
            ATTR_TYPE.HONOR: Attribute(90, 100),
            ATTR_TYPE.HEAT: Attribute(0, 100),
            ATTR_TYPE.NOTORIETY: Attribute(0, 20)
        }
        return attributes

    def buildLeaderAttributes(self):
        return self.buildAttributes()

    def step(self):
        if self.__attributes[ATTR_TYPE.HEAT].getValue() > 0:
            self.__attributes[ATTR_TYPE.HEAT].decrease(1)
        if random.randint(0, 10) == 10:
            self.__attributes[ATTR_TYPE.HEAT].increase(20)
            return 1
        return 0

    def applyBonusGangDestroyed():
        self.__attributes[ATTR_TYPE.NOTORIETY].increase(40)

class Hero(Member):

    def __init__(self, e, name, gang, isLeader = False):
        Member.__init__(e, name, gang, isLeader)

    def buildAttributes(self):
        attributes = {
            ATTR_TYPE.INERTIA: Attribute(0, 5),
            ATTR_TYPE.HONOR: Attribute(90, 100),
            ATTR_TYPE.HEAT: Attribute(0, 100),
            ATTR_TYPE.NOTORIETY: Attribute(0, 20)
        }
        return attributes

    def buildLeaderAttributes(self):
        return self.buildAttributes()

    def step(self):
        if self.__attributes[ATTR_TYPE.HEAT].getValue() > 0:
            self.__attributes[ATTR_TYPE.HEAT].decrease(1)
        if random.randint(0, 10) == 10:
            self.__attributes[ATTR_TYPE.HEAT].increase(20)
            return 1
        return 0

    def applyBonusGangDestroyed():
        self.__attributes[ATTR_TYPE.NOTORIETY].increase(40)