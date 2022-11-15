from math import sqrt
import re

def calc():
    try:
        equation = input("Enter equation : ")
        x = re.search(
            "^([\-\+])?((sqrt\(((\-|\+|\*|\/|\*\*)?(\(?([\-\+])?\d+(\.\d+)?\)?)?)+\))|(\d+(\.\d+)?))((\-|\+|\*|\/|\*\*)([\-\+])?((\(?sqrt\(((\-|\+|\*|\/|\*\*)?(\(?([\-\+])?\d+(\.\d+)?\)?)?)+\)\)?)|(\(?([\-\+])?\d+(\.\d+)?\)?)))+",
            equation)
        print("Matching: " + x.group())
        print(eval(x.group()))
    except ZeroDivisionError:
        print("It is not possible to divide by 0 :(")
    except AttributeError:
        print("Are you doing math with letters? :thinking:")
    except SyntaxError:
        print("That is an invalid expression")
    except:
        print("Something went wrong, but I don't know what...")


if __name__ == '__main__':
    while True:
        calc()

#Simple explanation of regex expression
# (\-|\+|\*|\/|\*\*)? - searches for the math operatores
# ([\-\+])?\d+(\.\d+)?) - searches for a number, that can start with "-" and "+" and can be a float, eg. -23.4, +5.2, -1