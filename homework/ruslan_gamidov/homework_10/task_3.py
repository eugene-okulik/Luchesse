def operation_func(calc_func):
    def wrapper(first, second):
        if first == second:
            return calc_func(first, second, '+')
        elif first > second:
            return calc_func(first, second, '-')
        elif second > first:
            return calc_func(first, second, '/')
        elif first < 0 or second < 0:
            return calc_func(first, second, '*')
    return wrapper


@operation_func
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


x = float(input("Первое число: "))
y = float(input("Второе число: "))

print(calc(x, y))
