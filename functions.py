from variables import *
from sys import exit
import json
def run(employee_list):
    employee = check_via_email(employee_list)
    greet(employee)
    give_based_on_status(employee)


def search(employee_list):
    not_found = True
    answer = input("> ").strip()
    if(not answer == "back"):
        for employee in employee_list:
            if (answer == employee["name"]):
                not_found = False
                return employee
                break
        if (not_found):
            print("not found, please try again")
            return search(employee_list)
def greet(employee):
    print(f"hello { employee["name"] } ")

def check_via_email(employee_list):
    not_found = True
    print("please enter your email")
    entered_email =  input("> ").strip()
    print("please enter your password")
    entered_password = input("> ").strip()
    for employee in employee_list:
        if(entered_email == employee["email"] and entered_password == employee["password"]):
            not_found = False
            return employee
            break
    if(not_found):
        print("not found or password is wrong, please try again")
        return check_via_email(employee_list)


def undefined_keyword():
    print(f"""sorry, undefined keyword. please try again
{seperator}""")

def give_based_on_status(employee):
    print(seperator)
    if(employee["status"] == 1):
        status_1_control_pannel(employee)
    elif (employee["status"] == 2):
        status_2_control_pannel(employee)
    elif (employee["status"] == 3):
        status_3_control_pannel(employee)
    elif (employee["status"] == 4):
        status_4_control_pannel(employee)

def save_data(file, data):
    with open(file, "w") as new_json_file:
        json.dump(data, new_json_file, indent=4)

def status_1_control_pannel(employee):
    print(status_1_control_pannel_display)
    answer = input("> ").lower().strip()
    if(answer == "info"):
        show_info(employee , True)
    elif(answer == "complain"):
        complain(employee , False)
    elif (answer == "quit"):
        save_data("employees.json" , employee_database)
        quit()
    else:
        undefined_keyword()
        status_1_control_pannel(employee)
def status_2_control_pannel(employee):
    print(status_2_control_pannel_display)
    answer = input("> ").lower().strip()
    if(answer == "info"):
        show_info(employee , True)
    elif(answer == "employee info"):
        show_employee_info(employee)
    elif(answer == "bonus"):
        bonus_control(2 , employee)
    elif(answer == "show best"):
        show_best_pannel(employee)
    elif (answer == "change work"):
        change_work(employee)
    elif (answer == "report"):
        report(employee)
    elif(answer == "fire"):
        terminate(employee)
    elif (answer == "quit"):
        save_data("employees.json" , employee_database)
        quit()
    else:
        undefined_keyword()
        status_2_control_pannel(employee)



def status_3_control_pannel(employee):
    print(status_3_control_pannel_display)
    answer = input("> ").lower().strip()
    if (answer == "info"):
        show_info(employee , True)
    elif (answer == "employee info"):
        show_employee_info(employee)
    elif (answer == "show best"):
        show_best_pannel(employee)
    elif (answer == "change work"):
        change_work(employee)
    elif (answer == "report"):
        report(employee)
    elif (answer == "fire"):
        terminate(employee)
    elif (answer == "quit"):
        save_data("employees.json" , employee_database)
        quit()
    else:
        undefined_keyword()
        status_3_control_pannel(employee)


def status_4_control_pannel(employee):
    print(status_4_control_pannel_display)
    answer = input("> ").lower().strip()
    if (answer == "info"):
        show_info(employee , True)
    elif (answer == "employee info"):
        show_employee_info(employee)
    elif (answer == "bonus"):
        bonus_control(4 , employee)
    elif (answer == "show best"):
        show_best_pannel(employee)
    elif (answer == "change work"):
        change_work(employee)
    elif (answer == "report"):
        report(employee)
    elif (answer == "fire"):
        terminate(employee)
    elif(answer == "quit"):
        save_data("employees.json" , employee_database)
        quit()
    else:
        undefined_keyword()
        status_4_control_pannel(employee)








def show_info(employee , for_self):
    state = "inactive"
    pay_after_bonus = employee["pay"]*employee["bonus"]/100 +employee["pay"]
    if(employee["active"]):
        state = "active"
    print(f"""name : {employee["name"]}
department : {employee["department"]}
work : {employee["work"]}
pay : {employee["pay"]}$    after bonus({employee["bonus"]}%) : {pay_after_bonus}$
arrival delay (hours) : {employee["arrival delay (hours)"]}
working time (years) : {employee["working time (years)"]}
email : {employee["email"]}
bonus : {employee["bonus"]}%
complaints : {employee["complaints"]}
state : {state}""")
    if(employee["work"] in change_work_status_2):
        print(f"{change_work_status_2[employee["work"]][0]} : {employee[change_work_status_2[employee["work"]][0]]}")
    if(for_self):
        give_based_on_status(employee)



def complain(employee , reported):
    list_employee_names(employee, employee_database , True)
    person_complained_on = search(employee_database)
    person_complained_on["complaints"] += 1
    print(f"successfully complained on  {person_complained_on["name"]}")
    if(reported):
        report(employee)
    else:
        give_based_on_status(employee)

