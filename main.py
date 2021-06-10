from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()


coffee = CoffeeMaker()

money = MoneyMachine()


machine_on=True

while machine_on:
    choice = input(f"What would you like {menu.get_items()} : ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee.report()
        money.report()

    else:
      # if choice == 'latte':
      #   menu_item = latte
      # elif choice == 'espresso':
      #   menu_item = espresso
      # else:
      #   menu_item = cappuccino
      #
      # if coffee.is_resource_sufficient(menu_item):
      #   cost = menu_item.cost
      #   if money.make_payment(cost):
      #     coffee.make_coffee(menu_item)
      #

      drink = menu.find_drink(choice)
      is_enough_ingredients = coffee.is_resource_sufficient(drink)
      is_payment_successful = money.make_payment(drink.cost)
      if is_enough_ingredients and is_payment_successful:
          coffee.make_coffee(drink)