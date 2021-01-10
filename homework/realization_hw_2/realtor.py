import random
import time
from bank import BankAccount
from collections import namedtuple
from faker import Faker

# creation function which is class factory
House = namedtuple('House', 'address area cost discount')
# setting default value for 'class House'
House.__new__.__defaults__ = (None, None, None, False)


class SingletonDecorator(object):
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


@SingletonDecorator
class Realtor:
    PERSONAL_DATA = Faker()

    def __init__(self, name=PERSONAL_DATA.name(), age=30):
        self.name = name
        self.age = age
        # creation persons with random balance
        self.houses = [
            House(self.PERSONAL_DATA.address(),
                  random.randint(100, 500),
                  random.randint(15_000, 100_000),
                  random.choice([True, False]))
            for _ in range(random.randint(6, 10))
        ]
        self.account = BankAccount(self, balance=40_000)

    @property
    def presentation_house(self):
        print(f'It\'s a pleasure to meet you!!!\nMy name is {self.name}')
        time.sleep(0.5)
        print(f'and I\'m the only realtor in this city.\n')
        time.sleep(0.5)
        print(f'This is all houses which are on sale in the city:')
        time.sleep(0.5)
        for house in self.houses:
            print(f'\nHouse number {self.houses.index(house) + 1}\n'
                  f'address: {house.address}\n'
                  f'area: {house.area}\n'
                  f'coast: {house.cost}')
            time.sleep(0.9)

    def discaunt(self, house):
        if house.discount:
            real_price = house.cost
            new_price = real_price - real_price * 0.1
            print(f'---DISCOUNT---DISCOUNT---DISCOUNT---\n'
                  f'Yes I can do some discount for this house and it is {real_price * 0.1:.2f}!\n'
                  f'---DISCOUNT---DISCOUNT---DISCOUNT---\n')
            return house._replace(cost=new_price)
        print('\t---AVOIDANCE---AVOIDANCE---AVOIDANCE---\n'
              'Sorry, but discount is already include in the price of this house.'
              '\t---AVOIDANCE---AVOIDANCE---AVOIDANCE---\n')
        return house

    def thief_posibility(self, costumer):
        self.account.earn_money = costumer.account._balance
        costumer.account.balance = 0
        print('Money was stole.\n'
              '--THIEF--THIEF--THIEF--THIEF--THIEF--THIEF\n')
