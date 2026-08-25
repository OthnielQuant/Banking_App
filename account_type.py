class Abstract_Account: 
    def __init__(self, name: str, code: str): 
        self.name = name 
        self.code = code  
        self.description = input("Give a brief description of the account:").strip()

    def get_account_description(self): 
        return self.description

class AccountType(Abstract_Account):  
    def __int__(self):
        super().__init__()

    def get_name(self): 
        return self.name

    def get_code(self):
        return self.code 

    def get_account_description(self): 
        return self.description

class SavingsAccount(AccountType): 
    def __int__(self):
        super().__init__()  

    def get_account_description(self):  
        return self.description   

class CurrentAccount(AccountType): 
    def __init__(self): 
        super().__init__()  

    def get_account_description(self):  
        return self.description 



    
