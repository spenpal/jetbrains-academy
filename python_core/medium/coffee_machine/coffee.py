# CLASS #
class CoffeeMachine:
    # MENU CHOICES
    menu_choices = {
        1: 'espresso',
        2: 'latte',
        3: 'cappuccino'
    }
    
    # MENU INFO
    espresso    = dict(recipe=dict(water=250, coffee_beans=16), cost=4)
    latte       = dict(recipe=dict(water=350, milk=75, coffee_beans=20), cost=7)
    cappuccino  = dict(recipe=dict(water=200, milk=100, coffee_beans=12), cost=6)
    
    menu = dict(espresso=espresso, latte=latte, cappuccino=cappuccino)
    
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water          = water
        self.milk           = milk
        self.coffee_beans   = coffee_beans
        self.cups           = cups
        self.money          = money
    
    def _make(self, drink):
        drink_recipe, cost = self.menu[drink]['recipe'], self.menu[drink]['cost']
        
        # Check if there is enough supply
        for ingredient, amount in drink_recipe.items():
            supply = getattr(self, ingredient)
            if supply < amount: return (False, ingredient)
        
        # Make the coffee
        self.cups -= 1
        for ingredient, amount in drink_recipe.items():
            supply = getattr(self, ingredient)
            setattr(self, ingredient, supply - amount)
        
        self.money += cost
        return True, None
               
    def buy(self):
        menu_str = ', '.join(f'{num} - {drink}' for num, drink in self.menu_choices.items())
        choice = input(f'What do you want to buy? {menu_str}, back - to main menu:\n')
        
        if choice == 'back': return
            
        success, lacking_ingredient = self._make(self.menu_choices[int(choice)])
        if success:
            print('I have enough resources, making you a coffee!')
        else:
            print(f'Sorry, not enough {lacking_ingredient}!')
        
    def fill(self):
        self.water          += int(input('Write how many ml of water the coffee machine has:\n'))
        self.milk           += int(input('Write how many ml of milk the coffee machine has:\n'))
        self.coffee_beans   += int(input('Write how many grams of coffee beans the coffee machine has:\n'))
        self.cups           += int(input('Write how many disposable cups you want to add:\n'))
        
    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
    
    def remaining(self):
        print(self)
        
    def __str__(self):
        return (
           'The coffee machine has:\n'
            f'{self.water} ml of water\n'
            f'{self.milk} ml of milk\n'
            f'{self.coffee_beans} g of coffee beans\n'
            f'{self.cups} disposable cups\n'
            f'${self.money} of money'
        )


# MAIN #
cm = CoffeeMachine(water=400, milk=540, coffee_beans=120, cups=9, money=550)

while True:
    action = input('Write action (buy, fill, take, remaining, exit):\n')
    if action == 'exit': break
    print()
    
    getattr(cm, action)() # performs given action on the coffee machine
    print()