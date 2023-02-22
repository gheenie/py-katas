def create_counter(start_num):
	def up():
		nonlocal start_num
		start_num += 1
		return start_num

	def down():
		nonlocal start_num
		start_num -= 1
		return start_num

	return { 'up': up, 'down': down }
