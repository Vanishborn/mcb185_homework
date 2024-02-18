# 53genomestats.py by Henry Li and Lisa Yuan

import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]

	for val in vals:
		if val < mini:
			mini = val
		if val > maxi:
			maxi = val

	return mini, maxi

def mean(vals):
	total = 0

	for val in vals:
		total += val

	return total / len(vals)

def standard_deviation(my_list, mean):
	length = len(my_list)

	if length < 2:
		return 0
	
	sum_list = 0

	for item in my_list:
		sum_list += (item - mean) ** 2

	variance = sum_list / length
	std_dev = variance ** 0.5

	return std_dev

def median(my_list):
	my_list.sort()
	length = len(my_list)
	
	if length % 2 == 0:
		middle_left = my_list[length // 2 - 1]
		middle_right = my_list[length // 2]
		median_value = (middle_left + middle_right) / 2
	else:
		median_value = my_list[length // 2]

	return median_value

feature_count = 0
feature_lengths = []

with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		line = line.split('\t')
		if line[2] == feature:
			feature_count += 1
			feature_lengths.append(int(line[4])-int(line[3])+1)

feature_min, feature_max = minmax(feature_lengths)
feature_mean = mean(feature_lengths)
feature_SD = standard_deviation(feature_lengths, feature_mean)
feature_median = median(feature_lengths)

print('count:', feature_count)
print('min:', feature_min)
print('max:', feature_max)
print('mean:', feature_mean)
print('standard deviation:', feature_SD)
print('median:', feature_median)
# print('range:', feature_max-feature_min)
