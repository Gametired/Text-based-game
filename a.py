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