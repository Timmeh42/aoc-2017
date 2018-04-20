with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

valids = 0
for line in input_data:
	words = line.split()
	wordlist = []
	valid = True

	for word in words:
		charlist = list(word)
		ana = "".join(sorted(charlist))
		for anaword in wordlist:
			if (ana == anaword):
				valid = False
		wordlist.append(ana)
	if (valid):
		valids += 1


print(valids)

