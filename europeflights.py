#This is a European Adventure program.

import itertools
from operator import itemgetter

#Set up a dictionary with costs
D = {'CA': 73, 'BA': 138, 'SA': 74, 'HA': 110, 'AC': 68, 'BC': 87, 'SC': 89, 'HC': 85, 'AB': 109, 'CB': 79, 'SB': 74, 'HB': 113, 'AS': 54, 'CS': 75, 'BS': 84, 'HS': 57, 'AH': 82, 'CH': 63, 'BH': 120, 'SH': 54
     , 'LA': 72, 'LB': 89, 'LC': 63, 'LH': 97, 'LS': 88, 'DA': 108, 'DB': 123, 'DC': 62, 'DH': 94, 'DS': 58
     , 'ABarcelona': 180, 'BBarcelona': 203, 'CBarcelona': 98, 'HBarcelona': 116, 'SBarcelona': 109}

#First find all possible combinations that visit each place once
def permgenerator():
    return list(itertools.permutations(['Amsterdam', 'Bergen', 'Copenhagen', 'Helsinki', 'Stockholm']))

#Then find the cost of each permutation
def costfinder():
    trips = permgenerator()
    costTrips = ()
    for trip in trips:
        cost = 0
        for i in range(len(trip)-1):
            cost += D[trip[i][0] + trip[i+1][0]]
        trip = trip + (cost,)
        costTrips = costTrips + (trip,)
    costTrips = sorted(costTrips, key=itemgetter(5))
    return costTrips

#Then add cost of flying from London
def getThereL():
    trips = costfinder()
    Ltrips = ()
    for trip in trips:
        if trip[0] == 'Amsterdam':
            newCost = trip[5] + D['LA']
        elif trip[0] == 'Bergen':
            newCost = trip[5] + D['LB']
        elif trip[0] == 'Copenhagen':
             newCost = trip[5] + D['LC']
        elif trip[0] == 'Stockholm':
            newCost = trip[5] + D['LS']
        elif trip[0] == 'Helsinki':
            newCost = trip[5] + D['LH']
        newTrip = trip + (newCost,)
        Ltrips = Ltrips + (newTrip,)
    Ltrips = sorted(Ltrips, key=itemgetter(6))
    return Ltrips

#Compared to cost of flying from Dublin
def getThereD():
    trips = costfinder()
    Dtrips = ()
    for trip in trips:
        if trip[0] == 'Amsterdam':
            newCost = trip[5] + D['DA']
        elif trip[0] == 'Bergen':
            newCost = trip[5] + D['DB']
        elif trip[0] == 'Copenhagen':
             newCost = trip[5] + D['DC']
        elif trip[0] == 'Stockholm':
            newCost = trip[5] + D['DS']
        elif trip[0] == 'Helsinki':
            newCost = trip[5] + D['DH']
        newTrip = trip + (newCost,)
        Dtrips = Dtrips + (newTrip,)
    Dtrips = sorted(Dtrips, key=itemgetter(6))
    return Dtrips

#Then add cost of flying to Barcelona
#From London
def LondonToBarcelona():
    Ltrips = getThereL()
    Btrips = ()
    for Ltrip in Ltrips:
        if Ltrip[4] == 'Amsterdam':
            newCost = Ltrip[6] + D['ABarcelona']
        elif Ltrip[4] == 'Bergen':
            newCost = Ltrip[6] + D['BBarcelona']
        elif Ltrip[4] == 'Copenhagen':
            newCost = Ltrip[6] + D['CBarcelona']
        elif Ltrip[4] == 'Helsinki':
            newCost = Ltrip[6] + D['HBarcelona']
        elif Ltrip[4] == 'Stockholm':
            newCost = Ltrip[6] + D['SBarcelona']
        newTrip = Ltrip + (newCost,)
        Btrips = Btrips + (newTrip,)
    Btrips = sorted(Btrips, key=itemgetter(7))
    return Btrips

#From Dublin
def DublinToBarcelona():
    Dtrips = getThereD()
    Btrips = ()
    for Dtrip in Dtrips:
        if Dtrip[4] == 'Amsterdam':
            newCost = Dtrip[6] + D['ABarcelona']
        elif Dtrip[4] == 'Bergen':
            newCost = Dtrip[6] + D['BBarcelona']
        elif Dtrip[4] == 'Copenhagen':
            newCost = Dtrip[6] + D['CBarcelona']
        elif Dtrip[4] == 'Helsinki':
            newCost = Dtrip[6] + D['HBarcelona']
        elif Dtrip[4] == 'Stockholm':
            newCost = Dtrip[6] + D['SBarcelona']
        newTrip = Dtrip + (newCost,)
        Btrips = Btrips + (newTrip,)
    Btrips = sorted(Btrips, key=itemgetter(7))
    return Btrips










            

