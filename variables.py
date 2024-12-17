import json
from functions import *

def load_file(file):
    opened_file = open(file, "r")
    return json.load(opened_file)
    opened_file.close()

employee_database = load_file("employees.json")







seperator = "-------------------------------------------------------------"

status_1_control_pannel_display = f"""info  --->  show my info
complain  --->  complain on an employee or a manager
quit  --->  quit the program"""
status_2_control_pannel_display = f"""info  --->  show my info
employee info  ---> show info of an employee
bonus  --->  control the bonuses
show best  ---> show the employees with best stats
change work  --->  change the work of an employee
report  --->  report an employee
fire  --->  fire an employee
quit  --->  quit the program"""
status_3_control_pannel_display = f"""info  --->  show my info
employee info  ---> show info of an employee or a manager
show best  ---> show the employees with best stats
change work  --->  change the work of an employee
report  --->  report an employee
fire  --->  fire an employee
quit  --->  quit the program"""
status_4_control_pannel_display = f"""info  --->  show my info
employee info  ---> show info of an employee or a manager
bonus  --->  control the bonuses
show best  ---> show the employees with best stats
change work  --->  change the work of an employee
report  --->  report an employee
fire  --->  fire an employee
quit  --->  quit the program"""



show_best_pannels = {
    "warehouse" : """loader  --->  show the best loaders
driver  --->  show the best drivers
back  --->  go back to control pannel""",
    "accounting" : """accountant  --->  show the best accountants""",
    "sales" : """seller  --->  show the best salesmen""",
    "management" : """manager  --->  show the best managers(in terms of complaints)
seller  --->  show the best sellers(in terms of sold units)
accountant  --->  show the best accountants(in terms of sheets analyzed)
HR  --->  show the best HR employees(in terms of complaints) 
loader  --->  show the best loaders(in terms of loaded units)
driver  --->  show the best drivers(in terms of transported units)
back  --->  go back to control pannel"""
}






def warehouse_change_work_pannel(worker):
    output = f"""loader  --->  change {worker["name"]}'s work to a loader
driver  --->  change {worker["name"]} to a driver
back  --->  go back to pannel"""
    return output
def accounting_change_work_pannel(worker):
    output = f"""accountant --->  change {worker["name"]}'s work to an accountant
back  --->  go back to pannel"""
    return output
def sales_change_work_pannel(worker):
    output = f"""seller --->  change {worker["name"]}'s work to an seller
back  --->  go back to pannel"""
    return output
def human_resources_change_work_pannel(worker):
    output = f"""guard  --->  change {worker["name"]}'s work to a guard
janitor  --->  change {worker["name"]}'s work to a janitor
secretary  --->  change {worker["name"]}'s work to a secretary
back  --->  go back to pannel"""
    return output
def management_change_work_pannel(worker):
    output = f"""HR  --->  change {worker["name"]}'s work to a human resources employee
accounting manager  --->  change {worker["name"]}'s work to an accounting manager
sales manager  --->  change {worker["name"]}'s work to an sales manager
warehouse manager  --->  change {worker["name"]}'s work to an warehouse manager
accounting manager  --->  change {worker["name"]}'s work to an accounting manager
seller --->  change {worker["name"]}'s work to an seller
accountant --->  change {worker["name"]}'s work to an accountant
driver  --->  change {worker["name"]} to a driver
loader  --->  change {worker["name"]}'s work to a loader
secretary  --->  change {worker["name"]}'s work to a secretary
guard  --->  change {worker["name"]}'s work to a guard
janitor  --->  change {worker["name"]}'s work to a janitor
back  --->  go back to pannel
"""
    return output





change_work_status_2 = {
    "accountant" : ("sheets analyzed" , "accounting"),
    "seller" : ("sold units" , "sales"),
    "loader" : ("loaded units" , "warehouse"),
    "driver" : ("transported units" , "warehouse")
}

change_work_status_3 = {
    "janitor" : (None , "maintenance"),
    "secretary" : (None , "administration"),
    "guard" : (None , "security"),

}
change_work_status_4 = {
    "manager" : None,
    "accounting manager" : (None , "accounting"),
    "warehouse manager": (None, "warehouse"),
    "sales manager": (None, "sales"),
    "hr" : (None , "human resources"),
    **change_work_status_3,
    **change_work_status_2
}