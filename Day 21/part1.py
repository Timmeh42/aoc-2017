with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

import numpy as np

rules = {}

def rot(strn):
	if len(strn) == 4:
		rstrn = strn[1] + strn[3] + strn[0] + strn[2]
	elif len(strn) == 9:
		rstrn = strn[2] + strn[5] + strn[8] + strn[1] + strn[4] + strn[7] + strn[0] + strn[3] + strn[6]
	return rstrn

def flip(strn):
	if len(strn) == 4:
		rstrn = strn[1::-1] + strn[3:1:-1]
	elif len(strn) == 9:
		rstrn = strn[2::-1] + strn[5:2:-1] + strn[8:5:-1]
	return rstrn

for line in input_data:
	line = line.replace('.', '0')
	line = line.replace('#', '1')
	inp, out = line.strip().split(' => ')
	inps = inp.replace('/', '')
	out = out.replace('/', '')
	outs = [int(c) for c in out]
	if len(outs) == 9:
		outs = np.array([outs[0:3], outs[3:6], outs[6:9]])
	elif len(outs) == 16:
		outs = np.array([outs[0:4], outs[4:8], outs[8:12], outs[12:16]])
	rules[inps] = outs
	print(inps, outs.flatten())
	inps = flip(inps)
	if inps not in rules:
		rules[inps] = outs
		print(inps, outs.flatten())
	inps = flip(inps)

	for i in range(3):
		inps = rot(inps)
		if inps not in rules:
			rules[inps] = outs
			print(inps, outs.flatten())
		inps = flip(inps)
		if inps not in rules:
			rules[inps] = outs
			print(inps, outs.flatten())
		inps = flip(inps)
	print('-----------')

print('-------------------------------')

grid = np.array([[0, 1, 0],
				[0, 0, 1],
				[1, 1, 1]])
print(grid)


for i in range(18):
	gs = grid.shape[0]
	if gs % 2 == 0:
		mgs = gs // 2
		newgrid = np.zeros((gs+mgs,gs+mgs), dtype=np.int)
		for y in range(mgs):
			for x in range(mgs):
				minigrid = grid[y*2:(y+1)*2, x*2:(x+1)*2]
				gstr = ''.join([str(n) for n in minigrid.flatten()])
				outmini = rules[gstr]
				newgrid[y*3:(y+1)*3, x*3:(x+1)*3] = outmini
	elif gs % 3 == 0:
		mgs = gs // 3
		newgrid = np.zeros((gs+mgs,gs+mgs), dtype=np.int)
		for y in range(mgs):
			for x in range(mgs):
				minigrid = grid[y*3:(y+1)*3, x*3:(x+1)*3]
				gstr = ''.join([str(n) for n in minigrid.flatten()])
				outmini = rules[gstr]
				newgrid[y*4:(y+1)*4, x*4:(x+1)*4] = outmini
	grid = newgrid
	#print(grid)

count = len(list([n for n in grid.flatten() if n == 1]))
print(count)