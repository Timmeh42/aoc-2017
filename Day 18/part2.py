with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

prog = []

for line in input_data:
	prog.append(line.split())

regs = [{},{}]
lin = [0,0]
msq = [[],[]]
act = 0
dead = 0
sends = 0

def set(r, v):
	global regs
	if v in regs[act]:
		regs[act][r] = regs[act][v]
	else:
		regs[act][r] = int(v)

def add(r, v):
	global regs
	if v in regs[act]:
		regs[act][r] += regs[act][v]
	else:
		regs[act][r] += int(v)

def mul(r, v):
	global regs
	if v in regs[act]:
		regs[act][r] = regs[act][r] * regs[act][v]
	else:
		regs[act][r] = regs[act][r] * int(v)

def mod(r, v):
	global regs
	if v in regs[act]:
		regs[act][r] = regs[act][r] % regs[act][v]
	else:
		regs[act][r] = regs[act][r] % int(v)

def jgz(r, v):
	global regs, lin
	if regs[act][r] != 0:
		lin[act] -= 1
		if v in regs[act]:
			lin[act] += regs[act][v]
		else:
			lin[act] += int(v)

def snd(r):
	global regs, msq, sends
	if act == 1:
		sends += 1
	if r in regs[act]:
		msq[1-act].append(regs[act][r])
	else:
		msq[1-act].append(int(r))

def rcv(r):
	global regs, msq, act, dead
	if len(msq[act]) != 0:
		regs[act][r] = msq[act].pop(0)
		dead = 0
	else:
		act = 1-act
		lin[act] -= 1
		dead += 1
		#print('waiting')

regs[0]['p'] = 0
regs[1]['p'] = 1

while (lin[act] in range(len(prog)) and dead <= 1):
	arg = prog[lin[act]]
	#print(" "*10*act + str(arg))
	if arg[1] not in regs[act]:
			regs[act][arg[1]] = 0
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
	lin[act]+=1

print(sends)