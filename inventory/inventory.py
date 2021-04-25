#!/usr/bin/env python3
#! python3

playerStuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory")
    total_items = 0
    for k, v in inventory.items():
        total_items += inventory.get(k,0)
        print(str(v) + " " + k)
    print("Total number of items: " + str(total_items) + '\n')

displayInventory(playerStuff)

def addToInventory(inventory, addedItems):
    #add addedItems to inventory
    #addedItems is a list, inventory is a dictionary
    for item in addedItems:
        if item not in inventory.keys():
            inventory[item] = inventory.get(item,1)
        else:
            inventory[item] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(inv)
displayInventory(inv)    

input("Press ENTER to exit...")