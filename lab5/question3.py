list_of_tuples = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]

max_func = lambda list: str(max(list, key = lambda tuple:tuple[1])[1])
min_func = lambda list: str(min(list, key = lambda tuple:tuple[1])[1])

print("Maximum value in tuple is: " + max_func(list_of_tuples))
print("Minimum value in tuple is: " + min_func(list_of_tuples))