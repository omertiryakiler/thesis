from collections import defaultdict

position = defaultdict(list)
parts = defaultdict()
parts = {'BASE_1_IN_L_': 'base', 'LINK1_1_IN_L_': 'link_1','LINK2_1_IN_L_': 'link_2','ENDEFF_1_IN_L_': 'endeff','OPERATOR_1_ARM_AREA_IN_L_': 'arm', 'OPERATOR_1_HEAD_AREA_IN_L_': 'head'}
#dealing with time = 0
for p in parts:
	position[parts[p]].append('0')
#

with open('output.hist.txt', 'r') as f_orig:
	i = 0
	for line in f_orig:
		if (i > 1):
			for p in parts:
				if p in line:
					position[parts[p]].append(line[-2:])
		if "------ time" in line:
			i += 1

#print(position['link_1'])
#print(position['link_2'])
#print(position['base'])
#print(position['arm'])
#print(position['head'])
#print(position['endeff'])

A=[position['link_1'], position['link_2'], position['base'], position['arm'], position['head'], position['endeff']]

print(A)