def quit():
    print("goodbye")
    exit()

def show_employee_info(employee):
    list_employee_names(employee , employee_database)
    searched_person = search(employee_database)
    if(employee["status"] == 2):
        if(searched_person["department"] == employee["department"] and not searched_person["work"] == "manager"):
            show_info(searched_person , False)
        else:
            print(f"you cant see the info of {searched_person["name"]} since they're not in your department or they are managers")
    elif(employee["status"] == 3):
        if(not searched_person["department"] == "management" and not searched_person["work"] in ["seller" , "accountant" , "loader" , "driver"]):
            show_info(searched_person , False)
        else:
            print(f"you cant see the info of {searched_person["name"]} since they are managers or in the management department")
    elif(employee["status"] == 4):
        if(not searched_person["department"] == "management"):
            show_info(searched_person , False)
        else:
            print(f"you cant see the info of {searched_person["name"]} since they are in the management department")
    give_based_on_status(employee)

def list_employee_names(employee , employee_list , all = False , show_managers = True):

    if(all):
        for worker in employee_database:
            print(f"{worker["name"]}          {worker["department"]}          {worker["work"]}")
    else:
        for worker in employee_list:
            if(employee["department"] == "human resources" and worker["work"] in ["manager" , "guard" , "janitor" , "secretary"]):
                if(show_managers):
                    print(f"{worker["name"]}          {worker["department"]}          {worker["work"]}")
                elif(not show_managers and not worker["work"] == "manager"):
                    print(f"{worker["name"]}          {worker["department"]}          {worker["work"]}")
            elif (employee["department"] == "management" and not worker["department"] == "management"):
                print(f"{worker["name"]}          {worker["department"]}          {worker["work"]}")
            elif(worker["department"] == employee["department"] and not worker["work"] == "manager" and not (employee["department"] == "human resources" or employee["department"] == "management")):
                 print(f"{worker["name"]}          {worker["department"]}          {worker["work"]}")

    print(seperator)
def bonus_control(status , employee):
    list_employee_names(employee , employee_database)
    print("please enter the name of the employee you want to give a bonus to")
    bonused_person = search(employee_database)
    print(f"please enter the bonus that you want to give to {bonused_person["name"]}")
    bonus = float(input("> ").strip())
    try:
        if(bonus > 0):
            if(status == 2):
                if(bonused_person["department"] == employee["department"] and not bonused_person["work"] == ("manager" or "HR employee")):
                    bonused_person["bonus"] = bonus
                    print(f"a bonus of {bonus}% was successfully set to {bonused_person["name"]}")
                else:
                    print(f"you cant give {bonused_person["name"]} a bonus")
            elif(status == 4):
                if(not bonused_person["department"] == "management"):
                    bonused_person["bonus"] = bonus
                    print(f"a bonus of {bonus}% was successfully set to {bonused_person["name"]}")
                else:
                    print(f"you cant give a bonus to {bonused_person["name"]}")
        else:
            print("you cant give a negative bonus. please try again")
            bonus_control(status , employee)
    except:
        print("invalid bonus, please try again")
        bonus_control(status , employee)
    give_based_on_status(employee)



def print_best_at_job(work):
    best_list = sort_best_at_job(work)
    if(work in change_work_status_2):
        for employee in best_list:
            print(f"""{employee["name"]} : {employee[change_work_status_2[work][0]]} {change_work_status_2[work][0]}          {employee["complaints"]} complaints
""")
    elif (work == "manager"):
        best_list.reverse()
        for employee in best_list:
            print(f"""{employee["name"]}({employee["department"]}) : {employee["complaints"]} complaints
""")
    elif (work == "human resources"):
        best_list.reverse()
        for employee in best_list:
            print(f"""{employee["name"]}({employee["department"]}) : {employee["complaints"]} complaints
""")





def sort_best_at_job(work):
    worker_list = []
    if(work in change_work_status_2):
        for employee in employee_database:
            if(employee["work"] == work):
                worker_list.append(employee)
        return quick_sort(worker_list , change_work_status_2[work][0])
    elif (work == "human resources"):
        for employee in employee_database:
            if (employee["work"] == "HR employee"):
                worker_list.append(employee)
        return quick_sort(worker_list , "complaints")
    elif (work == "manager"):
        for employee in employee_database:
            if (employee["work"] == "manager"):
                worker_list.append(employee)
        return quick_sort(worker_list , "complaints")



def quick_sort(list , domain):

    if(len(list) <= 1):
        return(list)
    else:
        pivot = list.pop()
        more_than_pivot = []
        less_than_pivot = []
        for employee in list:
            if(employee[domain] < pivot[domain]):
                more_than_pivot.append(employee)
            else:
                less_than_pivot.append(employee)
        return quick_sort(less_than_pivot , domain) + [pivot] + quick_sort(more_than_pivot , domain)

