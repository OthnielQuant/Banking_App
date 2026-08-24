from account_type import AccountType 
from customer import Customer

class Bank(): 
    def __init__(self, name: str, account_types: list[AccountType], customers: list[Customer]): 
        self.name = name 
        self.account_types = account_types 
        self.customers = customers 

    def add_account_type(self, AccountType): 
        pass 

    def add_customer(self, Customer_person: Customer): 
        self.customers.append(Customer_person)

    def find_customer(self, account_number: str): 
        pass