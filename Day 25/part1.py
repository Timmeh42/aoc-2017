cursor = 0
tape = 0
state = 0
step = 0
stop = 12523873

while (step < stop):
	step+=1
	if cursor >= 0:
		mask = 1 << cursor
	else:
		mask = 1 >> abs(cursor)
	if state == 0:
		if tape & mask:
			cursor -= 1
			state = 4
			continue
		tape = tape ^ mask
		cursor += 1
		state = 1
		continue
	elif state == 1:
		if tape & mask:
			cursor += 1
			state = 5
			continue
		tape = tape ^ mask
		cursor += 1
		state = 2
		continue
	elif state == 2:
		if tape & mask:
			tape = tape ^ mask
			cursor += 1
			state = 1
			continue
		tape = tape ^ mask
		cursor -= 1
		state = 3
		continue
	elif state == 3:
		if tape & mask:
			tape = tape ^ mask
			cursor -= 1
			state = 2
			continue
		tape = tape ^ mask
		cursor += 1
		state = 4
		continue
	elif state == 4:
		if tape & mask:
			tape = tape ^ mask
			cursor += 1
			state = 3
			continue
		tape = tape ^ mask
		cursor -= 1
		state = 0
		continue
	elif state == 5:
		if tape & mask:
			tape = tape ^ mask
			cursor += 1
			state = 2
			continue
		tape = tape ^ mask
		cursor += 1
		state = 0
		continue
print(bin(tape).count("1"))