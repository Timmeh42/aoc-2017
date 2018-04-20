with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

input_dic = {}
group_list = []
group0_list = []

for line in input_data:
	nline = "".join(list(filter(lambda ch: ch not in ",<->", line)))
	things = nline.split()
	for i in range(len(things)):
		things[i] = int(things[i])
	input_dic[things[0]] = things[1:]

def searcher(num, grup):
	group_list[grup].append(num)
	for numb in input_dic[num]:
		if numb not in group_list[grup]:
			searcher(numb, grup)

for innum in input_dic:
	group = None
	for g in range(len(group_list)):
		if innum in group_list[g]:
			group = g
			break
	if group == None:
		group_list.append([])
		group = len(group_list)-1
	searcher(innum, group)

print(len(group_list))