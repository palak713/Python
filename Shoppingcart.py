cart=[]
def additems(items):
     cart.append(items)
     print(f"Your item is added {items}")
def removee(items):
     try :
       cart.remove(items)
       print(f"Your item is removed from cart {items} and now your cart contain {showcart()}")
     except:
         print("Sorry that item is not in your cart so you can't remove {items}")
def clearcart():
      cart.clear()
      print("Your cart is empty")
def showcart():
     for i in cart:
         print(i,"\n")


def main():
     done=False
     while not done:
         ans =input("quit/add/remove/show/clear").lower()
         if ans=='quit':
             print("Thanks for shopping")
             showcart()
             done=True
         elif  ans=="add":
              item=input("What would you like to add in the cart").title()
              additems(item)
         elif ans=="remove":
              item=input("What would you like to remove from the cart").title()
              removee(item)
         elif ans == "show":
             showcart()
         elif ans=="clear":
              clearcart()
         else:
             print("Sorry that was not in option try again")
main()
