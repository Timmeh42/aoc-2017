with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

input_dic = {}
group0_list = []

for line in input_data:
	nline = "".join(list(filter(lambda ch: ch not in ",<->", line)))
	things = nline.split()
	for i in range(len(things)):
		things[i] = int(things[i])
	input_dic[things[0]] = things[1:]

def searcher(num):
	group0_list.append(num)
	for numb in input_dic[num]:
		if numb not in group0_list:
			searcher(numb)

searcher(0)
print(len(group0_list))