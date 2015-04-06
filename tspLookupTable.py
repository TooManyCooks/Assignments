
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
print lengthMatrix[5][65]