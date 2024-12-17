this program will let any employee do what the can with the power that they have
first , the person enters their email and the they enter their password
if the email and the password are correct , they will be identified via the "check_via_email" function. if not a message would be printed
informing the user of that and allowing them to try again
the employees are divided into 4 groups based on their power by the "sort_status" function and the corrisponding control pannel will apear
each status has unique abilities, the status 1 group are on the bottom, they can only see their info and complain about another employee
the status 2 group are the managers of departments, they can fire , report , see the info of , set a bonus and see the employees with best stats
but the status 2 group members are limmeted to their department and cannot operate on employees from other departments or managers
status 3 group which are human resources employees , can do all of what status 2 group can do , but they are not limmeted to a department
however they cannot operate on employees from the management department or employees for departments where managers exist. they also can't fire managers 
status 4 group are the management employees , they are the upper managers and can do whatever they want to any employee
but they cant operate on employees from the management department
status 1 employees--------------------------------------------------------------
they have 3 options , info and complain , quit

info will show all their personal info but the password to enter into their pannel and thats via the "show_info()" function
this function takes in 2 parameters , the employee of the info thats wanted , and the for_self bool
if the for_self is true , then after the info is given it would return to the pannel of the employee of the info
if its false , it would not return to any pannel.

complain will be entering a complaint on an employee. in the complaint system the complaints are recorded via the "complain" function
any status employee can enter a complaint to any other employee

quit will quit the program
status 2 employees--------------------------------------------------------------
they have 8 options , info , employee info , show best , change work , report , bonus , fire , quit

the employee info shows the info of an employee via the "show_employee_info"
the name is entered via "search" function , and the info is handeled by the "show_info" function with for_self set to false

show best will show the employees from best (at working) to the worst via the "print_best_at_job" function
this function takes the work as an argument so only the employees in that specific work will be showed
in this function contains the "sort_best_at_job" function which also takes the work as an argument
the "sort_best_at_job" function adds all the employees from the specified work and then quicksorts them from best to worst
some of the status 2 employees have multiple work groups in the department so it will take them to a pannel were they specify the work they want

change work will change the wok of an employee. it takes the function that should be returned to if back was selected and the user(employee)
as an argument. it will take the user into a pannel that will guide the user furthe to change the work of their inferiors

report will take them to a pannel with three options , complain , delayed arrival and back

the delayed arrival will allow the managers to add the hours if any worker was late to arrive to work
it is handeled by the "delayed_arrival_report" function

back will let the user exit the report pannel

bonus will allow the user to add a bonus to an employee and its handeled by the "bonus_control" function

fire will allow the user to delete an employee from the database and its handeled by the "terminate" function
the employee deleted has their name inputed via the "search" function

status 3 employees------------------------------------------------------------
they have 7 options , info , employee info , show best , report , fire , quit

they can do everything that status 2 employees can even on managers but not on the management department and no bonus control

status 4 employees------------------------------------------------------------
they have 8 options , info , employee info , show best , report , bonus , fire , quit

they have power over every body excluding the employees in the management department
#########################################################################################################################
in any case of not entering correct key or plain out jiberish , the program will output a message indicating that and allow the user to try again
the saving system is dne by taking the employee_database(its a list of the employee dictionaries) from the employees.json file
and dumping them there when the quit keyward is called
