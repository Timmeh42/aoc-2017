with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

prog = []

for line in input_data:
	prog.append(line.split())

regs = {}
lin = 0
rec = 0

def set(r, v):
	global regs
	if v in regs:
		regs[r] = regs[v]
	else:
		regs[r] = int(v)

def add(r, v):
	global regs
	if v in regs:
		regs[r] += regs[v]
	else:
		regs[r] += int(v)

def mul(r, v):
	global regs
	if v in regs:
		regs[r] = regs[r] * regs[v]
	else:
		regs[r] = regs[r] * int(v)

def mod(r, v):
	global regs
	if v in regs:
		regs[r] = regs[r] % regs[v]
	else:
		regs[r] = regs[r] % int(v)

def jgz(r, v):
	global regs, lin
	if regs[r] != 0:
		lin -= 1
		if v in regs:
			lin += regs[v]
		else:
			lin += int(v)

def snd(r):
	global regs, rec
	if r in regs:
		rec = regs[r]
	else:
		rec = int(r)

def rcv(r):
	global regs
	if r in regs:
		if regs[r] != 0:
			print('recovered '+str(rec))

while (lin in range(len(prog))):
	arg = prog[lin]
	print(arg)
	if arg[1] not in regs:
		regs[arg[1]] = 0
	if arg[0] == 'set':
		set(arg[1], arg[2])
	if arg[0] == 'add':
		add(arg[1], arg[2])
	if arg[0] == 'mul':
		mul(arg[1], arg[2])
	if arg[0] == 'mod':
		mod(arg[1], arg[2])
	if arg[0] == 'jgz':
		jgz(arg[1], arg[2])
	if arg[0] == 'rcv':
		rcv(arg[1])
	if arg[0] == 'snd':
		snd(arg[1])
	lin+=1