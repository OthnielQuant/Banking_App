from account_type import * 
from bank import * 
from customer import * 
import shutil



columns = shutil.get_terminal_size().columns #Just to center the following text
text = input("Name of the bank:").upper()
  

bank = Bank(text)

def add(): 
    bank.add_customer(bank) 

def find():
    account_number = input("Enter account number:")
    found_customer = bank.find_customer(account_number) 
    bank.display_customers([found_customer]) 

def add_account_type(): 
    code = input("Savings (SAV) or Current (CUR):") 
    name = input("Name of the Account:")
    bank.add_account_type(code,name) 

def deposit():
    account_number = input("Account number:").strip()
    depo_amount = input("Deposit amount:") 

    try: 
        depo_amount = float(depo_amount)  
    except: 
        raise ValueError(f"Invalid amount {depo_amount}")

    found_cust_depo = bank.find_customer(account_number) 
    found_cust_depo.deposit(depo_amount)
    print(f"Deposited sum of {depo_amount} to account number {account_number}") 

def withdraw(): 
    account_number = input("Account number:").strip()
    withdraw_amount = input("Withdraw amount:").strip()

    try: 
        withdraw_amount = float(withdraw_amount) 
    except: 
        raise ValueError("Enter a number please")

    found_cust_withdraw = bank.find_customer(account_number) 
    found_cust_withdraw.withdraw(withdraw_amount)
    print(f"Withdrew sum of {withdraw_amount} from account number {account_number}")
    
def transfer(): 
    if bank.get_length_customers() < 2: 
        raise IndexError("Bank does not have enough customers to make transfer") 

    own_acc_num = input("Remitter Account Number:").strip()
    rec_acc_num = input("Recipient Account Number:").strip() 
    amount = input("Amount to transfer:").strip() 

    try: 
        amount = float(amount)
    except: 
        raise ValueError("Amount must be numerical") 

    own_customer = bank.find_customer(own_acc_num)  
    rec_customer = bank.find_customer(rec_acc_num)  

    own_customer.make_transfer(amount,rec_customer) 

    print("Transfer successful")
    
def delete(): 
    if bank.get_length_customers() < 1: 
        raise IndexError("No customers to delete") 

    acc_to_del = input("Account Number:").strip()

    cust_to_del = bank.find_customer(acc_to_del) 

    bank.display_customers([cust_to_del]) 

    print("Are you sure you want to delete this customer?".upper())
    choice = input("Press Y or any other character to escape:").upper().strip()

    if choice == "Y": 
        bank.delete_customers(acc_to_del) 
        print("Customer deleted successfully")


choices = ["Add Customer","Find Customer","Deposit Money","Withdraw Money","Transfer Money","Display All Customers","Delete Customer","Add Account Type","Exit"]
while True:  
    try: 
        print(text.center(columns))
        [print(f"{index+1}. {x}") for index,x in enumerate(choices)]
        select = input("Choose your action:") 

        if select == "1": 
            add()
        elif select == "2": 
            find()
        elif select == "3": 
            deposit()
        elif select == "4": 
            withdraw()
        elif select == "5":
            transfer()
        elif select == "6":
            bank.display_customers()
        elif select == "7":
            delete()
        elif select == "8": 
            add_account_type()
        elif select == "9": 
            exit("\n"+"GOODBYE".center(columns))  
        else: 
            print("Invalid command!\n") 

    except Exception as e:  
        print("\n")
        print(e)

    
    