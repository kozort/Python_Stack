class Product:
	def __init__(self, name= "Unnamed Prodcut", price=0, category="uncategorized"):
		self.name = name
		self.price = price
		self.category = category
	
	def update_price(self, percent_change, is_increased): 
		if is_increased:
			self.price *= 1+percent_change
		else:
			self.price *= 1-percent_change
		return self

	def print_info(self):
		print(f"Product name: {self.name}\nCategory:     {self.category}\nPrice:        ${self.price}")
		return self

#test cases
if __name__ == "__main__":
	product = Product("Oranges", 5, "Fruit")
	product.print_info()
	print("-"*20)
	print("10% inflation :(")
	product.update_price(0.1,True)
	product.print_info()
	print("-"*20)
	print("Going in Clearance!")
	product.update_price(0.5,False)
	product.print_info()

    