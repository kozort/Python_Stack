class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)
    
    def transfer_money(self, otherUser, amount):
        self.account_balance -= amount
        otherUser.account_balance += amount


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