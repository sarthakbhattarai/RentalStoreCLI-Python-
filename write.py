""" 
This function is created to write the bill in the txt file format
here the function write is created in a way the all the write function is carried ou here
"""
#The function write is created
def write(fileName, item):
    try:
        #the file is open in written mode
        with open(fileName, 'w') as file:
            for equip in item:
                line = f"{equip['sNumber']}, {equip['name']}, {equip['brand']}, ${equip['price']}, {equip['quantity']}\n"
                file.write(line)
    
    except:
        print("Error: The file is not found")
