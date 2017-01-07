import random
import member

firstwords = {}
lastwords = {}

with open("firstwords") as f:
    i = 0
    for word in f.readlines():
        firstwords[i] = word.rstrip()
        i += 1
        
with open("lastwords") as f:
    i = 0
    for word in f.readlines():
        lastwords[i] = word.rstrip()
        i += 1

def firstname():
    return firstwords[random.randint(0,len(firstwords)-1)]

def lastname():
    return lastwords[random.randint(0,len(lastwords)-1)]


def name(input):
    if(input == "gang"):
        return firstname() + " " + lastname()

class gang(object):
        def __init__(self):
            self.name = name("gang")
            self.leader = member.member()

