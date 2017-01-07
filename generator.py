def wordlist(filename):
    with open(filename) as f:
        i = 0
        returnwords = {}
        for word in f.readlines():
            returnwords[i] = word.rstrip()
            i += 1
        return returnwords
