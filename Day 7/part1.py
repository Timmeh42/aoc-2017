with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

tree = {}

for line in input_data:
	bits = line.split()
	me = bits[0]
	tree[me] = {}
	tree[me]["weight"] = int(bits[1][1:-1])
	tree[me]["children"] = []
	tree[me]["parent"] = ""
	if len(bits) > 2:
		for i in range(3, len(bits)):
			if i != len(bits)-1:
				child = bits[i][:-1]
			else:
				child = bits[i]
			tree[me]["children"].append(child)
for branch in tree:
	for child in tree[branch]["children"]:
		tree[child]["parent"] = branch
for branch in tree:
	if tree[branch]["parent"] == "":
		print(branch)
