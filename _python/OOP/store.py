from products import Product

class Store:
	def __init__(self, name="Store Default"):
		self.name = name
		self.productList = []

	def add_product(self, new_product):
		#  - takes a product and adds it to the store
		self.productList.append(new_product)
		return self

	def sell_product(self, id):
		#  - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
		print("*"*25)
		print("Sold Product:")
		print("*"*15)
		for i in range(len(self.productList)):
			if self.productList[i].id == id:
				self.productList[i].print_info()
				print("*"*15)
				self.productList.remove(self.productList[i])
				break
		return self

	def inflation(self, percent_increase):
		#  - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
		for i in range(len(self.productList)):
			self.productList[i].update_price(percent_increase, True)
		return self

	def set_clearance(self, category, percent_discount):
		#  - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)
		for i in range(len(self.productList)):
			if self.productList[i].category == category:
				self.productList[i].update_price(percent_discount, False)
		return self

if __name__ == "__main__":
	orange = Product("Oranges", 5, "Fruit")
	apple = Product("Apple", 4, "Fruit")
	melon = Product("Watermelon", 3, "Fruit")
	wallymart = Store("Wallymart")
	wallymart.add_product(apple)
	wallymart.add_product(orange)
	wallymart.add_product(melon)
	wallymart.productList[0].print_info()
