with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

reg = {}
maxv = 0

for line in input_data:
	parts = line.split()
	#print(parts[0]+" "+parts[1]+" "+parts[2]+" "+parts[3]+" "+parts[4]+" "+parts[5]+" "+parts[6])
	#print("------------------")
	oreg = parts[0]
	if oreg not in reg:
		reg[oreg] = 0
	#print(oreg, reg[oreg])
	ireg = parts[4]
	oval = int(parts[2])
	if parts[1] == "dec":
		oval = -1*oval
	stmnt = 'reg["'+parts[4]+'"]'+parts[5]+parts[6]
	sttrue = False
	if ireg not in reg:
		reg[ireg] = 0
	sttrue = eval(stmnt)
		#print(ireg, reg[ireg])
	if sttrue:
		reg[oreg] += oval
		maxv = max(maxv, reg[oreg])

for areg in reg:
	print(areg, reg[areg])

print(maxv)
