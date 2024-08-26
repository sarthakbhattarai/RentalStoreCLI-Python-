#This is opreation.py
#This carried out all the opreation that are required
""""
In this function all the operation is carried out as required.
Here we have three main function they are rentItems,reurnItems and findItems
In the rentItem we have carried out all the calculation anf function required to rent the item
In the returnItem we have carried out all the calculation anf function required to return the item
In the findItem we have checekd the serial number to carry all the details of that item.
"""
import datetime
import time
import write
from datetime import date

itemNotFound=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                            Item is not found
                                                 Thank You
    -------------------------------------------------------------------------------------------------------------------
    """

outOfStock=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                            Item is out of Stock
                                                 Thank You
    -------------------------------------------------------------------------------------------------------------------
    """
durationQty=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                        Invalid input! Rental duration and quantity must be positive.(greater than 0)
                                                 Thank You
    -------------------------------------------------------------------------------------------------------------------
    """             
#this is the rentItem function specialized in renting items        
def rentItem(item, customerName,customerAddress,customerNumber):
    #here I have used the try except concept to handle the exception
    try:
        sNumber = int(input("To rent the product please enter the Serial Number of that product: "))# converted the input value of user into int
          #calling the function to check the item   
        equip = findItem(item, sNumber)
        reviewItem = f"""
        -------------------------------------------------------------------------------------------------------------------                       
                        You want to rent item {equip['name']} with quantity price of {equip['price']}
        ------------------------------------------------------------------------------------------------------------------- 
        """
        print(reviewItem)
        if equip is None:
            print(itemNotFound)#if the item is not found in the list it display this
            return

        if equip['quantity'] == 0:
            print(outOfStock)
            return
        
        rentalDuration = int(input(f"Enter the number of days you want to rent {equip['name']}: "))# converted the input value of user into int
        itemQuantity=int(input(f"Enter the quantity of {equip['name']} you want to rent: "))
        if itemQuantity<=0 or rentalDuration<=0:
            print(durationQty)
            return
        
        if equip['quantity'] < itemQuantity:
            print(outOfStock)
            
            return
        #As 1 working day = 5 so the rental duration is divide by the 5 and quotent is stored in variable
        duration=int(rentalDuration/5)
         #cheacking weather the rentalDuration is divided by 5 if it os than 0 is add to duration or else 1 is added to duration
        if rentalDuration %5 ==0:
            duration +=0
        else:
            duration +=1
        #all the calculation begins here
        valueAddedTax=0.13  
        amount = equip['price'] * duration * itemQuantity
        vatAmount=amount*valueAddedTax 
        totalAmount = amount + vatAmount
        rentalDate = datetime.date.today().strftime("%Y-%m-%d")
        
        # A format for the bill has been created
        billFormat= f"""    
    -------------------------------------------------------------------------------------------------------------------
                                            Sarthak Rental store
    -------------------------------------------------------------------------------------------------------------------                   
                                                Rental Bill                       Date: {rentalDate}
    -------------------------------------------------------------------------------------------------------------------                                                                                            
                           Customer Name: {customerName}                                                                        
                           Customer Address: {customerAddress}                                                                     
                           Customer Number: {customerNumber}                                                                      
     ------------------------------------------------------------------------------------------------------------------- 
                           Item Name : {equip['name']}
                           Item Brand: {equip['brand']}
              Item per quantity price: {equip['price']}
                        Item Quantity: {itemQuantity}
                      Rental Duration: {rentalDuration}
                             Duration: {duration}   (As 1 working days = 5 days) 
                               Amount: {amount}
                           VAT Amount: {vatAmount}                                                                                  
    -------------------------------------------------------------------------------------------------------------------
                           Grand Total: {totalAmount}
    -------------------------------------------------------------------------------------------------------------------                       
                                                Thank You
    -------------------------------------------------------------------------------------------------------------------
                        
