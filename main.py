from account_type import * 
from bank import * 
from customer import * 
import shutil



columns = shutil.get_terminal_size().columns #Just to center the following text
text = input("Name of the bank:").upper()
  

bank = Bank(text)




choices = ["Add Customer","Find Customer","Deposit Money","Withdraw Money","Transfer Money","Display All Customers","Delete Customer","Add Account Type","Exit"]
while True:  
    try: 
        print(text.center(columns))
        [print(f"{index+1}. {x}") for index,x in enumerate(choices)]
        select = input("Choose your action:") 

        if select == "1": 
            bank.add_customer(bank)
        elif select == "2": 
            pass 
        elif select == "3": 
            pass 
        elif select == "4": 
            pass 
        elif select == "5":
            pass 
        elif select == "6":
            bank.display_customers()
        elif select == "7":
            pass 
        elif select == "8": 
            code = input("Savings (SAV) or Current (CUR):") 
            name = input("Name of the Account:")
            bank.add_account_type(code,name)
        elif select == "9": 
            exit("\n"+"GOODBYE".center(columns))  
        else: 
            print("Invalid command!\n") 

    except Exception as e:  
        print("\n")
        print(e)

    
    