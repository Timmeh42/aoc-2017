with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

net = {(x,y): input_data[y][x] for y in range(len(input_data)) for x in range(len(input_data[y])) if input_data[y][x] not in [' ', '\r', '\n']}

pos = [109, 0]

drc = [0,1]

lets = []
steps = 1

while (True):
	pos = [pos[0]+drc[0], pos[1]+drc[1]]
	try:
		c = net[tuple(pos)]
	except:
		break
	steps+=1
	print(c)
	if c == '+':
		print(drc)
		if abs(drc[1]) == 1:
			print((pos[0]-1, pos[1]) in net)
			print((pos[0]+1, pos[1]) in net)
			if (pos[0]-1, pos[1]) in net and net[(pos[0]-1, pos[1])] == '-':
				print('going left')
				drc = [-1, 0]
			elif (pos[0]+1, pos[1]) in net and net[(pos[0]+1, pos[1])] == '-':
				print('going right')
				drc = [1, 0]
			else:
				break
		elif abs(drc[0]) == 1:
			print((pos[0], pos[1]-1) in net)
			print((pos[0], pos[1]+1) in net)
			if (pos[0], pos[1]-1) in net and net[(pos[0], pos[1]-1)] == '|':
				print('going up')
				drc = [0, -1]
			elif (pos[0], pos[1]+1) in net and net[(pos[0], pos[1]+1)] == '|':
				print('going down')
				drc = [0, 1]
			else:
				break
	else:
		if c.isalpha() == True:
			lets.append(c)

print(lets)

print(steps)