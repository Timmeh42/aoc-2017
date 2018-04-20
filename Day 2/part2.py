with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

checksum = 0

for line in input_data:
	numbs = line.split()
	for i in range(len(numbs)):
		numbs[i] = int(numbs[i])
	
	for i in range(len(numbs)):
		for j in range(len(numbs)):
			div_res = numbs[i]/numbs[j]
			if (div_res != 1.0 and div_res.is_integer()):
				print(numbs[i],numbs[j])
				print(div_res)
				checksum += div_res
print(checksum)

################################
end = input("")