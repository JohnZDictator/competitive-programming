from collections import deque

forestSize = list(map(int, input().split()))
burningTreesCount = int(input())
coordinates = list(map(int, input().split()))

row = forestSize[0]
col = forestSize[1]

firePosition = []

counter = 0
while counter < len(coordinates):
    firePosition.append((coordinates[counter], coordinates[counter+1]))
    counter += 2

fireQueue = deque()
fireQueue.append(firePosition[0])
seen = set()
current = None

while len(fireQueue) > 0:
    current = fireQueue.popleft()
    seen.append(current)

    if current[0]-1 > 0:
        fireQueue.append( (current[0]-1, current[1]) )
    if current[0]+1 < row:
        fireQueue.append( (current[0]+1, current[1]) )
    if current[1]-1 > 0:
        fireQueue.append( (current[0], current[1]-1) ) 
    if current[1]+1 < col:
        fireQueue.append( (current[0], current[1]+1) )

print(current)