from account_type import *
from customer import Customer

class Bank(): 
    def __init__(self, name: str, account_types: list[AccountType] = [], customers: list[Customer] =[]): 
        self.name = name 
        self.account_types = account_types 
        self.customers = customers  

    def add_account_type(self, code: str, name_account_str: str,): 
        name_account_str = name_account_str.capitalize()
        code = code.upper()

        if code == "SAV": 
            type_account = SavingsAccount(name_account_str,"SAV")
        elif code == "CUR":  
            type_account = CurrentAccount(name_account_str,"CUR")
        else: 
            raise ValueError(f"Incorrect code {code} given")

        self.account_types.append(type_account)


    def add_customer(self, bank): 
        customer_to_add = Customer(bank) 
        self.customers.append(customer_to_add)

    def find_customer(self, account_number: str): 
        
        for cust in self.customers: 
            num = cust.get_account_number() 

            if num == account_number: 
                found_customer = cust 
                break 
        else: 
            raise IndexError(f"Could not find customer with account number:{account_number}") 

        return found_customer  

    def delete_customers(self, account_number: str):  
        customer_to_del = self.find_customer(account_number)  
        self.customers.remove(customer_to_del)
            

    def get_account_types(self): 
        return self.account_types 


    def display_customers(self, customer_list : list[Customer] = []): 
        if customer_list == []: customer_list = self.customers 
        if not self.customers: raise TypeError(f"{self.name} has 0 customers") 
        
        for index,c in enumerate(customer_list):  
            print(f"Customer {index+1}")
            print(f"Account Number: {c.get_account_number()}")  
            print(f"Account Type: ({c.get_account_type().get_code()}) {c.get_account_type().get_name()}")
            print(f"Name: {c.get_name()}") 
            print(f"Age: {c.get_age()}") 
            print(f"Account Balance: {c.get_balance()}")  
            print("~"*15)
            
