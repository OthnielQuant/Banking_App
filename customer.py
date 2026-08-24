from secrets import randbelow
from account_type import *
account_bounds = [999999999,9999999999]

class Customer: 
    def __init__(self,name: str, age : int, initial_deposit: float, account_typing : AccountType):  
        self.name = name 
        self.age = age 
        self.initial_depsoit = initial_deposit  
        self.account_type =  account_typing
        self.__account_number = str(randbelow(account_bounds[0],account_bounds[1]))
        self.__balance = initial_deposit  


        if self.initial_deposit < 0: 
            raise ValueError("Initial deposit cannot be negative")  

    def get_balance(self):   
        return self.__balance 

    def get_account_number(self): 
        return self.__account_number 

    def deposit(self,amount: float): 
        if amount <= 0: 
            raise ValueError("Depsoit must be greater than zero") 

        self.__balance += amount

    def withdraw(self,amount: float): 
        if amount <= 0:  
            raise ValueError("Withdrawl must be greater than zero")   
        elif amount > self.__balance: 
            raise ValueError("Withdrawal cannot exceed available balance") 

    def make_transfer(self, amount: float, recipient): 
        #I'm not sure this will work 

        if amount > self.__balance: 
            raise ValueError("Insuffcient funds") 
        
        recipient.deposit(amount) 
        self.__balance -= amount   

    def get_name(self): 
        return self.name 

    def get_age(self): 
        return self.age 

    def get_account_type(self): 
        return self.account_type

    
    

        

    