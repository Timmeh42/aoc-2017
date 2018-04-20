with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

checksum = 0

for line in input_data:
	numbs = line.split()
	for i in range(len(numbs)):
		numbs[i] = int(numbs[i])
	print(numbs)
	high = max(numbs)
	low = min(numbs)
	checksum += high
	checksum -= low

print(checksum)

################################
end = input("")