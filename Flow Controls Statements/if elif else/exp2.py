#program for accepting any Digit and display its name
#IfElifElseStmtEx2.py
d=int(input("Enter Any Digit:"))# 0  1   2    3  4  5 6 7 8 9
if(d==0):
    print("\t{} is ZERO".format(d))
elif(d==1):
    print("\t{} is ONE".format(d))
elif(d==2):
    print("\t{} is TWO".format(d))
elif(d==3):
    print("\t{} is THREE".format(d))
elif(d==4):
    print("\t{} is FOUR".format(d))
elif(d==5):
    print("\t{} is FIVE".format(d))
elif(d==6):
    print("\t{} is SIX".format(d))
elif(d==7):
    print("\t{} is SEVEN".format(d))
elif(d==8):
    print("\t{} is EIGHT".format(d))
elif(d==9):
    print("\t{} is NINE".format(d))
elif(d>9):
    print("\t{} is a Number".format(d))
elif d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("\t{} is -VE Digit".format(d))
elif d<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("\t{} is -VE Number".format(d))
print("Program Execution Completed")