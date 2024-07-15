#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Account:
    def __init__(self,cust_id,deposit_amt):
        self.cust_id=cust_id
        self.amt=deposit_amt
        
    def deposit(self,deposit_amt):
        self.amt+=deposit_amt
        
    def withdraw(self,withdraw_amt):
        if self.amt>=withdraw_amt:
            self.amt-=withdraw_amt
        else:
            print("Eroor!")
            
    def display_amt(self):
        print(f"Current balance: {self.amt:.2f}")
    
    def get_amt(self):
        return self.amt
    
    
    
class CheckingAccount(Account):
    pass

class SavingsAccount(Account):
    pass

class BusinessAccount(Account):
    pass


def initialise_objects():
    global master_list
    amir_checking = CheckingAccount(1, 2545.6)
    ben_savings = SavingsAccount(2, 12876.9)
    ben_business = BusinessAccount(2, 14504.2)
    master_list = [
        [amir_checking, 1, 1],
        [ben_savings, 2, 2],
        [ben_business, 2, 3],
    ]


if __name__ == "__main__":
    initialise_objects()
    session_on = True

    while session_on:
        print("Welcome to 24-hour ATM service.")
        print("Insert your card.")

        cust_id = int(input("Enter your customer id number: "))

        cust_accounts = [acc for acc in master_list if acc[1] == cust_id]
        if cust_accounts:
            account_selected = False

            while not account_selected:
                print("Enter 1 for checking account")
                print("Enter 2 for savings account")
                print("Enter 3 for business account")
                account_type = int(input("Enter which account to use: "))

                selected_account = next(
                    (acc for acc in cust_accounts if acc[2] == account_type), None
                )

                if selected_account:
                    account_obj = selected_account[0]
                    account_selected = True
                    account_session_on = True

                    while account_session_on:
                        print("\nHow may I help you?")
                        print("Press 1 for balance view.")
                        print("Press 2 for withdrawals")
                        print("Press 3 to exit.")

                        action_value = int(input("Please enter your choice: "))

                        if action_value == 1:
                            account_obj.display_amt()

                        elif action_value == 2:
                            amt_to_withdraw = float(
                                input("Enter the amount to withdraw: ")
                            )
                            account_obj.withdraw(amt_to_withdraw)
                            print(f"Current balance is {account_obj.get_amt():.2f}")

                        elif action_value == 3:
                            account_session_on = False
                            print("Thank you for using the 24-hour ATM service.")
                            print("Have a pleasant day.\n")
                            print("##########################################")
                        else:
                            print("Invalid option. Please try again.")
                else:
                    print("Error. You don't have that account. Please try again.\n")
        else:
            print("Cannot find your record. Please get your card. Exiting this session...") 
        
            
        
        


# In[ ]:




