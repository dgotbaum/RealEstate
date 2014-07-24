__author__ = 'dgotbaum'
import csv
from Tract import Tract
from Neighborhood import Neighborhood

Neighborhoods ={}
Boroughs = {}
def populate():
    global Neighborhoods
    global Boroughs
    with open('2020.csv', mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if ("_" in row[0] and row[1] != "NA"):
                nbrhd = row[3]
                boro = row[2]
                value = row[1]
                key = row[0]
                t =  Tract(key,value,boro,nbrhd)
                if boro not in Boroughs:
                    if nbrhd not in Neighborhoods:
                        Neighborhoods[nbrhd] = (Neighborhood(nbrhd, [t]))
                    else:
                        Neighborhoods[nbrhd].tracts.append(t)
def neighborhoodMedians():
    print("\n\n\nMEDIANS:\n")
    for key in Neighborhoods.keys():
        print(key+": " +str(Neighborhoods[key].median()))
def neighborhoodAverages():
    print("\n\n\nAVERAGES\n")
    for key in Neighborhoods.keys():
        print(key+": " +str(Neighborhoods[key].average()))


def main():
    populate()
    neighborhoodMedians()
    neighborhoodAverages()






main()