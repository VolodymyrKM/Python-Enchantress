import random
from exceptions import *
from datetime import datetime


class BankAccount:
    """
     initialization of the instance BankAccount with the attributes,
     personal_data takes as the parameter the instance of the class person:
     almost each parameter unpuked from human instance to the attributes.
     this class provides simple access to the data of the person as a password check,
     and also this class provides two maine human life possibility of earning money ad spending money
    """
    TIME_BANK_ACTION = datetime.now().strftime("%b %d %Y %H:%M:%S")

    # creation bank account some person
    def __init__(self, person, *, balance=0,  wisa_password=0000):
        self._person_data = person
        self._person_name = self._person_data.name
        self._age = self._person_data.age
        self._ssn = random.randint(34567897653, 2345775323456)  # social security number
        self._balance = balance
        self._wisa_password = wisa_password

    @staticmethod
    def checker(value):
        if not isinstance(value, (int, float)):
            raise MoneyError()
        return value

    @property
    def balance(self):
        # implementation simple bank access to the data of person
        if self._balance == 0:
            raise ZeroBalance('Insufficient funds.')
        elif self._balance < 0:
            raise CreditMinusBalance('Your accounts overdrawn, you should go to '
                                     'work to earn some money.')
        # checking password person card
        check_pass = int(input('Enter password: '))
        if isinstance(check_pass, (int, float)) \
                and len(str(check_pass)) <= 4 \
                and check_pass == self._wisa_password:
            return self._balance
        else:
            raise WrongPassword('Your password should be integer numbers'
                                'and length must be at least four numbers')

    @balance.setter
    def balance(self, money):
        BankAccount.checker(money)
        self._balance = money
        print(f'\n-----------TRANSACTION MESSAGE -----------\n'
              f'Dear {self._person_name}. Balance was set: {self._balance}\n'
              f'-----------TRANSACTION MESSAGE -----------\n')

    def transfer_money(self, money):
        # method to spend money
        BankAccount.checker(money)
        self._balance -= money
        print(f'\n-----------TRANSACTION MESSAGE -----------\n'
              f'Dear {self._person_name}! At {BankAccount.TIME_BANK_ACTION} you transferred {money}.\n'
              f'Now your balance: {self._balance}\n'
              f'-----------TRANSACTION MESSAGE ------------\n')

    # decorating method transfer_money to setter
    transfer_money = property(fset=transfer_money)

    def earn_money(self, money):
        # method to earn money
        BankAccount.checker(money)
        self._balance += money
        print(f'\n-----------TRANSACTION MESSAGE -----------\n'
              f'Dear {self._person_name}! At {BankAccount.TIME_BANK_ACTION}\n'
              f'your balance is replenished at {money}.\n'
              f'Now your balance: {self._balance}\n'
              f'\n-----------TRANSACTION MESSAGE -----------')

    earn_money = property(fset=earn_money)
