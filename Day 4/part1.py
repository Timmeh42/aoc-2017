with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

valids = 0
for line in input_data:
	words = line.split()
	dupes = 0
	for i in range(len(words)):
		for j in range(len(words)):
			if (i!=j and words[i] == words[j]):
				dupes+=1
	if (dupes == 0):
		valids += 1

print(valids)

