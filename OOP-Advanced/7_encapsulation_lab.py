"""
Objectives:
  improving the student's skills in operating with the getter, setter, and deleter methods;
  improving the student's skills in creating their own exceptions.

Scenario:
  Implement a class representing an account exception,
  Implement a class representing a single bank account,
  This class should control access to the account number and account balance attributes by implementing the properties:
  it should be possible to read the account number only, not change it. In case someone tries to change the account number, raise an alarm by raising an exception;
  it should not be possible to set a negative balance. In case someone tries to set a negative balance, raise an alarm by raising an exception;
  when the bank operation (deposit or withdrawal) is above 100.000, then additional message should be printed on the standard output (screen) for auditing purposes;
  it should not be possible to delete an account as long as the balance is not zero;

Test your class behavior by:
  setting the balance to 1000;
  trying to set the balance to -200;
  trying to set a new value for the account number;
  trying to deposit 1.000.000;
  trying to delete the account attribute containing a non-zero balance.
"""


class AccountError(Exception):
    pass


class SingleBankAccount:
    def __init__(self, account_number, account_balance=0):
        self.__account_number = account_number
        self.__account_balance = account_balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_balance(self):
        return self.__account_balance

    @account_number.setter
    def account_number(self, number):
        if self.__account_number != number:
            raise AccountError(f'It is not possible to change the account number to {number} which cause to: {acc_err}')

    @account_balance.setter
    def account_balance(self, balance):
        if 0 <= balance < 100000:
            self.__account_balance = balance
        elif balance >= 100000:
            raise AccountError('Auditing is required')
        else:
            raise AccountError('It is not possible to set a negative balance')

    @account_number.deleter
    def account_number(self):
        if self.__account_balance > 0:
            raise AccountError('The account with positive balance is not the meter of removal.')
        elif self.__account_balance == 0:
            print('The account is going to be deleted')
        self.__account_number = None


single_bank_account = SingleBankAccount('CH6589144186373445432')

# setting the balance to 1000
single_bank_account.account_balance = 1000

# trying to set the balance to -200
try:
    single_bank_account.account_balance = -200
except AccountError as acc_err:
    print(f'Setting negative balance cause the error: {acc_err}')

# trying to set a new value for the account number
try:
    single_bank_account.account_number = 'SE3491688959728545147677'
except AccountError as acc_err:
    print(f'Setting new value for the account number causes the error: {acc_err}')

# trying to deposit 1.000.000
try:
    single_bank_account.account_balance += 1000000
except AccountError as acc_err:
    print(f'Depositing 1.000.000 causes the error: {acc_err}')

print(f'The account {single_bank_account.account_number} has a balance {single_bank_account.account_balance}')

# trying to delete the account attribute containing a non-zero balance
try:
    del single_bank_account.account_number
except AccountError as acc_err:
    print(f'Deleting the account attribute containing a non-zero balance causes the error: {acc_err}')

# setting the balance to 0
single_bank_account.account_balance = 0

print(f'The account {single_bank_account.account_number} has a balance {single_bank_account.account_balance}')

# trying to delete the account attribute containing a zero balance
del single_bank_account.account_number


# Setting negative balance cause the error: It is not possible to set a negative balance
# Depositing 1.000.000 causes the error: Auditing is required
# The account CH6589144186373445432 has a balance 1000
# Deleting the account attribute containing a non-zero balance causes the error: The account with positive balance is not the meter of removal.
# The account CH6589144186373445432 has a balance 0
# The account is going to be deleted
