import random

firstwords = ["Red","Blue","East Street","Death","The"]
lastwords = ["Falcons","Lightning","Ballers","Families","Crew","Mafia","Mob"]
def name(input):
    first = random.choice(firstwords)
    last = random.choice(lastwords)
    return first + " " + last
