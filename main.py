
import os
import time
import random


def clear():
  os.system("clear")
def sleep():
  time.sleep(1)
def back_to_start():
  pass

def back_to_shop():
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
      clear()
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
            money = money - 2
            attack = attack + 3
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
        back_to_shop()
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


health = 50
attack = 5
armor = 5
money = 10
inventory_value = 0
level = 0
choice = 0
worth = 0
level_exp = 0

clear()
print("Welcome slayer to this strange and dangerous world. Would you like to start?")
sleep()
start = input("y or n? ")



while start == "y":
  clear()
    
  if level_exp == 100:
    level = level + 1
    level_exp = 0
  print("Welcome to your new adventure")
  print("Armor = ",armor,". Attack = ",attack,". Money = £",money, ". Level = ",level,".")
  print("1 = Shop")
  print("2 = Adventure")
  print("3 = Leave")
  choice = int(input(": "))
  
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
          if money >= 2:
            print("Here you go!")
            money = money - 2
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
            money = money - 15
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
            money = money - 25
            attack = attack + 25
            sleep()
            back_to_shop()
      if choice == 4:
        back_to_shop()
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
            money = money - 5
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
            money = money - 20
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
            money = money - 40
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

  if choice == 2:
    clear()
    choice = 0
    print("Welcome to the map!")
    print("1 = World 1")
    print("2 = World 2")
    print("3 = HELL")
    print("4 = Back")
    choice = int(input(": "))
    if choice == 1:
      if level >= 0:
        choice_enter = input("Are you sure you want to enter? y or n ")
        while choice_enter == "y":
          clear()
          print("Something doesn't feel right?")
          sleep()
          battle = True 
          e_health = random.randint(1, 20)
          print("A MONSTER HAS APPEARED with",e_health,"HEALTH!")
          sleep()
          while battle == True:
            clear()
            e_damage = random.randint(10, 60)
            print("1 = ATTACK")
            print("2 = SKIP TURN")
            print("3 = LEAVE(SCARDEY CAT)")
            choice = int(input("WHAT WILL YOU DOOO! "))
            if choice == 1:
              print("You attack with all your strenght dealing",attack,"dammage!")
              e_health = e_health - attack
              if e_health <= 0:
                print("You have defeated the creature!!")
                worth = random.randint(1,20)
                print("You take its scale worth £",worth,"!")
                sleep()
                sleep()
                sleep()
                choice_enter = False
                battle = False
                health = 100
                level_exp = level_exp + random.randint(10,20)
                inventory_value = inventory_value + worth
                pass
            if choice == 2:
              print("The monster did ", e_damage,"damage.")
              health = health - (e_damage - armor)
              print("You have ", health,"health left!")
              sleep()
              sleep()
              sleep()
              if health <= 0:
                print("You lost")
                sleep()
                sleep()
                choice_enter = False
                battle = False
              pass
            if choice == 3:
              print("You should be ashamed!")
              sleep()
              battle = False
        
  
  if choice == 3:
    choice = 0
    print("Bye")
    break