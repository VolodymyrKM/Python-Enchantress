import random
import time
import person
import bank
import realtor
from faker import Faker
from realtor import SingletonDecorator


class Human(person.Person):
    """
    Initialization of the instance human inherited from the abstract class Person,
    and implement it method.
    the human has two method make money which is provides earn and transfer money
    to the personal balance and method by house
    """
    def __init__(self, name, age, bankaccount, personal_home=None):
        super().__init__(name, age, bankaccount, personal_home)

    def make_money(self):
        self.do_some_job = random.randint(1500, 5000)
        print('\n---WORK---WORK----WORK----WORK---WORK---WORK---\n'
              'Doing my necessary job to by my house...\n'
              '---WORK---WORK----WORK----WORK---WORK---WORK---\n')
        self.account.earn_money = self.do_some_job

    def buy_house(self, house):
        if house.discount and self.account._balance >= house.cost:
            self.personal_home = house
            print(f'\n---CONGRATULATION---CONGRATULATION---CONGRATULATION----\n'
                  f'I\'m very happy I bought this house of my dream.\n'
                  f'Address: {house.address}\n'
                  f'Area: {house.area}')
            return True
        else:
            print(f'\nI should work harder to earn more\n'
                  f'money to by this house for {house.cost}...\n')
            return house


@SingletonDecorator
class HouseAuction:
    """
    Initialisation of class HouseAuction with the attributes person which randomly create persons
    and add person attribute account.
    Also this class provide one maine method start_auction.
    """



    PERSONAL_DATA = Faker()

    def __init__(self):

        self.person = [Human(self.PERSONAL_DATA.name(), random.randint(27, 67), None) for _ in
                       range(random.randint(2, 4))]
        for human in self.person:
            human.account = bank.BankAccount(human, balance=random.randint(50_000, 100_000))
        self.realtor = realtor.Realtor()

    def start_auction(self):
        print(f'Present people on the auction {len(self.person)}\n')
        self.realtor.presentation_house

        while len(self.person) != 0:
            if len(self.realtor.houses) == 0:
                print('Now we have\'t houses to sel you...')
                break
            house = random.choice(self.realtor.houses)
            print(f'Auction with house: on the address\n{house.address}\n'
                  f'with area: {house.area}, which is cost {house.cost}')
            time.sleep(0.5)
            person = random.choice(self.person)
            if person.buy_house(house):
                if not random.randint(2, 2) % 2:
                    self.realtor.discaunt(house)
                if not random.choice((list(range(0, 100, 3)) + list(range(0, 10, 2)))) % 2:
                    self.realtor.thief_posibility(person)
                    continue
                person.account.transfer_money = house.cost
                self.realtor.account.earn_money = house.cost
                person.personal_home = house
                self.realtor.houses.pop(self.realtor.houses.index(house))
                self.person.pop(self.person.index(person))
                print(f'Happy {person.name} left auction ')
                time.sleep(0.5)
                print(f'Numbers of house: {len(self.person)} left.')
            else:
                person.make_money()
        print('The auction is over....\n'
              '-------------------------THE END------------------------------')


if __name__ == '__main__':
    auction = HouseAuction()
    ### PUSH THE BUTTON TO START AUCTION
    auction.start_auction()