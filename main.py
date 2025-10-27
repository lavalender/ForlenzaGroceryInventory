def add_item(inventory, name, quantity):
    """
    Add a new item to the inventory.
    
    Args:
    inventory (dict): The current inventory
    name (str): The name of the item
    price (str): The price of the item
    quantity (str): The quantity of the item
    """
    inventory[name] = quantity
    print(f"{name} added to the inventory.")

def remove_item(inventory, item_name):
    """
    Remove an item from the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to remove
    """
    #converts input to uppercase and sets it to the variable item_name
    item_name.upper() == item_name
    del inventory[item_name]
    print(f"{item_name} removed from the inventory.")

def update_quantity(inventory, item_name, new_quantity):
    """
    Update the quantity of an item in the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to update
    new_quantity (str): The new quantity of the item
    """
    inventory[item_name] = new_quantity
    print(f"{item_name} quantity updated to {new_quantity}.")

def display_inventory(inventory):
    """
    Display all items in the inventory.
    
    Args:
    inventory (dict): The current inventory
    """
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for name in inventory:
            quantity = inventory[name]
            print(f"{name}: Quantity: {quantity}")

# Initialize inventory with two example items
inventory = {
    "apple": 100,
    "banana": 150
}

while True:
    print("\n1. Add item\n2. Remove item\n3. Update quantity\n4. Exit")
    print("")
    display_inventory(inventory) #displays inventory throughout code use
    print("")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        add_item(inventory, name, quantity)
    elif choice == "2":
        name = input("Enter item name to remove: ")
        remove_item(inventory, name)
    elif choice == "3":
        name = input("Enter item name to update: ")
        quantity = input("Enter new quantity: ")
        update_quantity(inventory, name, quantity)
    elif choice == "4": #removed option to view inventory
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")