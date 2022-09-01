from typing import List


def recursive_binary_search(input_list: List[int], target: int):
	if len(input_list) == 0:
		return False
	else:
		midpoint = (len(input_list))//2

		if input_list[midpoint] == target:
			return True
		else:
			if input_list[midpoint] < target:
				return recursive_binary_search(input_list[midpoint+1:], target)
			else:
				return recursive_binary_search(input_list[:midpoint], target)


def verify(result):
	print("Target found: ", result)


numbers = [x for x in range(8)]
each_result = recursive_binary_search(numbers, 12)
verify(each_result)
each_result = recursive_binary_search(numbers, 5)
verify(each_result)
