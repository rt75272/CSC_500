class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity  = item_quantity

    def print_item_cost(self):
        print(f"${self.item_price:.2f}")


items = []
for i in range(2):
    name = input("\nEnter the item name: ")
    cost = float(input("Enter the item price: "))
    quantity = int(input("Enter the quantity: "))
    item = ItemToPurchase(name, cost, quantity)
    items.append(item)

# item_1 = ItemToPurchase("Chocolate Chips", 3, 1)
# item_2 = ItemToPurchase("Bottled Water", 1, 10)

total_cost = (items[0].item_price * items[0].item_quantity) + (items[1].item_price * items[1].item_quantity)

items[0].print_item_cost()
print(f"${total_cost:.2f}")