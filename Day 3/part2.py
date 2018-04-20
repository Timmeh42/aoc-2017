import math
input_data = 368078

def ringmax(ring):
	return 1+(ring)*(ring+1)*4

def getring(numb):
	return math.ceil(math.sqrt(numb))//2

def getringpos(numb):
	ring = getring(numb)
	n = numb - ring - ringmax(ring-1)
	n = n%(ring*2)
	n = ring - math.fabs(ring - n)
	return int(n)

def left():
	global dirc
	dirc = [-dirc[1], dirc[0]]
	#print("left")

def right():
	global dirc
	dirc = [dirc[1], -dirc[0]]
	#print("right")

def frwd():
	global pos
	pos = [pos[0]+dirc[0], pos[1]+dirc[1]]
	#print("forward")

def back():
	global pos
	pos = [pos[0]-dirc[0], pos[1]-dirc[1]]
	#print("back")

def step():
	left()
	frwd()
	if (tuple(pos) in data_map):
		back()
		right()
		frwd()

def sumup():
	global data_map
	val = 0
	for x in range(-1,2):
		for y in range(-1,2):
			npos = [pos[0]+x,pos[1]+y]
			if (tuple(npos) in data_map):
				val += data_map[tuple(npos)]
	data_map[tuple(pos)] = val
	print(pos, val)
	#print(val)

goal = input_data
curr = 1

data_map = {}

pos = [0,0]
dirc = [0,-1]	# [1,0] [0,1] [-1,0] [0,-1]

data_map[tuple(pos)] = 1
end = False

while (not end):
	step()
	sumup()
	if (data_map[tuple(pos)] >= goal):
		end = True
		print(data_map[tuple(pos)])


"""






1
2	3	4	5	6	7	8	9
10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49

neighbours:
always the previous number

1
1	2	3	4	5	6	7	8
1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16
1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24



12	11	10	9	8	7	6
13	8	7	6	5	4	5
14	9	4	3	2	3	4	
15	10	5	1	1	2	3
16	11	6	7	8	1	2
17	12	13	14	15	16	1
18	19	20	21	22	23	24


"""