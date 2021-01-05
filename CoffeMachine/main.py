import menu
import art

print(art.logo)
print("Welcome to the Coffeemachine, we have Espresso, Latte or Cappucino")


def give_report():
    for i in menu.resources:
        print(f"{i.title()}: {menu.resources[i]}{menu.resources_unit[i]}")


def turn_off():
    global on
    print("Turning off the Machine - have a nice day")
    on = "off"


def refill_automat():
    global refill
    refill = 0


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
                refill = 1


def process_coins(name):
    money_inserted = 0
    refund = 0
    print(f"Please insert {float(menu.MENU[name]['cost'])} $")
    for i in menu.currency:
        k = int(input(f"How many {i} (worth {menu.currency[i]}$) you insert?"))
        money_inserted += (k * menu.currency[i])
    if money_inserted > menu.MENU[name]['cost']:
        refund = money_inserted - menu.MENU[name]['cost']
        menu.resources["money"] += menu.MENU[name]['cost']
        print(f"Thank you, here is your {refund}$")
    elif money_inserted < menu.MENU[name]['cost']:
        print(f"Not enough money, please give enough money ( {menu.MENU[name]['cost']} $ )")
        print(f"Here is your money {money_inserted} $")


def make(name):
    need = menu.MENU[name]['ingredients']
    left = menu.resources
    menu.resources = {key: left[key] - need.get(key, 0) for key in left}
    print(f"Here is your tasty {name}, i wish you a nice day")


def user_choice(user_wants):
    if user_wants == "off":
        turn_off()
    elif user_wants == "report":
        give_report()

    elif user_wants not in menu.MENU:
        print(f"Sorry we dont have {user_wants}, we only have {', '.join([i for i in menu.MENU.keys()]).title()}")
    else:
        user_wants = user_wants.lower()
        check_ressources(user_wants)
        if refill == 0:
            process_coins(user_wants)
            make(user_wants)
        else:
            print("Please call maintenance for refilling the automat")


on = "on"
refill = 0
while on == "on":
    user_choice(input("What do you want?"))
