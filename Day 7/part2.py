def checkweight(me):
	if tree[me]["children"] == []:
		tree[me]["balanced"] = True
		tree[me]["totalweight"] = tree[me]["weight"]
	else:
		sub = 0
		tree[me]["balanced"] = True
		tree[me]["totalweight"] = tree[me]["weight"]
		for branch in tree[me]["children"]:
			checkweight(branch)
			tree[me]["totalweight"] += tree[branch]["totalweight"]
			if tree[branch]["totalweight"] != sub and sub !=0:
				tree[me]["balanced"] = False
			else:
				sub = tree[branch]["totalweight"]

def checkbalance(me, level):
	print(" "*level+me+" "+str(tree[me]))
	if tree[me]["balanced"] == False:
		for branch in tree[me]["children"]:
			checkbalance(branch, level+1)

def propagatebalance(me):
	weights = []
	for branch in tree[me]["children"]:
		weights.append(tree[branch]["totalweight"])
	offweight = max(weights) - min(weights)

with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

tree = {}
root = ""

for line in input_data:
	bits = line.split()
	me = bits[0]
	tree[me] = {}
	tree[me]["weight"] = int(bits[1][1:-1])
	tree[me]["totalweight"] = 0
	tree[me]["children"] = []
	tree[me]["parent"] = ""
	tree[me]["balanced"] = False
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
		root = branch

print("Root: "+root)
checkweight(root)

checkbalance(root, 0)