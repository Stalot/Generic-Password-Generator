def matematica(num1, num2, **kwargs):

    match kwargs['operation']:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            return f'ERROR: The math operator ({kwargs["operation"]}) is invalid. Only +, -, * and / are accepted.'
    
result = matematica(3, 8, operation='+')
print(result)