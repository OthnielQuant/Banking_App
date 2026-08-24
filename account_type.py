class Abstract_Account: 
    def __init__(self): 
        pass 

    def get_account_description(self): 
        pass

class AccountType(Abstract_Account):  

    def __init__(self, name: str, code: str): 
        self.name = name 
        self.code = code 

    def get_name(): 
        pass 

    def get_code():
        pass  

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



    
