from abc import ABC, abstractmethod
from bank import BankAccount



class Person(ABC):
    def __init__(self, name: str, age: int, bankaccount: BankAccount, personal_home=None):
        self.name = name
        self.age = age
        self.account = bankaccount
        self.personal_home = personal_home

    def __str__(self):
        # person presentation
        return f'My name is {self.name}, I\'m {self.age} years old. \n' + \
               '{}'.format(f'And I have personal house an i\'m happy).'
                           if self.personal_home else f'I haven\'t'
                            f' personal house.\nI\'m going to make some money and by it.')

    @abstractmethod
    def make_money(self):
        raise NotImplemented

    @abstractmethod
    def buy_house(self, house):
        raise NotImplemented
