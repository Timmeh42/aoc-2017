input_data = "jxqlasbh"

def rotate(lst, rotation):
	if rotation > 0:
		rotation = rotation%len(lst)
	else:
		rotation = -1*(-rotation%len(lst))
	nlist = lst[rotation:]+lst[:rotation]
	return nlist

def knothash(instr):
	lens = []
	for i in instr:
		lens.append(ord(i))
	lens = lens + [17,31,73,47,23]
	skip = 0
	pos = 0

	hlist = list(range(256))

	for i in range(64):
		for hlen in lens:
			hlist = rotate(hlist,pos)
			if hlen != 0:
				hlist = hlist[hlen-1::-1] + hlist[hlen:]
			hlist = rotate(hlist,-pos)
			pos += hlen + skip
			skip += 1

	knot_hash = ""
	for i in range(16):
		subl = hlist[i*16:(1+i)*16]
		xor = subl[0]
		for j in subl[1:]:
			xor = xor ^ j
		knot_hash += format(xor, "02x")
	return knot_hash

tot = 0

for suffix in range(128):
	k_hash = knothash(input_data+'-'+str(suffix))
	print(input_data+'-'+str(suffix), k_hash)

	for c in k_hash:
		h = bin(int(c, 16))[2:]
		for b in h:
			if b == '1':
				tot += 1

print(tot)