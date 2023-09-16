price = int(input("Enter the price of the item"))
name_of_item = input("Enter the name of item you want to purchase")
credit_status = bool(input("do you have good credit status? if yes type 1 or ignore "))
if credit_status:
    print("""
        *********************
            INVOICE 
        *********************
    """)
    print('Name of item:', name_of_item)
    print('Discount:', '10%')
    print('Deposit:', price - 10 * price / 100)
else:
    print("""
            *********************
                INVOICE 
            *********************
         """)
    print('Name of item:', name_of_item)
    print('Discount:', "0")
    print('Deposit:', price - 25 * price / 100)
