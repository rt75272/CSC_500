class ItemToBuy:
    # Default constructor.
    def __init__(self, name="none", price="0.0", quantity=0, description="none"):
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

x = ItemToBuy("Cookies", 5.99, 2, "Food")
x.print_info()