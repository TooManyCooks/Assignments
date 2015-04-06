#!/usr/bin/env python
import itertools

lengthMatrix = [[0 for x in range(80)] for x in range(80)]
pointsMatrix = [[0 for x in range(2)] for x in range(80)]

def solve_tsp(points):
    
    #initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1):(dist, [0,idx+1]) for idx,dist in enumerate(lengthMatrix[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + lengthMatrix[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        A = B
    result = min([(A[d][0] + lengthMatrix[0][d[1]], A[d][1]) for d in iter(A)])
    return result[1]

lengthMatrix = [[0 for x in range(80)] for x in range(80)]
pointsMatrix = [[0 for x in range(2)] for x in range(80)]

points = open("tspPoints.txt", "r+")
for i in range(80):
    currentPos = points.readline()
    currentPos = currentPos.split(',')
    for j in range(80):
        pointsMatrix[i][0] = currentPos[1]
        pointsMatrix[i][1] = currentPos[2].strip('\r\n')

for i in range(80):
    for j in range(80):
        lengthMatrix[i][j] = abs((float(pointsMatrix[j][0])+float(pointsMatrix[j][1]))-(float(pointsMatrix[i][0])+float(pointsMatrix[i][1])))

print solve_tsp(pointsMatrix)