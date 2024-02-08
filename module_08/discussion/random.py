class ItemToBuy:
    # Default constructor.
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description        

    def print_info(self):
        total = self.price * self.quantity
        print(
            f"{self.quantity} {self.name} @ ${self.price} {self.description} = ${total}"
        )

class Cart:
    # Default constructor
    def __init__(self, customer_name="none"):
        self.customer_name = customer_name
        self.cart_items = []

    # Adding to our array of cart items.
    def add_item(self, ItemToBuy):
        if(ItemToBuy.name != "none"):
            self.cart_items.append(ItemToBuy)
            print(f"{ItemToBuy.name} added to cart")
        else:
            print(f"Nothing added to cart :(")

    def remove_item(self, name="none"):
        found = False
        for item in self.cart_items:
            if item.name == name:
                self.cart_items.remove(item)
                found = True
                print(f"{name} has been removed")
                break 
            else:
                print("Item not found in cart. Nothing removed.")

    def show_cart(self):
        for item in self.cart_items:
            item.print_info()

def print_menu(cart):
    menu = ("\n\tMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "o - Output shopping cart\n"
            "q - Quit shopping\n"
    )
    command = ''
    while command != 'q':
        print(menu)
        if(command == 'a'):
            print("Add item")
        elif(command == 'r'):
            print("Remove item")
        elif(command == 'o'):
            print("Output cart")
        elif(command == 'q'):
            print("Shutting down")
        else:
            print("Something blew up")


# Pushing the big red button.
if __name__ == "__main__":
    x = ItemToBuy("Cookies", 5.99, 2, "Food")
    cart = Cart("Bob")
    cart.add_item(x)
    cart.show_cart()
    cart.remove_item(x.name)
    # x.print_info()