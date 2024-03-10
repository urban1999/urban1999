def main():
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if operator == "+":
        sum(a, b)
    elif operator == "-":
        diff(a, b)
    elif operator == "*":
        mult(a, b)
    elif operator == "/":
        div(a, b)
    else:
        print("Error! Please try again.")
        main()

    restart = input("Would you like to try another calculation? Enter Y or N.")
    
    if restart == "Y":
        main()
    
def sum(a, b):
    answer = a + b
    print("Answer is: " + str(answer))

def diff(a, b):
    answer = a - b
    print("Answer is: " + str(answer))

def mult(a, b):
    answer = a * b
    print("Answer is: " + str(answer))

def div(a, b):
    answer = a / b
    print("Answer is: " + str(answer))

main()
