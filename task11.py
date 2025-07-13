nums = list(range(1, 21))

result = list(filter(map(lambda n : n % 2 , nums)))

print(result)