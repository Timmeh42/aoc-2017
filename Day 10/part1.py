with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

lens = input_data[0].split(",")
for i in range(len(lens)):
	lens[i] = int(lens[i])

def rotate(lst, rotation):
	if rotation > 0:
		rotation = rotation%len(lst)
	else:
		rotation = -1*(-rotation%len(lst))
	nlist = lst[rotation:]+lst[:rotation]
	if len(nlist) != len(lst):
		print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ")
	return nlist



skip = 0
pos = 0
#lens = [3,4,1,5]
#hlist = [0,1,2,3,4]
hlist = list(range(256))

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
print(hlist[0]*hlist[1])

