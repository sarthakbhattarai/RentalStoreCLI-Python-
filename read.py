""" 
Here the function read is created which read the txt file and stor the value od the txt file in the list which after store teh dictionary.
Here the the list id the list of dictionary which normally known as the 2D list
"""
#function read is created where all the function is carried out
def read(fileName):
    item=[]#a list is initilize
    try:
        #here the text file is open in the read mode
        with open(fileName,'r') as file:
            #loop start to read the each line of txt file
            for line in file:
                #the line is splitted by , and store in data
                data= line.strip().split(', ')
                # a dictionar is created it stores the key and the value respectivel
                equip={
                    'sNumber' : int(data[0]),
                    'name': data[1],
                    'brand': data[2],
                    'price': float(data[3].replace('$', '')),
                    'quantity': int(data[4])
                }
                #the dictionary is appended in the item list
                item.append(equip)
            #return the value of item to the function    
            return item
    except:
        print("Error: The file not found")