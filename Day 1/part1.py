with open("input.txt","r",newline="") as archive:
	input_data = archive.read()

total_sum = 0

for i in range(len(input_data)):
	if (input_data[i-1] == input_data[i]):
		print(input_data[i-1])
		total_sum += int(input_data[i-1])

print(total_sum)

################################
end = input("")