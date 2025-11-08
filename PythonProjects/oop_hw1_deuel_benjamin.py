class bankAccount:
	def __init__(self, accountId, owner, balance):
		self.accountId = accountId
		self.owner = owner
		self._balance = balance
	
	@property
	def balance(self): return self._balance
	def __str__(self): return f"Account #{str(self.accountId)} - Owner: {self.owner} - Balance: ${self._balance}"
	
	def deposit(self, amount):
		if amount <= 0: print("ERROR: Amount must be greater than 0.")
		else: self._balance += amount
		return self._balance
	def withdraw(self, amount):
		if amount > self._balance: print("ERROR: You do not have enough money.")
		elif amount <= 0: print("ERROR: Amount must be greater than 0.")
		else: self._balance -= amount
		return self._balance

class savingsAccount(bankAccount):
	def __init__(self, accountId, owner, balance, interest):
		super().__init__(accountId, owner, balance)
		self.interest = interest / 100.0
	
	def addInterest(self):
		interestAmount = self._balance * self.interest
		self._balance += interestAmount
		return interestAmount
	def withdraw(self, amount):
		if self._balance - amount < 100.0:
			print("ERROR: Cannot go below $100 balance.")
			return self._balance
		else: return super().withdraw(amount)

try:
	if __name__ == "__main__":
		# Regular account
		regular = bankAccount("1001", "Alice", 500)
		print(regular)
		regular.deposit(100)
		print(f"After deposit: ${regular.balance}")
		regular.withdraw(200)
		print(f"After withdrawal: ${regular.balance}")
		print("\n" + "="*40 + "\n")
		# Savings account
		savings = savingsAccount("2001", "Bob", 1000, 0.02)
		print(savings)
		interest = savings.addInterest()
		print(f"Interest earned: ${interest:.2f}")
		print(f"New balance: ${savings.balance}")
		# Try to go below minimum
		savings.withdraw(950) # Should fail
		savings.withdraw(500) # Should work
		print(f"Final balance: ${savings.balance}")
		input()
except Exception as e: input(e)