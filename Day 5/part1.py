with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

for i in range(len(input_data)):
	input_data[i] = int(input_data[i])

pos = 0
steps = 0

while (pos < len(input_data)):
	input_data[pos] += 1
	pos += input_data[pos]-1
	steps += 1
print(steps)