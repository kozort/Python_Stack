from bankAccount import BankAccount
 
class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.account = BankAccount(int_rate=0.02, balance=0)

	def make_deposit(self, amount):
		self.account.deposit(amount)
		return self

	def make_withdrawal(self, amount):
		self.account.withdraw(amount)
		return self

	def display_user_balance(self):
		self.account.display_account_info()
		return self
    
	def transfer_money(self, otherUser, amount):
		self.account.withdraw(amount)
		otherUser.account.deposit(amount)
		return self


Jane = User("Jane", "jane@gmail.com")
Jim = User("Jim", "jim@gmail.com")
John = User("John", "lohn@gmail.com")

Jane.make_deposit(100)
Jane.make_deposit(100)
Jane.make_deposit(100)
Jane.make_withdrawal(78)
Jane.display_user_balance()

Jim.make_deposit(200)
Jim.make_deposit(200)
Jim.make_withdrawal(42)
Jim.make_withdrawal(155)
Jim.display_user_balance()

John.make_deposit(500)
John.make_withdrawal(155)
John.make_withdrawal(155)
John.make_withdrawal(155)
John.display_user_balance()

Jane.transfer_money(John, 100)
Jane.display_user_balance()
John.display_user_balance()