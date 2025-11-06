def Calculate(input1, input2, operator):

    if operator == 'add' or operator == '+':
        result = input1 + input2
    elif operator == 'subtract'    or operator == '-':
        result = input1 - input2
    elif operator == 'multiply'    or operator == '*':
        result = input1 * input2   
    elif operator == 'divide'  or operator == '/':
        if input2 != 0:
            result = input1 / input2
        else:
            raise ValueError('Cannot divide by zero')
    elif operator == 'power'   or operator == '^':
        result = input1 ** input2
    elif operator == 'modulus' or operator == '%':
        result = input1 % input2
    else:
        raise ValueError('Invalid operator')
    return result

#input1 = float(input("This is a calculator program. Please enter the first number: "))
#input2 = float(input("Please enter the second number: ")) 
#operator = input("Please enter the operator (add, subtract, multiply, divide, power) or the signs: ").strip().lower()
#print(result := Calculate(input1, input2, operator))