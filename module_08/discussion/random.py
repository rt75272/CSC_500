class ItemToBuy:
    # Default constructor.
    def __init__(self, name="none", price="0.0", quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description        

    def print_info(self):
        total = self.price * self.quantity
        print(f"{self.name}")