with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

input_data = "230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167"

lens = []
for i in input_data:
	lens.append(ord(i))
lens = lens + [17,31,73,47,23]

def rotate(lst, rotation):
	if rotation > 0:
		rotation = rotation%len(lst)
	else:
		rotation = -1*(-rotation%len(lst))
	nlist = lst[rotation:]+lst[:rotation]
	return nlist


skip = 0
pos = 0
#lens = [3,4,1,5]
#hlist = [0,1,2,3,4]
hlist = list(range(256))

for i in range(64):
	for hlen in lens:
		#print("---------------")
		#print(hlist)

		#print("rotate by",pos)
		hlist = rotate(hlist,pos)
		#print(hlist)

		#print("flip inner list from 0 to", hlen-1)
		if hlen != 0:
			hlist = hlist[hlen-1::-1] + hlist[hlen:]
		#print(hlist)

		#print("rotate by",-pos)
		hlist = rotate(hlist,-pos)

		pos += hlen + skip
		skip += 1
print(hlist)

knot_hash = ""
for i in range(16):
	subl = hlist[i*16:(1+i)*16]
	xor = subl[0]
	for j in subl[1:]:
		xor = xor ^ j
	knot_hash += format(xor, "02x")
print(knot_hash)
