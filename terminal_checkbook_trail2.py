#!/usr/bin/env python
# coding: utf-8

# In[15]:


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
        # Your main code goes here, which will only execute if authentication is successful.
       # greeting message to user
        print()
        print('~~~ Welcome to your terminal checkbook! ~~~')
        print()


# In[4]:


#imports
import os
import subprocess
import locale
#locale.setlocale(locale.LC_ALL, '')


# In[4]:


# shows me all the files in my current directory
# os.listdir()


# In[61]:


with open('my_checkbook.txt', 'w') as f:
    f.write('500')


# In[62]:


filename = 'my_checkbook.txt'


# In[95]:


#1 balance function
def balance(filename):
    with open(filename) as f:
        line = f.read().split('\n')
        balance = 0
        for x in line:
            balance += float(x)
        return round(balance, 2)


# In[96]:


#2 debit function
def debit(debit_prompt):
    with open(filename, 'a') as f:
        if float(debit_prompt) > balance(filename):
            print('balance is too low for this debit')
            f.write('\n' + f'-{round(float(debit_prompt), 2)}')
        else:
            f.write('\n' + f'-{round(float(debit_prompt), 2)}')


# In[97]:


#3 credit function
def credit(credit_prompt):
    with open(filename, 'a') as f:
        f.write('\n' + f'{round(float(credit_prompt), 2)}')


# In[ ]:


def userchoice():
    prompt = input('What would you like to do?\n\n\
    1) view current balance\n\
    2) record a debit (withdraw)\n\
    3) record a credit (deposit)\n\
    4) exit\n')
    return prompt
#print(prompt)
prompt = userchoice()


# In[109]:


while prompt not in ['1', '2', '3', '4'] and prompt != '4':
    print(f'Invalid choice: {prompt}')
    prompt = userchoice()
while prompt != '4':
    # 1: view current balance
    if prompt == '1':
        print(f'Your choice?: {prompt}')
        # balance function goes here
        print()
        print(f'Your current balance is ${round(balance(filename), 2)}.')
        print()
        prompt

    # 2: debit
    elif prompt == '2':
        print(f'Your choice?: {prompt}')
        print()
        debit_prompt = input('How much is the debit? ')
        # debit function goes here
        debit(debit_prompt)
        if balance(filename) >= float(debit_prompt):
            print(f'Withdrew ${round(float(debit_prompt), 2)}, new balance is ${round(balance(filename), 2)}.')
        else:
            balance(filename) < float(debit_prompt)
            
            print(f'Withdrew ${round(float(debit_prompt), 2)}, new balance is ${round(balance(filename), 2)}.')
        
        print()
        prompt     

    # 3: credit
    elif prompt == '3':
        print(f'Your choice?: {prompt}')
        print()
        credit_prompt = input('How much is the credit? ')
        # credit function goes here
        credit(credit_prompt)
        print(f'Deposited ${round(float(credit_prompt), 2)}, new balance is ${round(balance(filename), 2)}.')
        print()
        prompt
        
    else:
        print('Something went wrong!')
        break
        prompt

    prompt = userchoice()


# In[104]:


#4 exit
print(f'Your choice?: {prompt}')
print()
print('Thanks, have a great day!')

