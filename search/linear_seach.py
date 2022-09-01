from typing import List, Optional


def linear_search(input_list: List[int], target: int) -> Optional[int]:
	"""
	Returns the index position of the targed if found, else returns None
	"""
	for key, value in enumerate(input_list):
		if input_list[key] == target:
			return key
	return None


def verify(index):
	if index is not None:
		print("target found at index:", index)
	else:
		print("target not found in list")

numbers = [no for no in range(10)]
result = linear_search(numbers, 8)
verify(result)

# if __name__ == "__main__":
# 	print(linear_search([2, 3, 4, 5, 6], 6))
