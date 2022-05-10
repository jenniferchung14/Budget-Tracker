####################################################################
# Program Name: Budget Tracker
#
# Problem: People use multiple methods of payments to purchase
#          different items which can get a bit messy when trying 
#          to keep tabs on how you are doing with budgeting, 
#          whether you have went over your goal or not, and how 
#          much in total you have spent over time with all the
#          purchases you have made. For people with credit and
#          debit card they have income statements, but when paying
#          with cash they may lose track of how much they have spent
#          in total when combined with the other purchases they 
#          have made with their debit/credit cards.
#
# Description: A program that allows user to input all their 
#              purchases and checks weather they have gone over
#              their intended budget goal that they have set, as
#              well as keeps track of the total amount they have
#              spent on all purchases of any sort of payment type.
####################################################################

from datetime import * #allows access to the entire datetime library 

paymentType = ["Cash", "Credit Card", "Debit Card", "Giftcard", "Other"]
category = ["Bills", "Rent", "Bus", "Uber", "Grocery", "Food", "Clothes", "Hygiene", "Entertainment", "Gift", "Technology", "School Supplies", "Tuition", "Travel", "Other"]
paymentList = []
categoryOfItemsList = []
purchases = []
priceList = []
dateList = []

#instructs user on what the program is about
print("Welcome!! This program is meant to help keep you keep track of your purchases and the how much you are are spending.")
print("You can use this program at the end of the month to see how you did with your budget goal and what the total amount\nof money you have spent on all your purchases are or even at the end of a week or day.")
print("With this program you can keep yourself a little more organized with your financial side, where you are able to\nsee all your purchases in one list instead of flipping through multiple receipts and statements and pulling out a\ncalculator to do calculations.")
print("You will be prompted to ask answer multiple questions regarding your purchases which will then allow all the purchases\nyou entered to be displayed as a list in the end, as well as the total you spent and how you did regarding keep up with\nyour budget goal if you had one.")

#asks user for name then greets user
nameOfUser = input("\nPlease enter your name: ")
print("\nNice to meet you " + nameOfUser + "!")

goalChoice = input("\nDo you have a budget goal? Please enter 'Y' for yes and 'N' for no: ")
goalChoice = goalChoice.upper()

#while loop to ask user to input the goal choice until they pick Y for yes or N for no if they are inputting something else
while(goalChoice != "Y" and goalChoice != "N"):
    goalChoice = input("\nIt seems you have put an invalid input. Please try again. Enter 'Y' for yes and 'N' for no: ")
    goalChoice = goalChoice.upper()

#if the user picks yes for goalchoice, program will ask for the user's budget goal amount
if goalChoice == "Y":
    budgetGoal = float(input("\nPlease enter the amount of your budget goal: $"))

#function that checks whether their purchase date is a valid date or not and makes sure that the date isn't a future date
def dateChecker():
    dateOfPurchase = input("\nPlease enter the day you spent the item on in the format dd/mm/yy: ")
    currentDate = date.today()       
    isValidDate = True
   
    try: 
        datetime.strptime(dateOfPurchase, "%d/%m/%y")
    except ValueError:
        isValidDate = False

    #will repeatedly ask for date until user inputs a valid date
    while(isValidDate == False or (isValidDate == True and datetime.strptime(dateOfPurchase, "%d/%m/%y").date() > currentDate)): 
        print("\nIt seems you have entered an invalid date. Remember that you can't put a date ahead of the current date and it must be in the format of dd/mm/yy. Please try again.")
        dateOfPurchase = input("Please enter the day you spent the item on in the format dd/mm/yy: ")
        isValidDate = True
        try: 
            datetime.strptime(dateOfPurchase, "%d/%m/%y")
        except ValueError:
            isValidDate = False
    
    #adds the valid date that the user inputted to the master list that stores all the dates of purchases
    if(isValidDate):
        dateList.append(dateOfPurchase)

#function that displays the type of categories the user's purchase may be
def displayCategory():
    print("\n")

    for i in range(len(category)):
        print(str(i+1) + ". " + category[i])

#function that asks the user to choose the category that corresponds to their item they purchased then adds the user's valid choice into the cateogory list which will store the categories of each item purchase
def categoryOfItem(): 
    choiceOfCategory = input("\nEnter the number corresponding to the category of item you purchased (e.g enter 1 if the item was bills related): ")
    categoryNumChoices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    
    #if the user inputs an invalid choice, program will repeatedly asks which category their purhcase belongs in until the choice made is one that is in the list
    while(choiceOfCategory not in categoryNumChoices):
        print("\nIt seems you have entered an invalid input. Please try again.")
        choiceOfCategory = input("Enter the number corresponding to the category of item you purchased (e.g enter 1 if the item was bills related): ")

    #adds the user's choice into the master list that stores the category of purchase for each of the entries made
    for i in range(1, len(category)+1):
        if choiceOfCategory == str(i):
            categoryOfItemsList.append(category[i-1])

