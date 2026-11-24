"""
COMP 1110 Fall 2026 Group Project
Group Members: Jacob Feser, Tadiwanashe Dondo, Munashe Isaac Chapoka
Everyday Useful Calculator
"""

from rich import print
import requests

# Global Variables Checked / called by the Log Function
times_called = 0


def main():
    """ Function # 1: The Main Function
    The Main method doubles as the Menu Function
    Author: Jacob Feser
    """
    print("COMP 1110 Project Fall 2026\nJacob Feser, Tadiwanashe Dondo, Munashe Isaac Chapoka")
    print("Select an Option (Type the Option Number to use that function):\n 1. [underline]L[/underline]oan Interest Calculator\n 2. [underline]U[/underline]nit Converter\n 3. u[underline]S[/underline]eful Car Details Calculator\n 4. [underline]C[/underline]urrency Converter\n 5. [underline]P[/underline]aint Area Calculator\n 6. [underline]D[/underline]iscount Calcuator\n 7. [underline]E[/underline]lectricity Cost Calcuator\n 0. e[underline]X[/underline]it")
    inputcode = "1"
    while True:
        inputcode = input("Code: ")
        match inputcode:
            case 'X':
                print("Exiting Program, Thank you for using [bold]The Everyday Calculator[/bold]")
                Log(1,"Menu","{inputcode}, Exit")
                break
            case '0':
                print("Exiting Program, Thank you for using [bold]The Everyday Calculator[/bold]")
                Log(1,"Menu","{inputcode}, Exit")
                break
            case 'L':
                print("Loan Interest Calculator Selected")
                Log(1,"Menu","{inputcode}, LIC")
                LoanInterest
            case '1':
                print("Loan Interest Calculator Selected")
                Log(1,"Menu","{inputcode}, LIC")
                LoanInterest
            case 'U':
                print("Unit Converter Selected")
                Log(1,"Menu","{inputcode}, UC")
                UnitConverter
            case '2':
                print("Unit Converter Selected")
                Log(1,"Menu","{inputcode}, UC")
                UnitConverter
            case 'S':
                print("Useful Car Details Calculator Selected")
                Log(1,"Menu","{inputcode}, CDC")
                CarDetails
            case '3':
                print("Useful Car Details Calculator Selected")
                Log(1,"Menu","{inputcode}, CDC")
                CarDetails
            case 'C':
                print("Currency Converter Selected")
                Log(1,"Menu","{inputcode}, CC")
                CurrencyConverter
            case '4':
                print("Currency Converter Selected")
                Log(1,"Menu","{inputcode}, CC")
                CurrencyConverter
            case 'P':
                print("Paint Area Calculator Selected")
                Log(1,"Menu","{inputcode}, PAC")
                Paint
            case '5':
                print("Paint Area Calculator Selected")
                Log(1,"Menu","{inputcode}, PAC")
                Paint
            case 'D':
                print("Discount Calculator Selected")
                Log(1,"Menu","{inputcode}, DC")
                Discount
            case '6':
                print("Discount Calculator Selected")
                Log(1,"Menu","{inputcode}, DC")
                Discount
            case 'E':
                print("Electricity Cost Calculator Selected")
                Log(1,"Menu","{inputcode}, ECC")
                ElectricityCost
            case '7':
                print("Electricity Cost Calculator Selected")
                Log(1,"Menu","{inputcode}, ECC")
                ElectricityCost
            


def LoanInterest():
    """Function # 2: The Loan Interest Calculator
    Author: Tadiwanashe Dondo
    """
    print(1)

def UnitConverter():
    """Function # 3: The Unit Converter
    Author: Tadiwanashe Dondo
    """

def CarDetails():
    """Function # 4: The Useful Car Details Calculator
    Author: Munashe
    """

