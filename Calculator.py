menu=1
import os
from time import sleep
def clear_screen():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')

#Print out the menu#
while menu==1:
    
    try:
        print('''
    *Calculator Menu* (Version 1.0)
        1. Add Two numbers
        2. Subtract Two Numbers
        3. Divide two numbers
        4. Multiply two numbers
        5. Calculate 8% tax on a value
        6. Calculate monthly payments,
        7. Quit
        ''')

#print user input#
        userchoice = int(input('Please select a menu item from 1 - 6: '))
        clear_screen()

#Addition#
        if userchoice == 1:
            print('Add Two Numbers')
            num_1 = float(input('First Number: '))
            num_2 = float(input('Second Number: '))
            result = num_1 + num_2
            print('Result: ', result)
            print('Going back to main menu now...')
            sleep(2)
            clear_screen()


#Subtraction#
        elif userchoice == 2:
            print('Subtract Two Numbers')
            num_1 = float(input('First Number: '))
            num_2 = float(input('Second Number: '))
            result = num_1 - num_2
            print('Result: ', result)
            print('Going back to main menu now...')
            sleep(2)
            clear_screen()
#Division#
        elif userchoice == 3:
            print('Divide Two Numbers')
            num_1 = float(input('First Number: '))
            num_2 = float(input('Second Number: '))
            result = num_1 / num_2
            print('Result: ', result)
            print('Going back to main menu now...')
            sleep(2)
            clear_screen()
#Multiplication#
        elif userchoice == 4:
            print('Multiply Two Numbers')
            num_1 = float(input('First Number: '))
            num_2 = float(input('Second Number: '))
            result = num_1 * num_2
            print('Result: ', result)
            print('Going back to main menu now...')
            sleep(2)
            clear_screen()
#Tax#
        elif userchoice == 5:
            print('Calculate 8% Tax')
            num_1 = float(input('First Number: '))
            num_2 = float(0.08)
            num_3 = float(1.08)
            result = num_1 * num_2
            result_2 = num_1 * num_3
            print('Tax Result: $', result)
            print('Total Amount: $', result_2)
            print('Going back to main menu now...')
            sleep(2)
            clear_screen()
#Monthly Payments#
        elif userchoice == 6:
            print('Monthly Payments')
            num_1 = float(input('Total Amount: '))
            num_2 = float(input('Number of years: '))
            result = num_1 / (num_2 * 12)
            print('Monthly Payments: $',result, " Per Month")
            print('Going back to main menu now...')
            sleep(2)
            clear_screen()
#else if user choose 7, program quit#
        elif userchoice == 7:
            break
        else:
            print('Invalid Menu Item')
        
    except ValueError:
        clear_screen()
        print("Invalid input type, Please enter a number")
