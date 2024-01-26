# 24accuracy.py by Henry Li and Lisa Yuan

# Given values for true positives, false positives, true negatives,
# and false negatives, write a function that returns the accuracy and F1 score.
# assuming all valid input
def accuracy_f1(tp, fp, tn, fn):
	accuracy = (tp + tn) / (tp + fp + tn + fn)
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	f1 = 2 * (precision * recall) / (precision + recall)
	
	return accuracy, f1

print(accuracy_f1(2, 2, 2, 2))
print(accuracy_f1(5, 1, 8, 1))
print(accuracy_f1(4, 2, 6, 6))
