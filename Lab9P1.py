def add_item(item_list) :
    User_input = input("Enter item: ")
    if User_input in item_list :
        print("Item is already in the list")
    else :
        item_list.append(User_input)
        print("Item has been added")


def change_item(item_list) :
    User_input = input("Enter item you want to change: ")
    if User_input in item_list :
        User_input_2 = input("Enter new item: ")
        Position = item_list.index(User_input)
        item_list.remove(User_input)
        item_list.insert(Position,User_input_2)
        print("Item has been changed")
    else :
        print("Item is not in the list")


def insert_item(item_list) :
    User_input = input("Enter item: ")
    Position = int(input("Enter location that you want to insert: "))
    item_list.insert(Position,User_input)
    print("Item has been inserted")


def remove_item(item_list) :
    User_input = input("Enter item you want to remove: ")
    if User_input in item_list :
        item_list.remove(User_input)
        print("Item has been removed")
    else :
        print("This item is not in the list")


def show_item(item_list) :
    if len(item_list) == 0 :
        print("The list is curently empty")
    else :
        print(item_list)


main_list = []
Text = """What would you like to do?
1: add item
2: change item
3: insert item
4: remove item
5: show items
6: exit"""
print(Text)
Choice = 0
while Choice != "6" :
    Choice = input("Enter a number: ")
    if Choice == "1" :
        add_item(main_list)
    elif Choice == "2" :
        change_item(main_list)
    elif Choice == "3" :
        insert_item(main_list)
    elif Choice == "4" :
        remove_item(main_list)
    elif Choice == "5" :
        show_item(main_list)
    elif Choice == "6" :
        continue