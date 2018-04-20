with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

wall = []
for l in input_data:
	la = l.split(': ')
	wall.append([int(la[0]), int(la[1])])
"""
wall = []
wall.append([0,3])
wall.append([1,2])
wall.append([4,4])
wall.append([6,4])
"""
severity = 0

def get_pos(t, le):
	l = le-1
	return abs((t+l)%(l*2)-l)

printout = ""
for delay in range(10000000):
	severity = 0
	caught = False
	for w in wall:
		scanner_pos = get_pos(w[0]+delay, w[1])
		pos = scanner_pos
		lng = w[1]
		#print("Wall depth: ", w[0])
		#print("Wall length: ", w[1])
		#print(scanner_pos)
		if scanner_pos == 0:
			severity += w[0] * w[1]
			caught = True
	if severity == 0:
		print(caught, severity, delay)



for i in range(10):
	lng = 9
	pos = get_pos(i, lng)
	print("[ ]"*pos+"[*]"+"[ ]"*(lng-pos-1))
