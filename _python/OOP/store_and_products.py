from products import Product
from store import Store

orange = Product("Oranges", 5, "Fruit")
apple = Product("Apple", 4, "Fruit")
melon = Product("Watermelon", 3, "Fruit")
peanut = Product("Peanuts", 1.20, "Nuts")
cashew = Product("Cashews", 1.40, "Nuts")
wallymart = Store("Wallymart")
wallymart.add_product(apple).add_product(orange).add_product(melon).add_product(peanut).add_product(cashew)

def print_full_store():
	print("-"*35)
	print("-"*35)
	print(wallymart.name)

	for i in range(len(wallymart.productList)):
		print("-"*25)
		wallymart.productList[i].print_info()
		

print_full_store()
wallymart.inflation(.25)
print_full_store()
wallymart.set_clearance("Fruit",.5)
print_full_store()
wallymart.sell_product(orange.id)
wallymart.sell_product(apple.id)
wallymart.sell_product(melon.id)
wallymart.sell_product(peanut.id)
wallymart.sell_product(cashew.id)
print_full_store()