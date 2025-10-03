numbers = [4, -2, 0, 7, -9, 3, -1, 5]
filtered_nums = list(filter(lambda numbers : numbers % 2 == 0 , numbers))
print(filtered_nums)