class BankAccount:
	def __init__(self, int_rate=0.01, balance=0): 
		self.int_rate = int_rate
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		if self.balance < amount:
			print("Insufficient funds: Charging a $5 fee")
			self.balance -= 5
		else:
			self.balance -= amount
		return self

	def display_account_info(self):
		print(f"Balance: ${self.balance}")
		return self

	def yield_interest(self):
		self.balance *= (1+self.int_rate)
		return self

# accountOne = BankAccount(0.05, 100)
# accountOne.display_account_info()
# accountTwo = BankAccount(0.10, 50)
# accountTwo.display_account_info()
# accountOne.deposit(100).deposit(100).deposit(100).withdraw(362).yield_interest().display_account_info()
# accountTwo.deposit(100).deposit(100).withdraw(7).withdraw(7).withdraw(7).withdraw(7).yield_interest().display_account_info()