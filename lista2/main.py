
def peek(str):
    if not str:
        return '\0'
    return str[0]


def consume(str):
    return str[1:]


def parserExpression(str):
    result = expression(str)
    if result:
        raise RuntimeError('invalid expression')

    return 'Valid Expression'


def expression(str):
    str = term(str)
    str = r(str)

    return str


def r(str):
    exp = peek(str)

    if exp == '+' or exp == '-':
        str = consume(str)
        return expression(str)

    return str


def s(str):
    exp = peek(str)
    if exp == '/' or exp == '*':
        str = consume(str)
        return term(str)

    return str


def term(str):
    str = factor(str)

    return s(str)


def factor(str):
    if peek(str) != 'x':
        raise RuntimeError('Unexpected character')

    return consume(str)


exp = 'x'
print(parserExpression(exp))
