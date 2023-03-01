import copy

def bubble_sort(array, calls=0):
	if len(array) == 0: return []

	nums = copy.deepcopy(array)

	if len(array) == 1: return nums

	length_nums_minus_1 = len(nums) - 1

	for i in range(length_nums_minus_1):
		current_num = nums[i]
		next_num = nums[i + 1]

		if current_num > next_num:
			nums[i] = next_num
			nums[i + 1] = current_num

	calls += 1

	if calls == length_nums_minus_1:
		return nums

	return bubble_sort(nums, calls)
