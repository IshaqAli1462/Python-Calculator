# Calculator
import sys
import time
import operator


def main_menu():  
    user_function = input(" 1 - Addition\n 2 - Subtraction\n 3 - Multiplication\n 4 - Division\n Q - Quit\n _________________________\n : ")
    if user_function == "1":
        time.sleep(.3)
        x = "Addition"
        y = operator.add
        numSum(x, y)
    elif user_function == "2":
        time.sleep(.3)
        x = "Subtraction"
        y = operator.sub
        numSum(x, y)
    elif user_function == "3":
        time.sleep(.3)
        x = "Multiplication"
        y = operator.mul
        numSum(x, y)
    elif user_function == "4":
        time.sleep(.3)
        x = "Division"
        y = operator.truediv
        numSum(x, y)
    elif user_function.lower() == "quit" or user_function.lower() == "q":
        sys.exit("Goodbye!")
    else:
        print("Error, \nPlease input one of the numbered options available!")
        time.sleep(2)
        main_menu()

def numSum(x, y):
    print(x)
    user_question= input(f"Please type in the numbers you would like to do {x}, using a space as a seperator: ")
    sum_list = [float(i) for i in user_question.split()]
    if len(sum_list)> 0:
        ans = y(sum_list[0], sum(sum_list[1:]))
        if ans % 1 == 0:
            intans = int(ans)
            print(intans)
        else:
            print(ans)
    else:
        print("Error, \nPlease enter a minimum of 2 values.")
        time.sleep(2)
        numSum()
    time.sleep(1)
    main_menu()


print("Calculator")
print("Please input the number for the function you would like to use")
time.sleep(.3)
main_menu()