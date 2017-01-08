import random
import member
import generator

firstwordsgang = generator.wordlist("firstwordsgang")
lastwordsgang = generator.wordlist("lastwordsgang")

def firstname():
    return firstwordsgang[random.randint(0,len(firstwordsgang)-1)]

def lastname():
    return lastwordsgang[random.randint(0,len(lastwordsgang)-1)]


def name(input):
    if(input == "gang"):
        return firstname() + " " + lastname()

class gang(object):
        def __init__(self):
            self.name = name("gang")
            self.leader = member.member()
            self.members = [self.leader]
            i = 0
            j = random.randint(0,5)
            while i < j:
                self.members.append(member.member())
                i += 1
