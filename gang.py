import random
import member

class gang(object):

        def __init__(self):
            self.name = name("gang")
            self.leader = member.member()


firstwords = ["Red","Blue","East Street","Death","The"]
lastwords = ["Falcons","Lightning","Ballers","Families","Crew","Mafia","Mob"]
def name(input):
    if(input == "gang"):
        first = random.choice(firstwords)
        last = random.choice(lastwords)
        return first + " " + last
