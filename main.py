"""
This main.py is created as the main.py
All the function is called here and all the displaying work to the user is done here
All the function is carried out in the main function
"""

import re
import display
import opreation
import read

#A function is created in a way thet all the function is carried out here
def main():
    #a banner is declaeared and the stylish format of the name is stored
    banner="""
        
░██████╗░█████╗░██████╗░████████╗██╗░░██╗░█████╗░██╗░░██╗  ██████╗░███████╗███╗░░██╗████████╗░█████╗░██╗░░░░░
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║░░██║██╔══██╗██║░██╔╝  ██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔══██╗██║░░░░░
╚█████╗░███████║██████╔╝░░░██║░░░███████║███████║█████═╝░  ██████╔╝█████╗░░██╔██╗██║░░░██║░░░███████║██║░░░░░
░╚═══██╗██╔══██║██╔══██╗░░░██║░░░██╔══██║██╔══██║██╔═██╗░  ██╔══██╗██╔══╝░░██║╚████║░░░██║░░░██╔══██║██║░░░░░
██████╔╝██║░░██║██║░░██║░░░██║░░░██║░░██║██║░░██║██║░╚██╗  ██║░░██║███████╗██║░╚███║░░░██║░░░██║░░██║███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

░██████╗████████╗░█████╗░██████╗░███████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝
    """
    #a file is read 
    item = read.read("equipment.txt")
    #a banner is printed
    print(banner)
    
    loop=True #a variable is decleared and boolean value is stored to run the loop
    #here the choices stored the stylish display of choices for user
    choices=f"""    
    -------------------------------------------------------------------------------------------------------------------
                                             Sarthak Rental store
    -------------------------------------------------------------------------------------------------------------------                   
                                         Welcome to Sarthak Rental Stores
    -------------------------------------------------------------------------------------------------------------------                                                                                            
                                Please Read the details and make choice Accordingly                                                                    
    ------------------------------------------------------------------------------------------------------------------- 
                           Please enter 1 if you want to make a look what items we rent.
                           Please enter 2 if you want to rent the  item.
                           Please enter 3 if you want to return item that you rented.
                           Please enter 4 if you want to make a exit.
    -------------------------------------------------------------------------------------------------------------------
                            Note: You can rent a one type of item at once  (sorry for inconvenience)                                                                                                    
    -------------------------------------------------------------------------------------------------------------------
                                                Thank You
    -------------------------------------------------------------------------------------------------------------------                    
"""
    #a variable thank you is store to dislpay when the user ecit
    thankYou=f"""
    -------------------------------------------------------------------------------------------------------------------
                                             Sarthak Rental store                 
    -------------------------------------------------------------------------------------------------------------------                       
                                            Hope to see you soon    
                                                Thank You
    -------------------------------------------------------------------------------------------------------------------
"""

    check=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                            Your name contain special character or numeric value...
                                       Please check it and make it correct
                                                    or
                      You can also use the removed of numeric value or special character from our software
                        If you want to check the name from our software please press 1 or else press 0
                                                  Thank You
    -------------------------------------------------------------------------------------------------------------------
    """
    
    check1=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                        If you want to use the software corrected name please press 1 or else press 0
                                                 Thank You
    -------------------------------------------------------------------------------------------------------------------
    """
    
    checkAddress=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                    Your Address contain special character...
                                       Please check it and make it correct
                                                    or
                            You can also use the removed of special character from our software
                        If you want to check the address from our software please press 1 or else press 0
                                                  Thank You
    -------------------------------------------------------------------------------------------------------------------
    """
    
    checkAddress1=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                        If you want to use the software corrected address please press 1 or else press 0
                                                 Thank You
    -------------------------------------------------------------------------------------------------------------------
    """
    #loop begins from here
    while loop==True:
    
        print(choices)
        try:
            #choice is asked to the user
            userChoice = int(input("Enter Your Choice: "))

            if userChoice == 1:
                display.display(item)#this will display the item
            elif userChoice == 2:
                try:
                    while True:
                        customerName = input("Enter your name: ")
                    # customerName=re.sub(r'[^a-zA-Z\s]', '', customerName)
                    
                        if re.search(r'\d', customerName) or re.search(r'[!-@#$%^&*()_+{}\[\]:;<>,.?~\\|]', customerName):
                            print(check)
                            yourChoice=int(input("Please enter your choice: "))
                        
                            if yourChoice==1:
                                # print("Your entered name: ",customerName)
                                customerName1=re.sub(r'[^a-zA-Z\s]', '', customerName)
                                # print("Corrected Name from software: ",customerName)
                                changeName=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                        Your Entered Name is {customerName}
                                    Software Corrected Name is {customerName1}
                                                Thank You
    -------------------------------------------------------------------------------------------------------------------
    """ 
                                print(changeName)
                                customerName=re.sub(r'[^a-zA-Z\s]', '', customerName)
                                print(check1)
                                yourChoice1=int(input("Please enter your choice: "))
                                if yourChoice1==1:
                                    print()
                                    break
                                elif yourChoice1==0:
                                    print()
                                    
                                else:
                                    print("Please enter the valid choice")
                                    yourChoice1=int(input("Please enter your choice: "))
                        
                            elif yourChoice==0:
                                print()
                            else:
                                print("Please enter the valid choice")
                                yourChoice=int(input("Please enter your choice: ")) 
                        else:
                            break  
                    
                    customerName=customerName.split()
                    customerName="".join(customerName)         
                    name=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                    Your Name is taken as {customerName}
                                                Thank You
    -------------------------------------------------------------------------------------------------------------------
    """     
                    print(name)
                    while True:
                        customerAddress = input("Enter your Address: ")
                    
                        if re.search(r'[!@#$%^/&*()_+{}\[\]:;<>,.?~\\|]', customerAddress):
                            print(checkAddress)
                            yourChoiceAddress=int(input("Please enter your choice: "))
                        
                            if yourChoiceAddress==1:
                                # print("Your entered address: ",customerAddress)
                                customerAddress1=re.sub(r'[^\w\s]', '', customerAddress)
                                # print("Corrected Address from software: ",customerAddress)
                                
                                changeAddress=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                    Your Entered Address is {customerAddress}
                                    Software Corrected Address is {customerAddress1}
                                                 Thank You
    -------------------------------------------------------------------------------------------------------------------
    """ 
                                print(changeAddress)
                                customerAddress=re.sub(r'[^\w\s]', '', customerAddress)
                                print(checkAddress1)
                                yourChoiceAddress1=int(input("Please enter your choice: "))
                                if yourChoiceAddress1==1:
                                    print()
                                    break
                                elif yourChoiceAddress1==0:
                                    print()
                                else:
                                    print("Please enter the valid choice")
                                    yourChoiceAddress1=int(input("Please enter your choice: "))
                            
                            elif yourChoiceAddress==0:
                                print()
                            
                            else:
                                print("Please enter the valid choice")
                                yourChoiceAddress=int(input("Please enter your choice: "))
                        else:
                            break
                    customerAddress=customerAddress.split()
                    customerAddress="".join(customerAddress)             
                    address=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                    Your Address is taken as {customerAddress}
                                                 Thank You
    -------------------------------------------------------------------------------------------------------------------
    """ 
                    print(address)  
                    
                    while True:          
                        customerNumber = int(input("Enter your Number: "))
                    
                        if len(str(customerNumber))==10: #this check weather the number of the user is valid or not
                            number=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                    Your Number is taken as {customerNumber}
                                                 Thank You
    -------------------------------------------------------------------------------------------------------------------
    """
                            print(number)
                            break
                        else:         
                            print("Invalid: please enter the number properly")
                    display.display(item)#display the item
                    opreation.rentItem(item, customerName,customerAddress,customerNumber)# call the rent function where all the function renting is carried out
                        
                except:
                    print("Please enter the number in numeric form")
            elif userChoice == 3:
                while True:
                    customerName = input("Enter your name: ")
                    # customerName=re.sub(r'[^a-zA-Z\s]', '', customerName)
                    
                    if re.search(r'\d', customerName) or re.search(r'[!-@#$%^&*()_+{}\[\]:;<>,.?~\\|]', customerName):
                        print(check)
                        yourChoice=int(input("Please enter your choice: "))
                        
                        if yourChoice==1:
                            # print("Your entered name: ",customerName)
                            customerName1=re.sub(r'[^a-zA-Z\s]', '', customerName)
                                # print("Corrected Name from software: ",customerName)
                            changeName=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                        Your Entered Name is {customerName}
                                    Software Corrected Name is {customerName1}
                                                Thank You
    -------------------------------------------------------------------------------------------------------------------
    """ 
                            print(changeName)
                            customerName=re.sub(r'[^a-zA-Z\s]', '', customerName)
                            print(check1)
                            yourChoice1=int(input("Please enter your choice: "))
                            if yourChoice1==1:
                                print()
                                break
                            elif yourChoice1==0:
                                print()
                                    
                            else:
                                print("Please enter the valid choice")
                                yourChoice1=int(input("Please enter your choice: "))
                        
                        elif yourChoice==0:
                            print()
                        else:
                            print("Please enter the valid choice")
                            yourChoice=int(input("Please enter your choice: ")) 
                    else:
                        break  
                    
                customerName=customerName.split()
                customerName="".join(customerName)         
                name=f"""
    -------------------------------------------------------------------------------------------------------------------                       
                                    Your Name is taken as {customerName}
                                                 Thank You
    -------------------------------------------------------------------------------------------------------------------
    """     
                print(name)
                opreation.returnItem(item, customerName) #calls the return function where all the returning process is carried out
            elif userChoice == 4:
                print(thankYou)#when the user exit it display thank you
                break
            else:
                print("Invalid choice! Please Enter again.")
        except:
            print("Invalid input! Please enter the correct input")
    

#here the main function is called
main()