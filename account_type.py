class Abstract_Account: 
    def __init__(self, name: str, code: str, description: str): 
        self.name = name 
        self.code = code  
        self.description = description

    def get_account_description(self): 
        return self.description

class AccountType(Abstract_Account):  

    def get_name(self): 
        return self.name

    def get_code(self):
        return self.code 

    def get_account_description(self): 
        return self.description

class SavingsAccount(AccountType): 
    def __init__(self, description: str): 
        self.description = description 

    def get_account_description(self):  
        return self.description   

class CurrentAccount(AccountType):  
    def __init__(self, description: str): 
        self.description = description 
    
    def get_account_description(self):  
        return self.description 



    