def CurrencyConverter():
    """Function # 5: The Currency Converter
    Author: Jacob Feser
    """
    def checkcurrency(isocode):
        isocode = isocode.strip().upper()
        # print(isocode)
        codelist = []
        for i in range (1,len(codessplitup)):
            workingdic = (codessplitup[i])
            codelist.append(workingdic["code"].strip().upper())
            # print(codelist)
        for j in range (0,len(codelist),1):
            # print(f"{isocode} and {codelist[j]}")
            if isocode == codelist[j]:
                # print("Valid Code, continue.")
                return(True)
            # print(f"checked {j} codes")
        return(False)

    def getcurrencysymbol(isocode):
        isocode = isocode.strip().upper()
        for i in range (1,len(codessplitup)):
            workingdic = (codessplitup[i])
            if isocode == workingdic["code"]:
                return(workingdic["symbol"])

    def userentered(choice):
        if (choice == 1):
            inputone = input("Origin Currency (ISO Code): ").strip().lower()
            if (inputone == "help"):
                for i in range (1,len(codessplitup)):
                    workingdic = (codessplitup[i])
                    print(f"ISO code for {workingdic["name"]} is {workingdic["code"]}\nAsset Type: {workingdic["type"]}\n")
                print(f"To see this list again, type \"help\" again. Or, enter a source Currency Code.")
                return(None)
            elif (inputone == "x"):
                return(inputone,)
            else:
                if (checkcurrency(inputone) == False):
                    print("Please enter a valid ISO Code. \nIf you require a list of ISO codes, type \"help\"")
                    return(None)
                else:
                    inputonesymbol = getcurrencysymbol(inputone)
                    return(inputone,inputonesymbol)
        if (choice == 2):
            inputtwo = input("Target Currency (ISO Code): ").strip().lower()
            if (checkcurrency(inputtwo) == False):
                print("Please enter a valid ISO Code. \nIf you require a list of ISO codes, type \"help\"")
                return(None)
            else:
                inputtwosymbol = getcurrencysymbol(inputtwo)
                return(inputtwo,inputtwosymbol)
        if (choice == 3):
            inputthree = -1
            while float(inputthree) < 0:
                inputthree = input("Input amount of Origin Currency to be converted: ")
                if float(inputthree) < 0:
                    print("Invalid Input, please enter a non-negative amount.")
            return(inputthree)

    # Retrieve current list of currencies, create a list / dictionary of all available currencies

    currencylist = requests.get("https://api.frankfurter.dev/v2/currencies")

    currencylist = currencylist.text

    length = len(currencylist)
    listofbreaks = [0]
    codessplitup = {str:str}

    for i in range(1,length,1):
        if (currencylist[i-1] == "}" and currencylist[i] == "," and currencylist[i+1] == "{"):
            listofbreaks.append(i)
    listofbreaks.append(len(currencylist))

    splitbycurrency = []

    for k in range (0,len(listofbreaks)-1):
        splitbycurrency.append(currencylist[listofbreaks[k]:listofbreaks[k+1]])

    for i in range(0,len(splitbycurrency)):
        # Set the open line as a working handle (? I think that is what its called?)
        line = splitbycurrency[i]

        # Make sure all variable are reset
        codesubstring = ""
        namesubstring = ""
        currencycodelocation = 0
        currencycodelocationend = len(line)
        currencynamelocation = 0
        currencynamelocationend = len(line)

        # Find and extract the Currency Code (3 or 4 letters)
        currencycodelocation = line.find("code") + 7
        codesubstring = line[currencycodelocation:]
        currencycodelocationend = codesubstring.find(",") -1
        codesubstring = codesubstring[:currencycodelocationend]

        # Find and extract the Currency Name (various length)
        namesubstring = line[currencycodelocationend+currencycodelocation:]
        currencynamelocation = namesubstring.find("name") + 7
        namesubstring = namesubstring[currencynamelocation:]
        currencynamelocationend = namesubstring.find("\"")
        namesubstring = namesubstring[:currencynamelocationend]

        # Find and extract the Currency Symbol (various length)
        currencysymbollocation = line.find("symbol") + 9
        symbolsubstring = line[currencysymbollocation:]
        currencysymbollocationend = symbolsubstring.find(",") -1
        symbolsubstring = symbolsubstring[:currencysymbollocationend]

        # Find and extrac the type of Currency (various length)
        currencytypelocation = line.find("type") +7
        typesubstring = line[currencytypelocation:]
        currencytypelocationend = typesubstring.find(",") -1
        typesubstring = typesubstring[:currencytypelocationend].capitalize()

        # Assign the generated strings to a dictionary, which will in turn be assigned to a dictionary of fixed codes.
        details = {"code": codesubstring, "name": namesubstring, "symbol": symbolsubstring, "type": typesubstring}

        # Assign the Code & name to a dictionary
        codessplitup[i+1] = details

    # Repeating Menu
    while (True):
        print(f"Welcome to the Currency Calculator!\nFor a List of Available Currencies & Their ISO Codes, type \"HELP\"\nTo exit this calculator, type \"x\"")
        # Gather Inputs
        currin = None
        while currin == None:
            currin,insym = userentered(1)
        if currin == "x":
            break
        else:
            currin = str(currin)
        currout,outsym = userentered(2)
        originamount = float(userentered(3))
    
        response = requests.get(f"https://api.frankfurter.dev/v2/rate/{currin}/{currout}")
        rawresponse = response.text

        # Extract the Rate from the returned string
        rateis = rawresponse.find("rate") +6
        rateend = rateis + rawresponse[rateis:].find("}")
        correctrate = float(rawresponse[rateis:(rateend)])

        # CONVERT & PRINT
        targetamount = float(originamount * correctrate)
        print(f"{insym} {originamount:.2f} ({currin.upper()}) = {outsym} {targetamount:.2f} ({currout.upper()})")

        #Prevent from automatically rolling over to the next cycle of the menu.
        input("Press any button to continue...")

    # Exit Function, return to main menu
    return(0)

def Paint():
    """Function # 6: The Paint (Area) Calculator
    Author: Munashe
    """

def Discount():
    """Function # 7: The Discount Calculator
    Author: Munashe
    """

def ElectricityCost():
    """Function # 8: The Electricity Cost Calculator
    Author: Tadiwanashe Dondo
    """

def Log(fxnnum, fxnname, calldetails):
    """Function # 9: The Data Log Function
    Author: Jacob Feser
    """
    

main()
