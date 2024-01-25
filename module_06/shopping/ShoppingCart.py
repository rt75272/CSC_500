class ShoppingCart:
    cart_items = []
    def __init__(self, current_name="none", customer_date="January 1, 2020"):
        self.current_name = current_name
        self.customer_date = customer_date

    # Adds an item to cart_item list.
    # Returns none.
    def add_item(ItemToPurchase):
        cart_items.append(ItemToPurchase)

    # Removes item from cart_items list
    # Returns none.
    def remove_item(item_name="none"):
        if cart_items.remove(item_name):
            print(f"{item_name} has been removed")
        else:
            print("Item not found in cart. Nothing removed.")
    
    # Modifies an item's description, price, and/or quantity.
    # Returns none.
    def modify_item(ItemToPurchase):
        return 0
    
    # Returns quantity of all items in cart.
    def get_num_items_in_cart():
        return len(cart_items)
    
    # Determines and returns the total cost of items in cart.
    def get_cost_of_cart():
        total_cost = 0
        for item in cart_items
            total_cost += item.item_price()
        return total_cost
    
    # Outputs total of objects in cart.
    def print_total():
        for item in cart_items:
            print(item)
        
    # Outputs each item's description.
    def print_descriptions()
        for item in cart_items:
            print(item.item_name)