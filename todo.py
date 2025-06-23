
# Simple todo list app
# Email: mki.devsoft@gmail.com

my_list = []

# check if any saved items on file
try:
    with open("listdata.txt", "r") as file:
        my_list = file.read().splitlines()
        file.close()
except:
    print('')

# print list 
def printList():
    print(my_list)

# add item to list
def addItem():

    item = input('Enter new item: ')
    my_list.append(item)
    print(item + " added to list")

# delete item from list
def deleteItem():
    item = input('Which item to delete: ')
    try:
        my_list.remove(item)
        print(item + " removed from list")
    except: 
        print(item + " not on the list")

# update value of item on list
def updateItem():
    old_item = input('item to update: ')
    location = my_list.index(old_item)
    new_item = input('enter new value: ')
    try: 
        my_list[location] = new_item
        print(old_item + " updated to " + new_item)
    except:
        print(old_item + " not in list")

# save current list to local file in project directory        
def saveList():
    with open("listdata.txt", "w") as file:
        for item in my_list:
            file.write(item + "\n")
    file.close()
    print('Your list has been saved!')

# display app menu
def showMenu():
    print('-' * 20)
    print('TODO List App')
    print('-' * 20)
    print('Menu')
    print('1: display list')
    print('2: add item to list')
    print('3: delete item from list')
    print('4: update item on list')
    print('0: Exit')

selection = -1
while (selection != 0):
    showMenu()
    try:
        selection = int(input('Enter a selection: '))
    except:
        print('Invalid selection. Try again')
    if (selection == 0):
        print('Thank you for using TODO List App')
        print('Goodbye!')
    elif (selection == 1):
        printList()
    elif (selection == 2):
        addItem()
    elif (selection == 3):
        deleteItem()
    elif (selection == 4):
        updateItem()
    else:
        print('wrong input. Make another selection')

saveList()
