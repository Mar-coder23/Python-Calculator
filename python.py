
# Created 4 function to calculate add, sub, multiply, divide
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b




# print statements to introduce and ask user which option to choose
print("Welcome to Mario's Calculator")
print("Please select an operation")
print("1.) Addition")
print("2.) Subtraction")
print("3.) Multiplication")
print("4.) Division")
print("1/2/3/4")


# Created a perform_calc() function to continusly ask if while loop is true, to select first and second number then it outputs the result
def perform_calc():
    while True: 
        option_choice = input("Choose an option here: ")
        
        if option_choice in ('1', '2', '3', '4'):
            a = float(input("First Number: "))
            b = float(input("Second Number: "))
            
            
            if option_choice == '1':
                result = add(a, b)
                print(f"Result: {a} + {b} = {result}")
            elif option_choice == '2':
                result = sub(a, b)
                print(f"Result: {a} - {b} = {result}")
            elif option_choice == '3':
                result = multiply(a, b)
                print(f"Result: {a} * {b} = {result}")
            elif option_choice == '4':
                if b == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = divide(a, b)
                    print(f"Result: {a} / {b} = {result}")
                    break
        else:
            print(" Invalid Input, choose a number between 1 and 4")
# Calling the function to perform it
perform_calc()

            
        
        
        
        
        
        
        
        
        

        















