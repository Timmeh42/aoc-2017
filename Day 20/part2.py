with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

prts = []

for line in input_data:
	stats = line.split()
	p = [int(n) for n in stats[0][3:-2].split(',')]
	v = [int(n) for n in stats[1][3:-2].split(',')]
	a = [int(n) for n in stats[2][3:-1].split(',')]
	prts.append([p,v,a])

for t in range(1000):
	posses = {}
	for i in range(len(prts)):
		p = prts[i]
		if tuple(p[0]) in posses:
			posses[tuple(p[0])].append(i)
		else:
			posses[tuple(p[0])] = []
			posses[tuple(p[0])].append(i)
	new_prts = [[[p[0][0]+p[1][0]+p[2][0], p[0][1]+p[1][1]+p[2][1], p[0][2]+p[1][2]+p[2][2]], [p[1][0]+p[2][0], p[1][1]+p[2][1], p[1][2]+p[2][2]], [p[2][0], p[2][1], p[2][2]]] for p in prts if len(posses[tuple(p[0])]) == 1]
	prts = new_prts

print(len(prts))