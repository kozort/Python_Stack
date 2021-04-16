
class Store:
	def __init__(self, name="Store Default"):
		self.name = name
		self.productList = []
	def add_product(self, new_product):
		#  - takes a product and adds it to the store
		self.product.append(new_product)
		return self

	def sell_product(self, id):
		#  - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
		return self

	def inflation(self, percent_increase):
		#  - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
		return self

	def set_clearance(self, category, percent_discount):
		#  - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)
		return self


