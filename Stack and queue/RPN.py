def RPN(expressions: str) -> float:
    stack = []
    for el in expressions.split():
        if el in "+-/*":
            if len(stack) < 2:
                raise ValueError(
                    f"Недостаточно операндов для операции '{el}'"
                )
            operand2 = stack.pop()
            operand1 = stack.pop()
            if el == "+":
                result = operand1 + operand2
            if el == "-":
                result = operand1 - operand2
            if el == "*":
                result = operand1 * operand2
            if el == "/":
                if operand2 == 0:
                    raise ZeroDivisionError(
                        f"Деление на ноль в выражении: {operand1} / {operand2}"
                    )
                else:
                    result = operand1 / operand2
            stack.append(result)
        else:
            stack.append(float(el))
    if len(stack) != 1:
        raise ValueError(
            f"Некорректное выражение. В стеке осталось {len(stack)} элементов: "
            f"{list(stack)}"
        )
    else:
        return stack.pop()


def test_RPN():
    print("1. Базовые операции:")
    print(f"   '3 4 +' = {RPN('3 4 +')} (ожидается 7.0)")
    print(f"   '10 5 -' = {RPN('10 5 -')} (ожидается 5.0)")
    print(f"   '6 7 *' = {RPN('6 7 *')} (ожидается 42.0)")
    print(f"   '15 3 /' = {RPN('15 3 /')} (ожидается 5.0)")

    print("\n2. Сложные выражения:")
    print(f"   '3 4 + 2 *' = {RPN('3 4 + 2 *')} (ожидается 14.0)")
    print(f"   '5 1 2 + 4 * + 3 -' = {RPN('5 1 2 + 4 * + 3 -')} (ожидается 14.0)")

    print("\n3. Деление на ноль:")
    try:
        RPN("5 0 /")
        print("   ОШИБКА: должно было быть исключение!")
    except ZeroDivisionError as e:
        print(f"   ✓ Правильно вызвано исключение: {e}")

    print("\n4. Лишние числа:")
    try:
        RPN("3 4 5 +")
        print("   ОШИБКА: должно было быть исключение!")
    except ValueError as e:
        print(f"   ✓ Правильно вызвано исключение: {e}")

    print("\n5. Недостаток операндов:")
    try:
        RPN("3 +")
        print("   ОШИБКА: должно было быть исключение!")
    except ValueError as e:
        print(f"   ✓ Правильно вызвано исключение: {e}")


if __name__ == "__main__":
    test_RPN()
