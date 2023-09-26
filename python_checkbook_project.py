#!/usr/bin/env python
# coding: utf-8

# In[4]:


import getpass

# Define the correct username and password
correct_username = "Jorge"
correct_password = "Tobias2024"

def authenticate():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed. Access denied.")
        return False

if __name__ == "__main__":
    if authenticate():
        print()
        print('~~~~~ Welcome to your secure terminal checkbook! ~~~~~')
        print()
                
        import os
        import subprocess
        import locale
        from os import path
        
        # Check if the file exists and initialize balance
        filename = 'my_checkbook.txt'
        if not os.path.isfile(filename):
            with open(filename, "w") as f:
                f.write("0.0")
        
        #1 balance function
        def balance(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()
                non_empty_lines = [line.strip() for line in lines if line.strip()]
                if non_empty_lines:
                    balance = sum(float(line) for line in non_empty_lines)
                    return round(balance, 2)
                else:
                    return 0.0
        

        #0 balance history function added
        def view_balance_history(filename):
            try:
                with open(filename, 'r') as f:
                    print("Transaction History:")
                    transactions = f.readlines()
                    for transaction in transactions:
                        print(transaction.strip())
            except FileNotFoundError:
                print("No transaction history available.")    
            
        #2 debit function
        #def debit(debit_prompt):
        #    with open(filename, 'a') as f:
        #        if float(debit_prompt) > balance(filename):
        #            print('WARNING: Negative balance as a result!')
        #            
        #            f.write('\n' + f'-{round(float(debit_prompt), 2)}')
        #        else:
        #            f.write('\n' + f'-{round(float(debit_prompt), 2)}')
        # added a confirmation to go negative on the current balance
        def debit(debit_prompt):
            with open(filename, 'a') as f:
                if float(debit_prompt) > balance(filename):
                    print('WARNING: Negative balance as a result!')
                    confirmation = input('Do you want to continue with the withdrawal? (yes/no): ')
                    if confirmation.lower() == 'yes':
                        f.write('\n' + f'-{round(float(debit_prompt), 2)}')
                        print(f'Withdrawal ${round(float(debit_prompt), 2)} successful. \n~~~~~~~OVERDRAFT WARNING~~~~~~~')
                        print()
                    else:
                        print(f'Withdrawal ${round(float(debit_prompt), 2)} canceled, your current balance is ${round(balance(filename), 2)}')   
                    
                else:
                    f.write('\n' + f'-{round(float(debit_prompt), 2)}')
                    print('Withdrawal successful.')
                    
        #3 credit function
        def credit(credit_prompt):
            with open(filename, 'a') as f:
                f.write('\n' + f'{round(float(credit_prompt), 2)}')
                print('Deposit successful.')
                print()
                
        def userchoice():
            prompt = input('What would you like to do?\n\n\
            0) view tansaction history\n\
            1) view current balance\n\
            2) record a debit (withdraw)\n\
            3) record a credit (deposit)\n\
            4) exit\n')
            return prompt
        #print(prompt)
        prompt = userchoice()
        
        #while prompt not in ['1', '2', '3', '4'] and prompt != '4':
        #    print(f'Invalid choice: {prompt}')
        #    prompt = userchoice()
        #while prompt != '4':
        #Added option 0 as to view the balance history
        
        # 1: view current balance
        while prompt not in ['0', '1', '2', '3', '4'] and prompt != '4':
            print(f'Invalid choice: {prompt}')
            prompt = userchoice()
        while prompt != '4':
            if prompt == '0':
                print(f'Your choice: {prompt}')
                view_balance_history(filename)
                print()
            elif prompt == '1':
                print(f'Your choice: {prompt}')
                print()
                print(f'Your current balance is ${round(balance(filename), 2)}')
                print()
                prompt
            
            # 2: debit
            elif prompt == '2':
                print(f'Your choice: {prompt}')
                print()
                debit_prompt = input('How much is the debit? $')
                debit(debit_prompt)
                if balance(filename) >= float(debit_prompt):
                    print(f'Withdrew ${round(float(debit_prompt), 2)}, new balance is ${round(balance(filename), 2)}')                    

# below was the way i was running it but would always say withdrew X amount, even if i canceled the debit.
#                else:
#                    print(f'Withdrew ${round(float(debit_prompt), 2)}, new balance is ${round(balance(filename), 2)}.')
                
                print()
                prompt     
        
            # 3: credit
            elif prompt == '3':
                print(f'Your choice: {prompt}')
                print()
                credit_prompt = input('How much is the credit? $')
                credit(credit_prompt)
                print(f'Deposited ${round(float(credit_prompt), 2)}, new balance is ${round(balance(filename), 2)}')
                print()
                prompt
                
            else:
                print('Something went wrong!')
                break
                prompt
        
            prompt = userchoice()
        
        #4 exit
        print(f'Your choice?: {prompt}')
        print()
        print('Thanks, have a great day!')

