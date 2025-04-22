def operations(sign ,num1 = 0,num2 = 0):
    if sign == '+':
        result = num1 + num2
        return result
    elif sign == '-':
        result = num1 - num2
        return result
    elif sign == '*':
        result = num1 * num2
        return result
    elif sign == '%': #remainder
        result = num1 % num2
        return result
    elif sign == '/': #Quotient
        result = num1 / num2
        return result
    else:
        result = num1
        return result


signslist = ['+','-','*','%','/']
num1 = int(input("Enter number:"))
sign = input("Enter sign :")

if sign in signslist:
    while sign in signslist:
        num2 = int(input("Enter number:"))
        updated_result = (operations(sign, num1, num2))
        num1 = updated_result
        sign = input("Enter sign :")
        if sign == '=':
            print(updated_result)



