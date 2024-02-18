# 55colorname.py by Henry Li

import sys

color_file_path = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini:
			mini = val
	return mini

user_color_val = [R, G, B]

for i in user_color_val:
	if i < 0 or i > 255:
		sys.exit('Error: color value out of range.')

color_names = []
color_vals = []

with open(color_file_path) as fp:
	for line in fp:
		line = line.split('\t')
		color_names.append(line[0])
		color_vals.append(line[2].strip())

distances = []

for item in color_vals:
	color_val = []
	color_val_str = item.split(',')
	for i in color_val_str:
		color_val.append(int(i))
	distance = dtc(user_color_val, color_val)
	distances.append(distance)

min_distance = minimum(distances)
min_index = distances.index(min_distance)

print(color_names[min_index])
