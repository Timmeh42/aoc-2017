import time
with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

grid = {(x-12,y-12):2 for y in range(len(input_data)) for x in range(len(input_data[y])) if input_data[y][x] == '#'}

pos = [0,0]
drc = [0,-1]
infs = 0

st = time.time()

#grid = {(-1,0):2, (1,-1):2}

# 0 = clean, 1 = weak, 2 = infected, 3 = flagged

for step in range(10_000_000):
	p = tuple(pos)
	if p in grid:
		if grid[p] == 1:
			grid[p] = 2
			infs+=1
		elif grid[p] == 2:
			drc = [-drc[1], drc[0]]
			grid[p] = 3
		elif grid[p] == 3:
			drc = [-drc[0], -drc[1]]
			del grid[p]
	else:
		drc = [drc[1], -drc[0]]
		grid[p] = 1
	pos = [pos[0]+drc[0], pos[1]+drc[1]]
et = time.time()
print(infs, et-st)