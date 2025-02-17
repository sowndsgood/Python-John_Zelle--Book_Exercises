# Automatic Teller Machine (ATM)

class User:

    def __init__(self,user_id,user_name,pin,checking_acc,savings_acc):
        self.user_id=user_id
        self.user_name=user_name
        self.pin=pin
        self.checking_acc=float(checking_acc)
        self.savings_acc=float(savings_acc)

    def check_balance(self):
        print(f"Checking account balance:{self.checking_acc}, Savings Account Balance: {self.savings_acc}")

    def withdraw_cash(self,account,cash):
        if account=="checking" and cash<=self.checking_acc:
                print(f"Balance before withdrawal in checking account:{self.checking_acc}")
                self.checking_acc-=cash
                print(f"Amount withdrawn:{cash}")
                print(f"Balance after withdrawal:{self.checking_acc}")
        elif account=="savings" and cash<=self.savings_acc:
                print(f"Balance before withdrawal in savings account:{self.savings_acc}")
                self.savings_acc-=cash
                print(f"Amount withdrawn:{cash}")
                print(f"Balance after withdrawal:{self.savings_acc}")
        else:
             print("No sufficient balance.")

    def transfer_money(self,option,cash):
        if option==1 and cash<=self.checking_acc:
            self.checking_acc -= cash
            self.savings_acc += cash
            print(f"Cash Transfered from Checking account to savings account. Balance in Checking Account:{self.checking_acc} and Savings Account:{self.savings_acc}")
        elif option==2 and cash<=self.savings_acc:
            self.savings_acc -= cash
            self.checking_acc += cash
            print(f"Cash Transfered from Savings account to checking account. Balance in Savings Account:{self.savings_acc} and Checking Account:{self.checking_acc}")

    def to_string(self):
        return f"{self.user_id},{self.user_name},{self.pin},{self.checking_acc},{self.savings_acc}"

          
def load_file(file='atm.txt'):
    users={}
    infile=open(file,'r')
    for line in infile:
        user_id,user_name,pin,checking_acc,savings_acc=line.strip().split(",")
        users[user_id]=User(user_id,user_name,pin,checking_acc,savings_acc)
    return users

def store_file(users,file='atm.txt'):
    outfile=open(file,'w')
    for user in users.values():
        print(user.to_string(),file=outfile)
    outfile.close()

def authenticate(users):
    print("Authetication Process:")
    attempts=3
    while attempts>0:
        user_id=input("Enter the User ID:")
        pin=input("Enter the PIN:")
        if user_id in users and users[user_id].pin==pin:
            print(f"Hello {users[user_id].user_name}!")
            return users[user_id]
        else:
            print("Invalid User ID or PIN")
            attempts-=1
    
def operations(user):
    
    running=True
    while running:
        print("Enter your operation:")
        print("1.Check Balance")
        print("2.Withdraw Money")
        print("3.Transfer Money")
        print("4.Quit")

        choice=int(input("Enter the choice:"))

        if choice==1:
            user.check_balance()
        elif choice==2:
            cash=int(input("Enter amount to be withdrawn:"))
            account = input("Amount to be withdrawn from:(checking/savings):").lower()
            user.withdraw_cash(account,cash)
        elif choice==3:
            cash=int(input("Enter amount to be withdrawn:"))
            option=int(input("Enter 1 if Cash need to be transfered from Checking account to savings account . Enter 2 if Cash need to be transfered from Savings account to checking account."))
            user.transfer_money(option,cash)
        elif choice==4:
            print("Quiting! Thank you!")
            break
        else:
            print("Invalid Choice. Give correct choice")

def main():
    users=load_file()
    user=authenticate(users)

    if user:
        operations(user)
        store_file(users)

if __name__=='__main__':
    main()