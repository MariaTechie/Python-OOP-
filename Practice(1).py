class Bankaccount():  # Defining a class named Bankaccount
    def __init__(self, name, type, balance=0):  # Constructor to initialize account details, with balance defaulting to 0
        self.__name = name  # Private attribute 
        self.__type = type  
        self.__balance = balance  
    
    def getBalance(self):  # Method to access the private balance attribute getter (because the attribute is private you can only have acccess to it in its class but here we used the value of the balance in the child class )
        return self.__balance  
         
    def setBalance(self, x):  # Method to set a new value for the balance setter in order to change the value later on 
        self.__balance = x  # Updates the balance to a new value
        
    def deposit(self, amount):  #instance metohd
        self.__balance += amount  # Adds the deposit amount to the current balance
        return self.__balance  # Returns the new balance
    
    def withdraw(self, value):  
        if value > self.__balance:  # Checks if the withdrawal amount is greater than the current balance
            print("You dont have enough") 
            return None
        else:
            self.__balance -= value  # Subtracts the withdrawal amount from the balance
            return self.__balance  # Returns the new balance (Rember we can actully hee have direct access to the balance becuase we are in the parent class later on you would need to use the setter method)
    
    def account(self): 
        return f'The name is {self.__name} and the type is {self.__type} the balance is {self.__balance}'
    
# Creating a subclass 
class SavingsAccount(Bankaccount):
    def __init__(self, name, type, balance):  # Constructor for SavingsAccount
        super().__init__(name, type, balance)  # Uses the parent class's __init__ method to set name, type, and balance by using the super()
             
    def calculate_intrest(self):  # Instance Method to calculate interest on the balance
        balance = self.getBalance()  # Get the current balance using the getter method and storing the value in a new variable
        intrest = (balance * 5) / 100  # Calculate 5% interest on the balance
        print(f'The intrest amount that will be added to the balance is {intrest}')  # Print the interest amount
        balance += intrest  # Add the interest to the balance
        self.setBalance(balance)  # Update the new balance using the setter method
        return f'The total in your balance is now {balance}'  # Return the updated balance after adding interest

# Creating another subclass 
class Chekingaccount(Bankaccount):
    def __init__(self, name, type, balance):  # Constructor for Chekingaccount, same as SavingsAccount
        super().__init__(name, type, balance)  # Call the parent class's __init__ method
    
    def calculate_withdraw(self, amount):  # Method to calculate if the withdrawal amount is allowed and apply fees
        balance = self.getBalance()  # Get the current balance  and store the value in a local variable
        average = balance / 4  # Calculate 1/4th of the balance
        if amount > average:  # Check if the withdrawal amount is more than 1/4th of the balance
            print("The amount is more than the average you can withdraw") 
            return None# If too much, print a message
        else:
            fees = (amount * 2) / 100  # Calculate 2% fee on the withdrawal amount
            print(f'{fees}$ will be reduced as fees')  # Print the fee that will be deducted
            balance = balance - amount - fees  # Subtract the withdrawal amount and fees from the balance
            self.setBalance(balance)  # Update the new balance after withdrawal and fee deduction
            return f'The current amount in your balance is {balance}'  # Return the updated balance
         
# Creating objects (instances) of the classes to use the methods

object1 = Bankaccount("hadi", "personal", 600) 
object1.withdraw(900)  # Try to withdraw 900 (not enough balance, so will print a message)
object1.withdraw(100)  # Withdraw 100 successfully
object1.deposit(200)  # Deposit 200 to the balance
print(object1.account())  # Print account details (name, type, and balance)

print("------------------------------------------------------------------------------------------------------------------------------")

object2 = SavingsAccount("rami", 'personal', 400)  # Create an instance of SavingsAccount
print(object2.calculate_intrest())  # Calculate interest to the balance, then print the updated balance
print("----------------------------------------------------------------------------------------------------------------------------")

object3 = Chekingaccount('Youssef', "personal", 900)  # Create an instance of Chekingaccount with balance of 900
print(object3.calculate_withdraw(100))  # Try to withdraw 100 and apply the withdrawal fees, then print the new balance