def show_best_pannel(employee):
    if(employee["department"] in show_best_pannels):
        print(show_best_pannels[employee["department"]])
        answer = input("> ").lower().strip()
        if(not answer == "back"):
            if(answer in change_work_status_2 and employee["department"] == change_work_status_2[answer][1]):
                print_best_at_job(answer)
            elif(answer in change_work_status_4 and employee["department"] == "management"):
                print_best_at_job(answer)
            else:
                undefined_keyword()
                show_best_pannel(employee)
    elif (employee["department"] == "human resources"):
        print("managers :")
        print_best_at_job("manager")

    give_based_on_status(employee)

def report(employee):

    print("""complain  --->  complain about an employee
delayed arrival  --->  report delayed arrival hours
back  --->  go back to pannel""")
    answer = input("> ").lower().strip()
    if(not answer == "back"):
        if(answer == "complain"):
            complain(employee , True)
        elif(answer == "delayed arrival"):
            delayed_arrival_report(employee)
        else:
            undefined_keyword()
            give_based_on_status(employee)
    give_based_on_status(employee)

def delayed_arrival_report(employee):
    list_employee_names(employee, employee_database)
    print("please enter the name of the employee that's late for work")
    reported_employee = search(employee_database)
    if (reported_employee["department"] == employee["department"] and not reported_employee["work"] == "manager" or employee["department"] == "human resources" or employee["department"] == "management"):
        print(f"how many hours did {reported_employee["name"]} miss")

        try:
            delayed_arrival_hours = float(input("> "))
        except :
            print("please try again and enter a number")
            delayed_arrival_report(employee)
        reported_employee["arrival delay (hours)"] += delayed_arrival_hours
        print(f"""{delayed_arrival_hours} hours were added successfully
{reported_employee["name"]} now has {reported_employee["arrival delay (hours)"]} delayed arrival hours noted on them""")
    else:
        print(f"you cant or are not responsible to report {reported_employee["name"]} delayed arrival")
        print(seperator)


def terminate(employee):
    list_employee_names(employee , employee_database , show_managers = False)
    print("please enter the name of the employee you want to fire")
    searched_person = search(employee_database)
    if(employee["status"] == 2):
        if(searched_person["department"] == employee["department"] and not searched_person["work"] == "manager"):
            searched_person["active"] = False
            print(f"{searched_person["name"]} was fired")
        else:
            print(f"you cant fire {searched_person["name"]}, they might not be in your department or are managers ")
    elif(employee["status"] == 3):
        if(not searched_person["work"] in ["manager" , "loader" , "seller" , "accountant"] and not searched_person["department"] == "management"):
            searched_person["active"] = False
            print(f"{searched_person["name"]} was fired")
        else:
            print(f"you cant fire {searched_person["name"]}, they might be managers ")
    elif(employee["status"] == 4):
        if(not searched_person["department"] == "management"):
            searched_person["active"] = False
            print(f"{searched_person["name"]} was fired")
        else:
            print(f"you cant fire {searched_person["name"]} since they are in management")
    give_based_on_status(employee)


def change_work(employee):
    list_employee_names(employee, employee_database , show_managers = False)
    worker = search(employee_database)
    department = employee["department"]
    if(department == "warehouse"):
        print(warehouse_change_work_pannel(worker))
    elif(department == "human resources"):
        print(human_resources_change_work_pannel(worker))
    elif(department == "accounting"):
        print(accounting_change_work_pannel(worker))
    elif (department == "sales"):
        print(sales_change_work_pannel(worker))
    elif(department == "management"):
        print(management_change_work_pannel(worker))
    answer = input("> ").lower().strip()
    if(not answer == "back"):
        if(not worker["work"] == answer):
            if(employee["status"] == 2):
                if(answer in change_work_status_2 and employee["department"] == worker["department"]):
                    change_worker_initials(worker , answer)
                else:
                    print(f"undefined keyword or you can't change {worker["name"]}'s work ")
            elif(employee["status"] == 3):
                if(answer in change_work_status_3):
                    change_worker_initials(worker , answer)
                else:
                    print(f"undefined keyword or you can't change {worker["name"]}'s work ")
            elif(employee["status"] == 4):
                if(answer in change_work_status_4):
                    change_worker_initials(worker, answer)
                else:
                    print(f"undefined keyword or you can't change {worker["name"]}'s work ")
        else:
            print(f"{worker["name"]} already works as {answer} ")

    give_based_on_status(employee)
def change_worker_initials(worker , work):
    worker["work"] = work
    worker["department"] = change_work_status_4[work][1]
    worker[change_work_status_4[work][0]] = 0
    clear_unwanted_keys(worker, change_work_status_4[work][0])
    print(f"successfully changed {worker["name"]}'s work to {work}")
def clear_unwanted_keys(employee, key ="default"):
    key_set = {"loaded units", "transported units", "sold units", "sheets analyzed"}
    if(key == "default"):
        for unwanted_key in key_set:
            if (unwanted_key in employee):
                del employee[unwanted_key]
    else:
        new_key = {key}
        keys_to_remove = key_set - new_key
        for unwanted_key in keys_to_remove:
            if(unwanted_key in employee):
                del employee[unwanted_key]









