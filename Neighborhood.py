__author__ = 'dgotbaum'
import math
class Neighborhood:
    def __init__(self, name, tracts):
        self.name = name
        self.tracts = tracts

    def average(self):
        sum = 0.0
        for t in self.tracts:
            sum+=eval(t.val)
        return sum/ len(self.tracts)

    def values(self):
        l = []
        for t in self.tracts:
            l.append(t.val)
        return l


    def median(self):
        return sorted(self.values())[len(self.values())//2 ]
