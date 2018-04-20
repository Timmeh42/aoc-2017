with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()[0]

banks = input_data.split()
mem = []
for i in range(len(banks)):
	banks[i] = int(banks[i])

#banks = [0,2,7,0]
print(banks)

first = 0


def shuffle():
	global banks
	pos = 0
	for p in range(len(banks)):
		if banks[p] == max(banks):
			pos = p
			break
	bin = banks[pos]
	banks[pos] = 0
	for i in range(bin):
		bpos = (pos + 1 + i)%(len(banks))
		banks[bpos] += 1

def hash():
	global first
	hsh = ""
	for b in banks:
		hsh += str(b) + " "
	hsh = hsh[:-1]

	for mb in mem:
		if mb == hsh:
			first = mem.index(hsh)
			return True
	mem.append(hsh)
	return False

while True:
	shuffle()
	if hash():
		break
print(len(mem)-first)