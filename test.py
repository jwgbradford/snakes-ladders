offset_size = 4
offset = (offset_size, offset_size)
offset_pattern = [(1, 1), (1, 3), (3, 1), (3, 3)]
print(offset_pattern[1])
offset = (offset_size * offset_pattern[1][0], offset_size * offset_pattern[1][1])
print(offset)