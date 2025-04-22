def operations(sign ,num1 = 0,num2 = 0):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '%': #remainder
        return num1 % num2
    elif sign == '/': #Quotient
        if num2 == 0 :
            return "Divide by zero is not possible."

        else:
            return num1 / num2

def calci():
    signslist = ['+','-','*','%','/']
    try :
        num1 = float(input("Enter number:"))
        sign = input("Enter sign :")

        if sign in signslist:
            while sign in signslist:
                num2 = float(input("Enter number:"))
                updated_result = (operations(sign, num1, num2))
                num1 = updated_result
                sign = input("Enter sign :")
            print(updated_result)
        else:
            print("Invalid Symbol")
    except ValueError:
        print("Invalid number entered.")

if __name__ == '__main__':
    calci()

