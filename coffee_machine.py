# Write your code here
class CoffeMachine():
    main_states = ['buy', 'fill', 'take', 'remaining', 'exit']

    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.state = 'main'
        self.state_fill = 'water'

    def print_status(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

    def make_coffee(self, money_l, water_l, milk_l, coffee_l):
        self.money += money_l
        self.water -= water_l
        self.milk -= milk_l
        self.coffee -= coffee_l
        self.cups -= 1

    def check_resources(self, water_l, milk_l, coffee_l):
        if self.water < water_l:
            return "water"
        elif self.milk < milk_l:
            return "milk"
        elif self.coffee < coffee_l:
            return "coffee"
        elif self.cups < 1:
            return "cups"
        else:
            return "ok"

    def buy(self, choice):
        if choice == 'back':
            return
        choice = int(choice)
        if choice == 1:
            check = self.check_resources(250, 0, 16)
            if check == 'ok':
                self.make_coffee(4, 250, 0, 16)
            else:
                print("Sorry, not enough " + check + "!")
        elif choice == 2:
            check = self.check_resources(350, 75, 20)
            if check == 'ok':
                self.make_coffee(7, 350, 75, 20)
            else:
                print("Sorry, not enough " + check + "!")
        elif choice == 3:
            check = self.check_resources(200, 100, 12)
            if check == 'ok':
                self.make_coffee(6, 200, 100, 12)
            else:
                print("Sorry, not enough " + check + "!")

    def fill(self, menu, quantity):
        if menu == 'water':
            self.water += int(quantity)
        elif menu == 'milk':
            self.milk += int(quantity)
        elif menu == 'coffee':
            self.coffee += int(quantity)
        elif menu == 'cups':
            self.cups += int(quantity)

    def take(self):
        print("I gave you $" + str(self.money))
        print("")
        self.money = 0

    def print_menu(self):
        if self.state == 'main':
            return "Write action (buy, fill, take, remaining, exit):"
        elif self.state == 'buy':
            return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
        elif self.state == 'fill':
            if self.state_fill == 'water':
                return "Write how many ml of water do you want to add:"
            if self.state_fill == 'milk':
                return "Write how many ml of milk do you want to add:"
            if self.state_fill == 'coffee':
                return "Write how many grams of coffee beans do you want to add:"
            if self.state_fill == 'cups':
                return "Write how many disposable cups of coffee do you want to add:"

    def get_input(self, input_string):
        if self.state == 'main':
            if input_string in CoffeMachine.main_states:
                if input_string == 'remaining':
                    self.print_status()
                    self.state = 'main'
                elif input_string == 'take':
                    self.take()
                    self.state = 'main'
                else:
                    self.state = input_string
            else:
                self.state = 'main'
        elif self.state == 'buy':
            self.buy(input_string)
            self.state = 'main'
        elif self.state == 'fill':
            if self.state_fill == 'water':
                self.fill('water', input_string)
                self.state_fill = 'milk'
            elif self.state_fill == 'milk':
                self.fill('milk', input_string)
                self.state_fill = 'coffee'
            elif self.state_fill == 'coffee':
                self.fill('coffee', input_string)
                self.state_fill = 'cups'
            elif self.state_fill == 'cups':
                self.fill('cups', input_string)
                self.state_fill = 'water'
                self.state = 'main'

coffe_machine = CoffeMachine()

while True:
    print(coffe_machine.print_menu())
    coffe_machine.get_input(input())
    if coffe_machine.state == 'exit':
        break