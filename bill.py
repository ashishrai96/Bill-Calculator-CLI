import random


def display_menu():
    """
    The function reads from the Menu.csv file and displays as
    well as stores the Items No. and prices with respect to its
    plate types.

    Returns:
        list: prices of items with respect to plate types.
    """

    file_path = "Menu.csv"
    price_menu = []

    file_reader_stream = open(file_path, "r")
    for line in file_reader_stream:
        line = line.strip()
        line = line.split(',')
        print(f"{line[0]:^15} {line[1]:<15} {line[2]:<15}")
        item = {
            "item_no": line[0],
            "full_plate_price": line[2],
            "half_plate_price": line[1]
        }
        price_menu.append(item)

    file_reader_stream.close()
    return price_menu


def take_order():
    """
    The function stores ordered items to a list from user's input.
    Returns:
        list: ordered items
    """

    ordered_items = []
    done = "y"
    while(done == "y"):
        print("\nWhat would you like to add?")
        item_no = input("Please specify Item No: ")
        plate_type = input("Would you like to have Full plate or Half plate?" +
                           "[(Half (h) / Full (f)]: ")
        quantity = input("Enter Quanity : ")

        item = {
            "item_no": item_no,
            "plate_type": plate_type,
            "quantity": quantity
        }
        ordered_items.append(item)
        done = input("\nDo you wish to add another item? [y/n]: ")

    return ordered_items


def ask_for_tip():
    """
    The functions ask for tip data, as per user's will.

    Returns:
        number: tip value in float data type.
    """

    tip = 0
    if(input("Would you like to add some tip? [y/n]: ") == "y"):
        tip = input("Enter 1 for 10%\nEnter 2 for 20%\nYour Choice: ")
        if(tip == "1"):
            tip = 0.1
        elif(tip == "2"):
            tip = 0.2
        else:
            tip = 0

    return tip


def generate_bill(ordered_items, price_menu):
    """
    The function generates bill dictionary.

    Parameters:
        list: ordered items.
        list: price of items with respect to its plate types.

    Returns:
        dictionary: bill object
    """

    bill = {
        "gross_amount": 0,
        "final_amount": 0,
        "tip": 0,
        "increase": 0,
        "discount": 0,
        "items": []
    }

    for o_item in ordered_items:
        item = {
            "item_no": o_item["item_no"],
            "plate_type": o_item["plate_type"],
            "quantity": o_item["quantity"],
            "price": 0
        }
        for menu_item in price_menu:
            if(o_item["item_no"] == menu_item["item_no"]):
                if(o_item["plate_type"] == "h"):
                    item["price"] = int(menu_item["half_plate_price"]) * (
                        int(o_item["quantity"]))
                else:
                    item["price"] = int(menu_item["full_plate_price"]) * (
                        int(o_item["quantity"]))
                # break
        added = False
        for billed_item in bill.get("items"):
            if(item["item_no"] == billed_item["item_no"] and (
                    item["plate_type"] == billed_item["plate_type"])):
                billed_item["quantity"] = int(billed_item["quantity"]) + (
                    int(item["quantity"]))
                billed_item["price"] = float(billed_item["price"]) + (
                    float(item["price"]))
                added = True
        if(not added):
            bill.get("items").append(item)
        else:
            pass
        bill["gross_amount"] += int(item["price"])

    return bill


def get_bill_split_count():
    """
    The function asks and stores the people count in which the bill's
    total price would be divided.

    Returns:
        number: Number of people among whom the bill total amount
                to be divided
    """

    split_count = 1
    if(input("Would you like to split the bill amount? [y/n]: ") == "y"):
        split_count = input("How many people plan to split? : ")

    return split_count


def try_test_your_luck_game(total_amount):
    """
    The fucntion asks for user's input whether to plat the game.
    In case of yes, the random number is generated based on which the
    discount or the increase in price is displayed.

    Parameters:
        number: Total amount of the bill

    Returns:
        number: discounted price or increased value
                negative value in case of discount,
                positive value in case of increased value
    """

    if(input("Would you like to participate in the event - " +
             "'Test Your Luck'? [y/n]: ") == "n"):
        return 0

    rand_num = random.randint(1, 100)
    discount = 0
    if(rand_num <= 5):
        discount = -0.5
    elif(rand_num <= 15):
        discount = -0.25
    elif(rand_num <= 30):
        discount = -0.1
    elif(rand_num <= 50):
        discount = 0
    else:
        discount = 0.2

    discounted_price = 0.00
    if(discount < 0):
        discounted_price = float(total_amount) * discount
        print(f"\nGreat!! Your discounted price: {discounted_price:.2f}")
        for i in range(10):
            for j in range(14):
                if(i < 5):
                    if(i == 0 or i == 4) and (j < 4 or j > 9):
                        print("*", end="")
                    elif(i > 0 and i < 4) and (
                            (j == 0 or j == 3 or j == 10 or j == 13)):
                        print("|", end="")
                    else:
                        print(" ", end="")
                elif(i == 7 and j == 6):
                    print("{}", end="")
                elif(i == 9 and j > 3 and j < 10):
                    print("_", end="")
                else:
                    print(" ", end="")
            print()
    else:
        discounted_price = float(total_amount) * discount
        if(discount == 0):
            print(f"\nTough Luck!! Unfortunately, " +
                  "You could not avail any discount")
        else:
            print(f"\nTough Luck!! Unfortunately, Your " +
                  f"bill amount has been increased by {discounted_price}")
        for i in range(6):
            for j in range(6):
                if((i == 0 or i == 5) and (j == 0 or j == 5)) or (
                        (i > 0 and i < 5 and j > 0 and j < 5)):
                    print(" ", end="")
                else:
                    print("*", end="")
            print()

    return discounted_price


def display_bill(bill):
    """
    The function takes bill object/dictionary as an input, and
    display the bill in desired format.

    Parameters:
        dictionary: bill data
    """

    print("\nHere is your bill:\n")
    for item in bill["items"]:
        if(item['plate_type'] == "h"):
            item['plate_type'] = "half"
        else:
            item['plate_type'] = "full"

        print(f"Item {item['item_no']} " +
              f"[{item['plate_type']}] " +
              f"[{item['quantity']}]:{item['price']:.2f}")
    print(f"Total: {bill['gross_amount']:.2f}")
    print(f"Tip Percentage: {(float(bill['tip'])*100):.0f}%")
    print(f"Discount/Increase: {bill['discount']:.2f}")
    print(f"Final Total: {bill['final_amount']:.2f}")


# Main
"""
This is main entry point of the program.
"""

price_menu = display_menu()
ordered_items = take_order()
bill = generate_bill(ordered_items, price_menu)
tip = ask_for_tip()

bill["tip"] = tip
bill["final_amount"] = bill["gross_amount"] * (1 + tip)
print(f"\nThe total amount to be paid: {float(bill['final_amount']):.2f}")

split_count = get_bill_split_count()
each_person_share = float(bill["final_amount"]) / float(split_count)
if(int(split_count) > 1):
    print(f"\nEach person has to contribute: {each_person_share:.2f}")
else:
    print(f"\nA person has to contribute: {each_person_share:.2f}")


discount = try_test_your_luck_game(bill["final_amount"])
bill["discount"] = discount
bill["final_amount"] = float(bill["final_amount"]) + discount
display_bill(bill)
each_person_share = float(bill["final_amount"]) / float(split_count)
if(int(split_count) > 1):
    print(f"\nEach person has to contribute: {each_person_share:.2f}")
else:
    print(f"\nA person has to contribute: {each_person_share:.2f}")
