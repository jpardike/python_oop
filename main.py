class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'hi, my name is {self.name}')

    def create_post(self, content):
        print(f'User: {self.name} created post: {content}')

new_user = User('Socrates')

# print(new_user.name)
# print(type(new_user))
# new_user.create_post('collecting stamps')

class BankAccount:
    def __init__(self, type_of_account='checking'):
        self.type_of_account = type_of_account
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

# socrates_bank_account = BankAccount()
# print(socrates_bank_account.type_of_account)
# print(socrates_bank_account.get_balance())
# socrates_bank_account.deposit(100)
# print(socrates_bank_account.get_balance())

class Pizza_parlor:
    def __init__(self, company_name):
        self.company_name = company_name
        self.pizzas_made = 0
        self.pizzas_sold = 0

    def make_pizza(self, amount_of_pizzas):
        self.pizzas_made += amount_of_pizzas

    def sell_pizza(self, amount_of_pizzas):
        if amount_of_pizzas > self.pizzas_made:
            print('You do not have enough pizzas made')
            return
        else:
            self.pizzas_sold += amount_of_pizzas
            self.pizzas_made -= amount_of_pizzas

# new_pizza_place = Pizza_parlor('Socrates Pizzas')
# new_pizza_place.make_pizza(4)
# print(new_pizza_place.pizzas_made)
# new_pizza_place.sell_pizza(4)
# print(new_pizza_place.pizzas_made)

class Phone:
    def __init__(self, phone_number):
        self.number = phone_number

    def make_call(self, other_number):
        print(f'Calling {other_number} from {self.number}')

joanns_phone = Phone('555-555-5555')

joanns_phone.make_call('333-333-3333')

class SmartPhone(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)

        self.apps = ['email', 'calculator', 'clock']

    def install_app(self, app_name):
        self.apps.append(app_name)
        return self.apps

socrates_smart_phone = SmartPhone('222-222-2222')
print(socrates_smart_phone)
print(socrates_smart_phone.number)
socrates_smart_phone.make_call('123-123-1234')

print(socrates_smart_phone.apps)
print(socrates_smart_phone.install_app('news'))

class Dog:
    def __init__(self, name):
        self.name = name
        self.good_dog = True

    def __str__(self):
        return f'And {self.name} was his namo'

milo = Dog('Milo')

print(milo.name)

print(milo)