while True:
    num1 = int(input("ENTER UR FIRST NUMBER: "))
    num2 = int(input("ENTER UR SECOND NUMBER: "))
    opr = input("ENTER THE OPR (+, -, *, /): ")

    if opr == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opr == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif opr == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif opr == '/':
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("WRONG OPERATOR!!")

    again = input("Do u want to continue using calculator (YES/NO): ").upper()
    if again != "YES":
        print("CALCULATOR CLOSED 🚫")
        break
