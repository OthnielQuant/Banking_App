from random import randrange 
from account_type import *
account_bounds = [999999999,9999999999]

class Customer: 
    def __init__(self,bank):  
        self.name = input("Name of customer:") 
        if not self.name.isalpha():  
            raise ValueError("Only use letters of the alphabet")


        self.age = input("Age of Customer:") 
        if not self.age.isdigit():  
            raise ValueError("Only use postive integers for age")
        self.age = int(self.age)


        self.initial_deposit = input("Initial deposit:") 
        try: 
            self.initial_deposit = float(self.initial_deposit)  
            if self.initial_deposit <= 0: 
                raise ValueError("Initial deposit must be greater than zero")
        except ValueError: 
            raise ValueError("Initial deposit must be greater than zero and numerical") 


        #Adding the choice of what type of account the customer selects 

        list_account_types = bank.get_account_types() 

        if not list_account_types: 
            raise ValueError("No account types to select from \nPlease use '8' to add account types")
            
        for index,x in enumerate(list_account_types): 
            print(f"\nOption: {index+1}")
            print(f"Name: {x.get_name()}")
            print(f"Code: {x.get_code()}")
            print(f"Description: {x.get_account_description()}")  
            print("~"*15)

        try:
            choice = int(input("Select which option of account you want:"))  
            if choice < 0: raise ValueError
        except ValueError: 
            raise ("Please use integer values")

        try: 
            self.account_type = list_account_types[choice-1] 
        except IndexError:  
            raise "Option chosen out of range" 
          
        
        self.__account_number = str(randrange(account_bounds[0],account_bounds[1]+1))
        self.__balance = self.initial_deposit 

 

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

        self.__balance -= amount  

    def make_transfer(self, amount: float, recipient): 
        #I'm not sure this will work 

        if amount > self.__balance: 
            raise ValueError("Insuffcient funds")  

        if amount <= 0:  
            raise ValueError("Amount cannot be less than or equal to 0")

        
        recipient.deposit(amount) 
        self.__balance -= amount   

    def get_name(self): 
        return self.name 

    def get_age(self): 
        return self.age 

    def get_account_type(self): 
        
        return self.account_type

    
    

        

    