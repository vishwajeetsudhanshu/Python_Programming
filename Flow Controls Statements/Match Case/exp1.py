#MatchCaseEx1.py
import sys
print("-"*50)
print("\tArithmetic Operations")
print("-"*50)
print("\t\t1.Addition")
print("\t\t2.Substraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Floor Division")
print("\t\t6.Mod Division")
print("\t\t7.Exponentiation")
print("\t\t8.Exit")
print("-"*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1:
        print("Enter Two Values for Addition")
        a,b=float(input()),float(input())
        print("\t\tSum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two Values for Substraction")
        a, b = float(input()), float(input())
        print("\t\tSub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two Values for Multiplication")
        a, b = float(input()), float(input())
        print("\t\tMul({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two Values for Division")
        a, b = float(input()), float(input())
        print("\t\tDiv({},{})={}".format(a, b, a / b))
    case 5:
        print("Enter Two Values for Floor Div")
        a, b = float(input()), float(input())
        print("\t\tFloorDiv({},{})={}".format(a, b, a // b))
    case 6:
        print("Enter Two Values for Mod Div")
        a, b = float(input()), float(input())
        print("\t\tMod({},{})={}".format(a, b, a % b))
    case 7:
        a, b = float(input("Enter Base:")), float(input("Enter Power:"))
        print("\t\tpow({},{})={}".format(a, b, a ** b))
    case 8:
        print("Thx for using program")
        sys.exit() # Physical Exit
    case _:
        print("UR Selection of Choice is wrong--try again")

print("Program execution is completed")