"""
        equip['quantity'] -= itemQuantity # the quantity has been decreased as the item has been rented
        write.write("equipment.txt", item)# updating the file

        miliSecond = int(time.time() * 1000)
        billName = f"{customerName.replace(' ', '_')}_rental_invoice{miliSecond}.txt"#createing the billName for the txt file
        with open(billName, 'w') as file:
            file.write(billFormat)#wrintin the bill in txt file

        print("Item rented successfully.")
        print(billFormat)
    
    except:
        print("Error: Please fill the requirement in proper way")# when the exception comes it will display this
   
    
def returnItem(item, customerName):
    try:
        
        sNumber = int(input(f"Enter the serial number of  the equipment you want to return: "))
        #calling the function to check the item 
        equip = findItem(item, sNumber)
        #checking weather the eqquipment is available or not
        if equip is None:
            print(itemNotFound)
            return
        reviewItem = f"""
    -------------------------------------------------------------------------------------------------------------------                       
                    You want to return item {equip['name']} with quantity price of {equip['price']}
    ------------------------------------------------------------------------------------------------------------------- 
        """
        print(reviewItem)
        #asking the user to input the values
        returnDate = datetime.date.today().strftime("%Y-%m-%d")
        itemQuantity=int(input(f"Enter the number of the quantity of {equip['name']} you want to Return: "))
        rentalDuration =  int(input(f"Enter the number of days for which you rented the {equip['name']} accordingly to the rent bill: "))
        
        
        #checkin the value od itemQuantity and rentalDuration
        if itemQuantity<=0 or rentalDuration<=0:
            print(durationQty)
            return
            
        
        finePerDay = 0.2 #20% of the item price
        #Asking the user to input the rented date
        rentalDateComponent= input("Enter the rented date from the rent bill in format of YYYY-MM-DD: ").split('-')
        #storing the rented date in the variable
        year,month,day=[int(item) for item in rentalDateComponent]
        #creating the date from the variable
        rentalDate=date(year,month,day)
        #calculating the late 
        late = (datetime.date.today() - rentalDate).days
        #checking weather late is greater equal or lesser than rentalDuration and calculating the days  late
        if late<=rentalDuration:
            daysLate=0
        else:
            daysLate=late-rentalDuration
        #calculating the fine with out vat    
        fine = (finePerDay * daysLate * itemQuantity*equip['price'])
        
        duration=int(rentalDuration/5)
        
        if rentalDuration %5 ==0:
            duration +=0
        else:
            duration +=1
        #calculatin begins   
        valueAddedTax=0.13 
        amount = equip['price'] * duration * itemQuantity
        vatAmount=amount*valueAddedTax 
        fineAmount=fine + fine*valueAddedTax
        totalAmount = amount + vatAmount +fineAmount
        #creating the bill format of return
        returnFormat= f"""    
    -------------------------------------------------------------------------------------------------------------------
                                            Sarthak Rental store
    -------------------------------------------------------------------------------------------------------------------                   
                                                Return Bill                       Date: {returnDate}
    -------------------------------------------------------------------------------------------------------------------                                                                                            
                           Customer Name: {customerName}                                                                     
    ------------------------------------------------------------------------------------------------------------------- 
                           Item Name : {equip['name']}
                           Item Brand: {equip['brand']}
              Item per quantity price: {equip['price']}
                        Item Quantity: {itemQuantity}
                      Rental Duration: {rentalDuration}
                            Days Late: {daysLate}
                         Fine Per Day: {finePerDay*100}% of Item price
                                 Fine: {fine}
                               Amount: {amount}
                    Total Fine Amount: {fineAmount}
                           VAT Amount: {vatAmount}                                                                                  
    -------------------------------------------------------------------------------------------------------------------
                           Grand Total: {totalAmount}
    -------------------------------------------------------------------------------------------------------------------                       
                                                Thank You
    -------------------------------------------------------------------------------------------------------------------                       
                        
"""

        equip['quantity'] += itemQuantity# Increasing the quantity as it has been returned
        write.write("equipment.txt", item)# updating the file
        miliSecond = int(time.time() * 1000)
        returnName = f"{customerName.replace(' ', '_')}_return_invoice{miliSecond}.txt"#createing the billName for the txt file
        with open(returnName, 'w') as file:
            file.write(returnFormat)#the return filr is written
            
        payTemplete=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                    Item returned successfully.
                                            Thank You
    ------------------------------------------------------------------------------------------------------------------- 
        """
        
        print(returnFormat)#printing the return bill
        pay=input("If you want to clear the bill please enter yes or else enter no: ")
        if pay.lower()=="yes":
            print(payTemplete)
            write.write("equipment.txt", item)
            with open(returnName, 'w') as file:
                file.write(returnFormat)#the return filr is written
        else:
            print("Clear the bill")
        
    except:
        print("Error: Please fill the requirement in proper way")# when the error comes it will display this
        
       
        
        
#this function is created check the item is there or
def findItem(item, sNumber):
    try:
        for equip in item:
            if equip['sNumber'] == sNumber:
                return equip
        return None
    except:
        print("Error: the file is not found")


    
