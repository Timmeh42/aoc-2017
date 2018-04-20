with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

wall = []
for l in input_data:
	la = l.split(': ')
	wall.append([int(la[0]), int(la[1])])

severity = 0

def get_pos(t, le):
	l = le-1
	return abs((t+l)%(l*2)-l)

for w in wall:
	print("Wall depth: ", w[0])
	print("Wall length: ", w[1])
	print(get_pos(w[0], w[1]))
	if get_pos(w[0], w[1]) == 0:
		severity += w[0] * w[1]
print(severity)

for i in range(10):
	lng = 6
	pos = get_pos(i, lng)
	print("[ ]"*pos+"[*]"+"[ ]"*(lng-pos-1))
