def postfix_calc(L: list):
    flag = True
    while flag:
        n = input()
        if n == '=' and len(L) > 0:
            flag = False
        elif n in '+-*/' and len(L) > 1:
            right = L.pop()
            left = L.pop()
            if n == '+':
                n = left + right
            elif n == '-':
                n = left - right
            elif n == '*':
                n = left * right
            elif n == '/':
                n = left / right
            L.append(n)
        elif n.isdigit():
            L.append(float(n))
        else:
            return 'is incorrect'
    return L.pop()


End, O = [], []
flag = True
while flag:
    n = input()
    if n == '=':
        flag = False
        for _ in range(len(O)):
            End.append(O.pop())
    elif n in ('*', '/', '+', '-'):
        O.append(n)
        for _ in range(len(O) - 1):
            if len(O) > 1:
                if O[len(O) - 1] in '+-' and O[len(O) - 2] in '*/':
                    End.append(O.pop(len(O) - 2))
                elif O[len(O) - 1] in '*/' and O[len(O) - 2] in '*/':
                    End.append(O.pop(len(O) - 2))
                elif O[len(O) - 1] in '+-' and O[len(O) - 2] in '+-':
                    End.append(O.pop(len(O) - 2))
    elif n.isdigit():
        End.append(n)
print(End, O)
