""" 
this function display is created to display the equipment txt file in the table
"""
#A function is display is created which display the table
def display(item):
    print(":──────┬─────────────────────────────────────┬─────────────────────┬───────────────────┬──────────:")
    print("│ S.No │ Item Name                           │ Brand               │ Price (for 5 days)│ Quantity │")
    print("├──────┼─────────────────────────────────────┼─────────────────────┼───────────────────┼──────────┤")
    for equip in item:
        print("│ {:<4} │ {:<35} │ {:<20}│ ${:>16.2f} │ {:>8} │".format(
            equip['sNumber'], equip['name'][:35], equip['brand'][:20],
            equip['price'], equip['quantity']))
    print(":──────┴─────────────────────────────────────┴─────────────────────┴───────────────────┴──────────:")
