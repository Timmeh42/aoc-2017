import time
with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

moves = input_data[0].split(',')

seq = 'abcdefghijklmnop'

seqs = []

def spin(s):
	global seq
	s = int(s)
	seq = seq[-s:]+seq[:-s]

def exch(p1, p2):
	global seq
	p1 = int(p1)
	p2 = int(p2)
	pr1 = min(p1, p2)
	pr2 = max(p1, p2)
	seq = seq[0:pr1]+seq[pr2]+seq[pr1+1:pr2]+seq[pr1]+seq[pr2+1:]

def part(c1, c2):
	global seq
	p1 = seq.index(c1)
	p2 = seq.index(c2)
	exch(p1, p2)

startt = time.time()

reps = 1000000000
cyclefound = False
cycle = 0

while reps > 0:
	for move in moves:
		step = move[0]
		progs = move[1:].split('/')
		if step == 's':
			spin(progs[0])
		if step == 'x':
			exch(progs[0], progs[1])
		if step == 'p':
			part(progs[0], progs[1])
	if seq not in seqs or cyclefound == True:
		seqs.append(seq)
		reps -= 1
	else:
		reps = reps%len(seqs)
		reps -= 1
		cycle = len(seqs)
		cyclefound = True

endt = time.time()
print(endt - startt)
print(cycle)
print(seq)
