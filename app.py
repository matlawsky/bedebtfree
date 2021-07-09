import commands
import os

debts = []
payments = []

commands.print_menu()
_input = input()
while _input != 'x' and _input != 'X':
    if _input == "0":
        debts.append(commands.create_debt())
    elif _input == "1":
        payments.append(commands.create_payment())     
    elif _input == "2":
        commands.save_operations(debts, payments)
    elif _input == "3":
        debts = commands.load_operations()[0]
        payments = commands.load_operations()[1]
        print(f"{len(debts)}")
        print(f"{len(payments)}")
    elif _input == "4":
        commands.paid_debt(debts)
    elif _input == "5":
        commands.update_debt(debts)
    elif _input == "6":
        commands.update_payment(payments)
    elif _input == "7":
        commands.show_all_debts(debts)
    elif _input == "8":
        commands.show_all_payments(payments)
    elif _input == "9":
        commands.show_overall(debts, payments)
    else: 
        print("There is no such action")
    input("done. press any key to go back to menu")
    os.system("cls")
    commands.print_menu()
    _input = input()
