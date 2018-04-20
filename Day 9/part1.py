with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()


def stream_score(strim):
	level = 0
	score = 0
	garbage = False
	skip = False
	for c in strim:
		#print(c)
		if skip:
			skip = False
			#print("Skipped due to !")
			continue
		
		if c == '!':
			skip = True
			#print("Skipping next character")
			continue

		if garbage == True:
			if c == '>':
				garbage = False
				#print("Garbage section finished")
			continue

		if c == '<':
			garbage = True
			#print("Garbage section started")
			continue

		if c == '{':
			level += 1
			#print("New level started", level)
			continue

		if c == '}':
			score += level
			level -= 1
			#print("Level ended", level)
			continue
	return score

inputs = ["{}", "{{{}}}", "{{},{}}", "{{{},{},{{}}}}", "{<a>,<a>,<a>,<a>}", "{{<ab>},{<ab>},{<ab>},{<ab>}}", "{{<!!>},{<!!>},{<!!>},{<!!>}}", "{{<a!>},{<a!>},{<a!>},{<ab>}}"]

#for i in inputs:
	#print(i, stream_score(i))
print(stream_score(input_data[0]))


