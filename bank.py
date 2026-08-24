import bisect 
from account_type import AccountType 
from customer import Customer

class Bank(): 
    def __init__(self, name: str, account_types: list[AccountType], customers: list[Customer]): 
        self.name = name 
        self.account_types = account_types 
        self.customers = customers.sort(key=lambda x: int(x.get_account_number()))  

    def add_account_type(self): 
        self.name_account = input("Name of New Account Type:") 

        if not self.name_account.isalpha():  
            raise ValueError("Only use letters of the alphabet")

        self.code_account = input("Code of New Account Type:").strip().upper()
        self.description = input("Brief description of Account Type:") 

        print("Creating Account Type...")

        self.__new_account_type = AccountType(self.name_account,self.code_account,self.description)

        self.account_types.append(self.__new_account_type)


    def add_customer(self, Customer_person: Customer): 
        self.name_customer = input("Name of customer:") 

        if not self.name_customer.isalpha():  
            raise ValueError("Only use letters of the alphabet")

        self.age_customer = input("Age of Customer:") 

        if not self.age.isdigit():  
            raise ValueError("Only use postive integers for age")

        self.age = int(self.age)
        self.initial_deposit = input("Initial deposit:")

        try: 
            self.initial_deposit = float(self.initial_deposit)  
            if self.initial_deposit <= 0: 
                raise ValueError("Initial deposit must be greater than zero")
        except ValueError: 
            raise ValueError  

        self.account_type_customer = input("Enter code of account type:").strip().upper()

        #Search for account type 

        for x in self.account_types:  
            if x.get_code() == self.account_type_customer: 
                found_type = x
                break 
        else: 
            raise IndexError("Could not find code for valid account type")

        


        print("Adding customer...")

        customer_to_add = Customer(self.name_customer,self.age_customer,self.initial_deposit,found_type)
           

        bisect.insort_right(self.customers, customer_to_add, key=lambda x: int(x.get_account_number()))

        print("Customer succesfully added")

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

        print("Are you sure you want to delete...") 
        self.display_customers(customer_to_del)  

        choice = input("Press Y to delete and any other character to exit deletion:")

        if choice == "Y": 
            self.customers.remove(customer_to_del)
            print("Deletion successful")  
            return None 

        print("Deletion aborted")

        


    def display_customers(self, customer_list : list[Customer] = self.customers): 

        for index,c in enumerate(customer_list):  
            print(f"Customer {index+1}")
            print(f"Account Number: {c.get_account_number()}")  
            print(f"Account Type: {c.get_account_type()}")
            print(f"Name: {c.get_name()}") 
            print(f"Age: {c.get_age()}") 
            print(f"Account Balance: {c.get_balance()}")  
            print("~"*15)
            
