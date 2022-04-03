import os
import time

def clear():
  os.system("clear")
def sleep():
  time.sleep(1)
def back_to_start():
  pass
def back_to_shop():
  if choice == 1:
  clear()
  choice = 0
  print("Welcome to the shop!")
  print("1 = Armor shop")
  print("2 = Weapon shop")
  print("3 = sell")
  print("4 = Back")
  choice = int(input(": "))
  if choice == 4:
      pass
  if choice == 3:
      choice = 0
      print("Would you like to sell your inventory, it is worth £",inventory_value,".")
      choice = input("y or n ")
      if choice == "y":
        money = money + inventory_value
        inventory_value = 0
        print("Thanks!")
        sleep()
        back_to_shop()
  if choice == 2:
      choice = 0
      print("Welcome to the weapon shop, mate!")
      print("1 = Wood Hoe")
      print("2 = Stone Axe")
      print("3 = Iron Sword")
      print("4 = Back")
      choice = int(input(": "))
      if choice == 1:
        choice = 0
        print("Alright, the price is 2 quid")
        choice = input("y or n ")
        if choice == "y":
          if money >= 5:
            print("Here you go!")
            money -= 5
            attack = attack + 5
            back_to_shop()
          else:
            print("Sorry you do not have enough money!")
            sleep()
            sleep()
            back_to_shop()
      if choice == 2:
        choice = 0
        print("Price = £15")
        print("Do you want to purchase?")
        choice = input("y or n ")
        if choice == "y":
          if money >= 10:
            print("Here you go!")
            attack = atack + 10
            sleep()
            back_to_shop()
          else:
            print("Not enough money!")
            back_to_shop()
      if choice == 3:
        print("Price = £25")
        choice = input("Would you like to buy, y or n? ")
        if choice == "y":
          if money >= 25:
            print("Here ya go, mate!")
            attack = attack + 25
            sleep()
            back_to_shop()
      if choice == 4:
        pass
  if choice == 1:
      clear()
      choice = 0
      print("Wlcome to me armor shop!")
      print("1 = Stone")
      print("2 = Iron")
      print("3 = Diamond")
      print("4 = Back")
      choice = int(input(": "))
      if choice == 1:
        print("Price = £5")
        print("Would you like to buy?")
        choice = input("y or n ")
        if choice == "y":
          if money >= 5:
            print("Here you go!")
            money -= 5
            armor = armor + 5
            back_to_shop()
          else:
            print("Sorry you do not have enough money!")
            sleep()
            sleep()
            back_to_shop()
      if choice == 2:
        print("Price = £20")
        print("Would you like to buy?")
        choice = input("y or n ")
        if choice == "y":
          if money >= 20:
            print("Here you go!")
            money -= 20
            armor = armor + 10
            back_to_shop()
          else:
            print("Sorry you do not have enough money!")
            sleep()
            sleep()
            back_to_shop()
      if choice == 3:
        print("Price = £40")
        print("Would you like to buy?")
        choice = input("y or n ")
        if choice == "y":
          if money >= 40:
            print("Here you go!")
            money -= 40
            armor = armor + 25
            back_to_shop()
          else:
            print("Sorry you do not have enough money!")
            sleep()
            sleep()
            back_to_shop()
      if choice == 4:
        print("BYE!")
        sleep()
        back_to_shop()

def back_to_adventures():
  print("")