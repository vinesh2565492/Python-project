##Bank Managament:
class account():
    def __init__(self,username,password,balance=0):
        self.username=username
        self.password=password
        self.balance=balance

class bankmanagement():
    def __init__(self):
        self.accounts={}

    def createaccount(self):
        username=input("Enter your username:")
        password=input("Enter your password:")

        if username in self.accounts:
            print("Username already exists:")
        else:
            self.accounts[username]=account(username,password,0)
            print("account created succesufully.")

    def login(self):
        username=input("Enter Your Username:")
        password=input("Enter your password:")

        if username in self.accounts:
            output=self.accounts[username]
            if output.password==password:
                print(f"Login Successfull ! Welcome,{username}")
                return output
            else:
                print("Invalid Details.")
        else:
            print("Username Not Found.")
        return None
    
    def deposit(self,account):
        amount=float(input("Enter Deposit amount:"))
        if amount > 0:
            account.balance += amount
            print(f"Deposited {amount} your balance is: {account.balance}")
        else:
            print("Invalid amount.")
    
    def withdraw(self,account):
        amount=float(input("Enter Withdrawl amount:"))
        if amount <= account.balance:
            account.balance -=amount
            print(f"withdraw {amount} and Your balance is: {account.balance}")
        else:
            print("Insufficient funds.")

    def Check_balance(self,account):
        print(f"Your current balance is :{account.balance}")

    def mini_statement(self,account):
        print("Mini statement:")
        print(f"Username:{account.username}")
        print(f"Balance: {account.balance}")

    def exit(self):
        print("Thank you for using our ATM")
        

display=bankmanagement()
while True:
    print("****Welcome to  Pythonlife Bank****")
    print("1.Create Account")
    print("2.Login")
    print("3.Exit")
    choice=input("Enter Your option:")

    if choice=='1':
        display.createaccount()

    elif choice=='2':
        account=display.login()
        if account:
            while True:
                print("\n ***Welcome to pythonlife ATM***")
                print("1.Deposit")
                print("2.Withdraw")
                print("3.Check Balance")
                print("4.Mini Statement")
                print("5.Logout")
                
                sub_choice=input("Enter Your Choice:")
                if sub_choice =='1':
                    display.deposit(account)
                    
                elif sub_choice =='2':
                    display.withdraw(account)

                elif sub_choice=='3':
                    display.Check_balance(account)

                elif sub_choice =='4':
                    display.mini_statement(account)
                elif sub_choice=='5':
                    print("Logout Successfully:")
                    break
                else:
                    print("Invalid user choice....Try Again")
    elif choice=='3':
        display.exit()
        break
    
    else:
        print("Invalid User Choice ..please Try again.")


    


                    








        



    
    



        
        
   
      
        
    

    
    
            