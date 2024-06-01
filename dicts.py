def create_inventory(items):
    inventario = dict()
    for item in items:
        if item in inventario.keys():
            cantidad = inventario[item] + 1
        else:
            cantidad = 1

        inventario[item] = cantidad
    return inventario

def add_items(inventory, items):

    for item in items:
        if item in inventory.keys():
            cantidad = inventory[item] + 1
        else:
            cantidad = 1

        inventory[item] = cantidad
    return inventory

def decrement_items(inventory, items):

    for item in items:
        if item in inventory.keys():
            cantidad = inventory[item] - 1
        else:
            cantidad = 1

        inventory[item] = cantidad
    return inventory

def remove_item(inventory, item):

    if item in inventory.keys():
        del inventory[item]

    return inventory

def list_inventory(inventory):
   inventory_list = list()

    for key in inventory:
        if not inventory[key]: continue
        inventory_list.append((key, inventory[key]))

    return inventory_list
