from calculator import Calculator

myCalc = Calculator()
a = float(input("Первое число: "))
b = float(input("Второе число: "))
move = input("Выберите действие +, -, *, / : ")
if move in ('+', '-', '*', '/'):
    if move == "+":
        print(myCalc.plus(a, b))
    elif move == "-":
        print(myCalc.minus(a, b))
    elif move == "*":
        print(myCalc.multi(a, b))
    elif move == "/":
        print(myCalc.div(a, b))
else:
    print("Error")
input("Press Enter to close...")