#function that asks user to write down the name of the items or any notes about the purchase, then adds whatever the user writes in the master list that stores all the names/notes the user made for each purchase
def nameOfItem():
    itemName = input("\nEnter the name of the item you purchased or any notes you would like to include about the item: ")
    purchases.append(itemName)

#function that displays all the payment type options that the user may have used to make their purchase
def displayPaymentType():
    print("\n")

    for i in range(len(paymentType)):
        print(str(i+1) + ". " + paymentType[i])

#function that asks user to pick the payment type they used to make purchase, then add to list that stores what type of payment type they used to make their purchases
def paymentChoiceOfItem():
    choiceOfPayment = input("\nEnter the number corresponding to the payment you used to purchase the item (e.g enter 1 if you used Cash): ")
    paymentNumChoices = ["1", "2", "3", "4", "5"]

    #if the user inputs an invalid choice, program will repeatedly asks what payment type they used to make their purchase until the choice made is one that is in the list
    while(choiceOfPayment not in paymentNumChoices):
        print("\nIt seems you have entered an invalid input. Please try again.")
        choiceOfPayment = input("Enter the number corresponding to the payment you used to purchase the item (e.g enter 1 if you used Cash): ")
    
    #adds the user's choice into the master list that stores the payment method they used for each of the entries made
    for i in range(1, len(paymentType)+1):
        if choiceOfPayment == str(i):
            paymentList.append(paymentType[i-1])

#function that asks user the amount they spent on their purchase then adds it to the master list that stores the amount they spent for each of their purchase
def priceOfItem():
    price = float(input("\nEnter the price of the item you purchased: $"))
    while(price < 0):
        print("\nIt seems you have entered an invalid input. Please try again.")
        price = float(input("\nEnter the price of the item you purchased: $"))
    priceList.append(price)

#function that keeps track of the total amount of money spent on all the purchases
def totalPriceofItems():
    total = 0.0

    for i in range(len(priceList)):
        total += priceList[i]
    return round(total, 2)

#function that shows how user did with their budget goal and whether they have gone over, were close to breaking the goal or spent safely within the goal
def budgetTracker():
    remaining = 0.0

    if goalChoice == "Y":
        remaining = round(budgetGoal - totalPriceofItems(),2)
        if remaining < 0:
            print("\nYou have broken your budget goal sadly :(")
            print("You have gone $" + str(abs(remaining)) + " over your budget goal.")
        elif remaining == 0:
            print("You have spent exactly the amount of your budget goal.")
        elif remaining <= 10.00:
            print("\nWARNING!!!" + "\nYou are close to breaking your budget watch out.\nYou are $" + str(remaining) + " away from breaking your budget goal!")
        else:
            print("\nYou still have $" + str(remaining) + " reamining before you break your budget goal.")

#function that lists out all the inputted purchases the user made in a list format, as well as the total of all the purchases together
def displayAllPurchases():
    lengthOfItems = []
    print("\n")

    for i in range(1, len(purchases)+1):
        purchaseInfo = str(i) + ". " + str(purchases[i-1]) +  " [" + str(categoryOfItemsList[i-1]) + "] - Paid by " + str(paymentList[i-1]) + " ($" + str(priceList[i-1]) + ") - " + str(dateList[i-1])
        lengthOfItems.append(len(purchaseInfo))
        print(purchaseInfo)
    print("-"*max(lengthOfItems))
    print("TOTAL: $" + str(totalPriceofItems()))

#function that asks user if they want to enter another entry
def again():
    another = input("\nDo you want to enter another entry? Enter Y for yes and N for no: ")
    another.upper()

    while (another != "Y" and another != "N"):
        print("It seems you have entered an invalid input")
        another = input("\nDo you want to enter another entry? Enter Y for yes and N for no: ")
        another.upper()

    #if user wants to make another entry, the process for entering the infomation of their purchase will repeat 
    while(another == "Y"):
        dateChecker()
        displayCategory()
        categoryOfItem()
        nameOfItem()
        displayPaymentType()
        paymentChoiceOfItem()
        priceOfItem()
        another = input("\nDo you want to enter another entry? Enter Y for yes and N for no: ")
        another.upper()
    
    #once user no long wants to make any more entries, program calls the functions to display all the purchases the user made and how they did budget wise if they had one
    displayAllPurchases()
    budgetTracker()
    print("\nHave a nice day! Bye bye :)")

#calls all the functions needed to gather the information of the user's purchases
dateChecker()
displayCategory()
categoryOfItem()
nameOfItem()
displayPaymentType()
paymentChoiceOfItem()
priceOfItem()
again()