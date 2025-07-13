# Program for accepting any digit and displaying its name
d = { 0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR",5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}
dig = int(input("Enter your Digit: "))  # Can be -ve, >9, etc.
res = (
    d.get(dig) if dig in d
    else "NUMBER" if dig > 9
    else "-VE DIGIT" if dig in [-1, -2, -3, -4, -5, -6, -7, -8, -9]
    else "-VE NUMBER"
)

print("{} is {}".format(dig, res))
