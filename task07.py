prices = ["$120", "$340", "$50", "$90"] 
prices_list = list(map(
    lambda price : float(price [1:]) , prices
))

print(prices_list)