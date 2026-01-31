def CPS(string: str) -> str:
    stack = []
    for el in string:
        if el in "({[":
            stack.append(el)
        elif el in ")}]":
            if not stack:
                return False
            last_el = stack.pop()
            if el == ")" and last_el == "(":
                continue
            if el == "}" and last_el == "{":
                continue
            if el == "]" and last_el == "[":
                continue
            return False
    return not stack


def test():
    count = 0
    test_lst = {
        ")": False,
        "(){}[]": True,
        "({[]})": True,
        "(]": False,
        "([)]": False,
        "{{(}}": False,
        "": True,
        "(11+2)/2*3{}[": False,
        "(тест(о))/[2*3]{тут ф строка}": True,
    }
    for k in test_lst:
        if CPS(k) != test_lst[k]:
            print(f"Тест {k} не прошел")
            count -= 1
        else:
            print(f"Тест {k} прошел")
        count += 1
    if count == len(test_lst):
        print(f"\nВсе тесты успешно пройдены")
    else:
        print(f"\nЧто то пошло не так")


if __name__ == "__main__":
    test()
