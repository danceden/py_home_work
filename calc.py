while True:
    try:
        a = int(input("Введите первое число:"))
        repeat = "r"
        while repeat == "r":
            try:
                operation, b = input("Введите операцию(+, -, *, /, **, =); через пробел введите чиcло:").split()
                b = int(b)
                if  operation == "+":
                    a = a + b
                elif operation == "-":
                    a = a - b
                elif operation == "*":
                    a = a * b
                elif operation == "/":
                    if b != 0:
                        a = a / b
                    else:
                        print(" На ноль делить нельзя!")
                elif operation == "**":
                    a = a ** b
                else:
                    print("Ошибка! Такой операции нет!")
            except:
                print("Результат:", a)
                repeat = input("Введите: r - продолжить или любую другую кнопку, чтоб начать сначала:")
    except ValueError:
        print("Ошибка! Вы ввели не чиcло!")