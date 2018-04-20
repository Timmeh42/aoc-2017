with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

prog = []

for line in input_data:
	prog.append(line.split())

regs = {l:0 for l in 'abcdefgh'}
regs['a'] = 1
lin = 0
mul_count = 0

def set(r, v):
	global regs
	if v in regs:
		regs[r] = regs[v]
	else:
		regs[r] = int(v)

def sub(r, v):
	global regs
	if v in regs:
		regs[r] -= regs[v]
	else:
		regs[r] -= int(v)

def mul(r, v):
	global regs, mul_count
	mul_count += 1
	if v in regs:
		regs[r] = regs[r] * regs[v]
	else:
		regs[r] = regs[r] * int(v)

def jnz(r, v):
	global regs, lin
	if r in regs:
		if regs[r] != 0:
			lin -= 1
			if v in regs:
				lin += regs[v]
			else:
				lin += int(v)
	else:
		if r != 0:
			lin -= 1
			if v in regs:
				lin += regs[v]
			else:
				lin += int(v)

while (lin in range(len(prog))):
	arg = prog[lin]
	print(arg)
	if arg[0] == 'set':
		set(arg[1], arg[2])
	if arg[0] == 'sub':
		sub(arg[1], arg[2])
	if arg[0] == 'mul':
		mul(arg[1], arg[2])
	if arg[0] == 'jnz':
		jnz(arg[1], arg[2])
	lin+=1
print('muls:', mul_count)