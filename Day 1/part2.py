with open("input.txt","r",newline="") as archive:
	input_data = archive.read()

total_sum = 0
skip = len(input_data)//2

for i in range(len(input_data)):
	if (input_data[i-skip] == input_data[i]):
		print(input_data[i-skip])
		total_sum += int(input_data[i-skip])

print(total_sum)

################################
end = input("")