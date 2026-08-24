from account_type import * 
from bank import * 
from customer import * 
import shutil



columns = shutil.get_terminal_size().columns #Just to center the following text
text = input("Name of the bank:").upper()
  

bank = Bank(text)




choices = ["Add Customer","Find Customer","Deposit Money","Withdraw Money","Transfer Money","Display All Customers","Delete Customer","Exit"]
while True:  
    try: 
        print(text.center(columns))
        [print(f"{index+1}. {x}") for index,x in enumerate(choices)]
        select = input("Choose your action:") 

        if select == "1": 
            bank.add_customer()
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
            exit("\n"+"GOODBYE".center(columns))  
        else: 
            print("Invalid command!\n") 

    except Exception as e:  
        print("\n")
        print(e)

    
    