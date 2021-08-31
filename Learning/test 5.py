
def addToInventory(inventory, addedItems):
    fj = 0
    for add in addedItems:
        inventory.setdefault(add,0)
        inventory[add] += 1
    for c, k in inventory.items():
            print(str(k) + ' ' + c)
    for ffj in inventory.values():
        fj += ffj
    return fj

def displayInventory(addj):  
    print()     
    print('Total number of items is ' + str(addj))



inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',]


print('Inventory:')
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)