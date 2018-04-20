with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

grid = {(x-12,y-12):1 for y in range(len(input_data)) for x in range(len(input_data[y])) if input_data[y][x] == '#'}

pos = [0,0]
drc = [0,-1]
infs = 0

for step in range(10000):
	p = tuple(pos)
	if p in grid:
		drc = [-drc[1], drc[0]]
		del grid[p]
	else:
		drc = [drc[1], -drc[0]]
		grid[p] = 1
		infs+=1
	pos = [pos[0]+drc[0], pos[1]+drc[1]]
print(infs)