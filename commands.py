from classes import Debt
from classes import Payment
import json


###
def print_menu():
    print("Press the button assigned to desired actions listed below:")
    print("0    -   create a debt")
    print("1    -   make payment")
    print("2    -   save operations locally")
    print("3    -   load operations from the disk")
    print("4    -   application log")
    print("5    -   update a debt")
    print("6    -   update a payment")
    print("7    -   show general debt")
    print("8    -   show payments list")
    print("9    -   show overall status of debt")


###### DEBT part

###
def input_debt_info():
    _id = input("ID: ")
    title = input("Title of the debt: ")
    to_whom = input("To whom you owe? ")
    how_much = input("How much do you owe? ")
    date = input("Date of the loan: ")
    return {
            "id": _id,
            "title": title,
            "to_whom": to_whom,
            "how_much": how_much,
            "date": date,
            "paid": False
        }

###
def create_debt():
    print("Please enter your debt info")
    debt_input = input_debt_info()
    debt = Debt(debt_input['id'], debt_input['title'], debt_input['to_whom'], 
                debt_input['how_much'], debt_input['date'], debt_input['paid'])

    print(debt.to_dict())
    return debt

###
def save_debts(debts):
    json_debts = []
    for debt in debts:
        json_debts.append(debt.to_dict())
    try:
        file = open("debts.dat", "a")
        file.write(json.dumps(json_debts, indent=4))
    except:
        print("error: saving the debts")

###
def load_debts():
    try:
        file = open("debts.dat", "r")
        loaded_debts = json.loads(file.read())
        debts = []
        for debt in loaded_debts:
            new_debt = Debt(debt['id'], debt['title'], debt['to_whom'], 
                debt['how_much'], debt['date'], debt['paid'])
            debts.append(new_debt)
        print("succesfully loaded")
        return debts
    except:
        print("the file doesnt exist or an error occured during loading")

###
def find_debt_by_id(debts, id):
    for index, debt in enumerate(debts):
        if debt.id == id:
            return index
    return None

###
def find_debts_to_id_list(debts, to_whom):
    whom_id_list = []
    for debt in debts:
        if (debt.to_whom).lower() == to_whom.lower():
            whom_id_list.append(debt.id)
    return whom_id_list

###
def find_debts_to_debt_list(debts, to_whom):
    whom_debt_list = []
    for debt in debts:
        if (debt.to_whom).lower() == to_whom.lower():
            whom_debt_list.append(debt)
    return whom_debt_list

###
def show_group_by_id(debts, group_ids):
    groups = []
    for debt in debts:
        for one in group_ids:
            if debt.id == one:
                groups.append(debt)
    return groups

###
def paid_debt(debts):
    id = input("enter id of the debt you want to issue")
    index = find_debt_by_id(debts, id)
    if index != None:
        debts[index].paid = True
        print("congratullations, you have paid one debt")
    else:
        print("haven't find debt")

def update_debt(debts):
    id = input("enter id of the debt you want to issue")
    index = find_debt_by_id(debts, id)
    if index != None:
        new_debt = create_debt()
        old_debt = debts[index]
        debts[index] = new_debt
        del old_debt
        print("Debt successfully updated")
    else:
        print("There is no such index")
    

###### PAYMENTS part

###
def find_payment_by_id(payments, id):
    for index, payment in enumerate(payments):
        if payment.id == id:
            return index
    return None

###
def input_payment():
    _id = input("ID: ")
    receiver = input("To whom? ")
    amount = input("How much? ")
    date = input("Date of the payment: ")
    return {
            "id": _id,
            "reciever": receiver,
            "amount": amount,
            "date": date
        }

###
def create_payment():
    print("Please enter your payment info")
    payment_input = input_payment()
    _payment = Payment(payment_input['id'], payment_input['reciever'], 
                payment_input['amount'], payment_input['date'])

    print(_payment.to_dict())
    return _payment

###
def save_payments(payments):
    json_payments = []
    for pay in payments:
        json_payments.append(pay.to_dict())
    try:
        file = open("payments.dat", "w")
        file.write(json.dumps(json_payments, indent=4))
    except:
        print("error: saving the payments")

###
def load_payments():
    try:
        file = open("payments.dat", "r")
        loaded_payments = json.loads(file.read())
        payments = []
        for pay in loaded_payments:
            new_pay = Payment(pay['id'], pay['reciever'], 
                            pay['amount'], pay['date'])
            payments.append(new_pay)
        print("succesfully loaded")
        return payments
    except:
        print("the file doesnt exist or an error occured during loading")

def update_payment(payment):
    id = input("enter id of the payment you want to issue")
    index = find_payment_by_id(payment, id)
    if index != None:
        new_payment = create_payment()
        old_payment = payment[index]
        payment[index] = new_payment
        del old_payment
        print("Debt successfully updated")
    else:
        print("There is no such index")

###
def find_debts_to_id_list(debts, to_whom):
    whom_id_list = []
    for debt in debts:
        if (debt.to_whom).lower() == to_whom.lower():
            whom_id_list.append(debt.id)
    return whom_id_list

##### GENERAL part

###
def save_operations(debts, payments):
    save_debts(debts)
    save_payments(payments)

###
def load_operations():
    debts = load_debts()
    payments = load_payments()
    return [debts, payments]

###
def debt_list(debts):
    for debt in debts:
        print(debt.to_dict())

###
def payment_list(payments):
    for payment in payments:
        print(payment.to_dict())

###
def show_overall(debts, payments):
    # show debts and payments by reciever
    overall = 0 
    receivers = []
    for i in debts:
        if len(receivers) == 0:
            receivers.append((i.to_whom).lower())
        else:
            for j in receivers:
                if ((i.to_whom).lower()) != j:
                    receivers.append((i.to_whom).lower())

    for r in receivers:
        print(f"{r}\n")
        
        receiver_sum_debt = 0
        receiver_sum_payment = 0
        for d in debts:
            if ((d.to_whom).lower()) == r:
                k = d.how_much
                receiver_sum_debt = receiver_sum_debt + k
                print(f"{k}\n")
                ovarall = overall - k
        for p in payments:
            if (p.reciever).lower() == r:
                k = d.amount
                receiver_sum_payment = receiver_sum_payment + k
                print(f"{k}\n")
                ovarall = overall + k
        ovr = receiver_sum_payment - receiver_sum_debt
        print(f"Sum of debt owed to {r} is {receiver_sum_debt} and you\n")
        print(f"have already paid {receiver_sum_payment} and overall\n") 
        if  ovr == 0:
            print(f"You have paid off your debt :D \n")
        elif ovr < 0:
            print(f"You have still {abs(ovr)} to pay\n")
        else:
            print(f":O You payed to much still for about {abs(ovr)}\n")

    if overall > 0:
        print(f"people owe you {overall} money\n")
    else:
        print(f"you still owe people {overall} money\n")        

###
def show_all_debts(debts):
    for debt in debts:
        print(debt.to_dict())

###
def show_all_payments(payments):
    for payment in payments:
        print(payment.to_dict())
