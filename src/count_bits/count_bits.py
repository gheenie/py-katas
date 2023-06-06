def count_bits(integer):
  count_1 = 0

  while integer != 0:
    if integer % 2 == 1:
      integer -= 1
      count_1 += 1
      integer /= 2
    else:
      integer /= 2
  
  return count_1
