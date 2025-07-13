#program for accepting a value and decide whether It is +VE or -VE or Zero
#IfElifElseStmtEx1.py
value=float(input("Enter Any Numerical Value:")) # 10
if(value>0):
    print("\t{} is +VE Value".format(value))
elif(value<0):
    print("\t{} is -VE Value".format(value))
elif(value==0):
    print("\t{} is ZERO".format(value))
print("Program execution Completed")