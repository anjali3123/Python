num1 = 10
num2 = num1

if num1 == num2:
    print("Same Value.")
else:
    print("Not Same Value.")
if id(num1) == id(num2):
    print("Same Adress.")
else:
    print("Not Same Adress.")

print("Value Of Numbre 1 :",num1)
print("Value Of Numbre 2 :",num2)
print("Adress Of Numbre 1 :",id(num1))
print("Adress Of Numbre 1 :",id(num2))
