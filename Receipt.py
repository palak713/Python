print("Hello sir/mam")
l =int(input("Enter how many items you are purchasing"))
s=0
e={}
for i in range(0,l):
 r = input("Enter The product")
 p = int(input("Enter the price of that product"))
 e.update({r:p})
 s = s + p
print("*" * 40)
print("*" * 10, "PALAK STORE", "*" * 10)
print(" " * 10, " KAIMGANJ")
print("=" * 33)
print("product->->->->->->->->->->->->->->price")
for keys,values in e.items():
    print(f"{keys}               {values}")

print("="*33)
print(" "*10,"Total")
print(" "*10,s)
print("="*33)
print("Thanks for shopping with us")
print("*" *40)
