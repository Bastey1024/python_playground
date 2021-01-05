import menu
import art
import pandas as pd
from datetime import datetime

print(art.logo)
print("Welcome to the Coffeemachine, we have Espresso, Latte or Cappucino")


def give_report():
    log.append([str(f"User Called for report"),datetime.now()])
    for i in menu.resources:
        print(f"{i.title()}: {menu.resources[i]}{menu.resources_unit[i]}")



def turn_off():
    global on
    print("Turning off the Machine - have a nice day")
    log.append([str(f'turned off the machine'),datetime.now()])

    on = "off"


def refill_automat():
    global refill
    refill = 0
    log.append([str("refilled automat"),datetime.now()])


def check_ressources(name):
    global refill
    refill = 0
    need = menu.MENU[name]['ingredients']
    left = menu.resources
    for i in need:
        if i in left:
            if left[i] > need[i]:
                continue
            else:
                print(f"Not enough {i} left, please refill")
                log.append([str(f" Please refill {i} "),datetime.now()])
                refill = 1


def process_coins(name):
    money_inserted = 0
    refund = 0
    global refill
    refill=0
    print(f"Please insert {float(menu.MENU[name]['cost'])} $")
    for i in menu.currency:
        try:
          k = int(input(f"How many {i} (worth {menu.currency[i]}$) you insert?"))
          money_inserted += (k * menu.currency[i])
        except:
          print("Please only insert a number of coins")
          pass
    if money_inserted > menu.MENU[name]['cost']:
        refund = money_inserted - menu.MENU[name]['cost']
        menu.resources["money"] += menu.MENU[name]['cost']
        print(f"Thank you, here is your Change {round(refund,2)}$")
    elif money_inserted < menu.MENU[name]['cost']:
        print(f"Not enough money, please give enough money ( {menu.MENU[name]['cost']} $ )")
        print(f"Here is your money {money_inserted} $")
        refill=1


def make(name):
    need = menu.MENU[name]['ingredients']
    left = menu.resources
    menu.resources = {key: left[key] - need.get(key, 0) for key in left}
    log.append([str(f"{name} sold"),datetime.now()])
    print(f"Here is your tasty {name}, i wish you a nice day")


def maintenance_function():
  print (art.maintenance)
  global maintenance
  maintenance = 1


def user_choice(user_wants):
    user_wants=user_wants.lower().strip()

    try:
      if user_wants == "maintenance":
        maintenance_function()
      elif maintenance == 1:
        if user_wants == "off":
          turn_off()
        elif user_wants == "report":
          give_report()
        elif user_wants == "refill":
          refill_automat()
          give_report()
        elif user_wants=="log":
          df=pd.read_csv("coffe_log.csv")
          print(df)
      elif user_wants not in menu.MENU:
          print(f"Sorry we dont have {user_wants}, we only have {', '.join([i for i in menu.MENU.keys()]).title()}")
      else:
          user_wants = user_wants.lower().strip()

          check_ressources(user_wants)
          if refill == 0:
              process_coins(user_wants)
              if refill == 0:
                make(user_wants)
              else:
                user_choice(input("What do you want?"))
          else:
              print("Please call maintenance for refilling the automat")
    except:
      pass


on = "on"
refill = 0
maintenance = 0
log = []

while on == "on":
    user_choice(input("What do you want?"))
    df = pd.DataFrame(log, columns=['order_name','time'])
    df.to_csv("coffe_log.csv",mode='a')
