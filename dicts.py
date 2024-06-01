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
    nueva_lista = list() # nueva_lista = []
    for item in inventory.items():
        # item = ("coal", 7)
        elemento, cantidad = item
        # elemento : str
        # cantidaf : int
        if cantidad > 0: # cant mayor a 0
            nueva_lista.append(item) # [("fh", 3)]

    return nueva_lista
