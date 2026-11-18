# COMP 1110 - Everyday Calculator

#### Video demo: <SpectraVideo URL>
#### Team: Tadiwanashe Dondo, Munashe Isaac Chapoka, Jacob Feser — COMP 1110, Fall 2026
#### Repository: <https://github.com/JabicZF/COMP1110-Python-Project>

## Description
### The Problem
Many Everyday Problems are difficult to solve without a calculator, and many people don’t actually know the math required to do some conversions, or calculations, and rather choose to Google an answer, which takes more time, and more energy than a dedicated calculator would.

### The Solution
A dedicated Calculator, with many options for different Everyday Uses, will allow users to solve their problems and questions simply and easily. An Easy-to-understand UI will also lower the barrier-to-entry

### I/Os
The Inputs for this program will all be user-generated, as users will type their selections and queries. The output will be two-fold. First, the user will see a printed response, and then, when they choose to quit the program, a text File (Log File) will be generated, with a list of all inputs, outputs, and calculations performed throughout the session. Every generated Log File will be unique, with a Time Stamp of the session’s start.


## The files
### project.py
project.py contains 9 functions:
1. Menu (Main) - (Jacob)
This Function will let you choose which calculator function you want to use. It will accept inputs as numbers, single letters, or whole words to get to the right function. From this main() function, all other functions will be able to be called
2. Loan Interest Calculator - (Tadiwanashe Dondo)
This Function will take in a Loan Period, the Interest Rate, and the Base Payment, and will output how long it will take you to pay it back. Additionally, the math can be used in reverse to calculate how much interest you will gain on an investment over time.
3. Unit Converter - (Tadiwanashe Dondo)
This Function will take in a value and a unit type (e.g. 4 Kilometers), and let the user choose which unit they want to convert to (e.g. Feet), and then perform the conversion.
4. Useful Car Details Calculator-(Muanshe)
This Function will offer several options: First, given a distance and fuel used, it will calculate the Fuel Efficiency. Alternatively, given a fuel quantity and Fuel Efficiency, it will return to the user a distance that they can travel. Finally, given a distance and Fuel efficiency, it will calculate the Fuel required for that trip.
5. Currency Converter - (Jacob)
Given an amount (in a source currency), and a destination currency, This function will convert the given amount into the Destination Currency. This function might have to be scaled back or eliminated, because it might be too difficult to source current currency conversion rates.
6. Paint  (Area) Calculator - (Munashe)
This Function will take in dimensions (e.g. 4’ x 8’), and the number of coats of paint that will be applied, and return the area of paint required to cover that area. It can also take the dimensions of a room (e.g. 4’ x 8’ x 8’), as well as the area of things that won’t be painted (e.g. Window 2’ x 4’), and coats planned, and calculate the paint required for all 4 walls (assuming the user isn’t painting the cut-out sections).
7. Discount Calculator-(Munashe) 
This Function will take in a base price for an item, as well as a discount percent, and return the discounted price. Additionally, if you have more layers of discounts (i.e. the item has a discount of 25% off, and you have a coupon that gives you 30% off your final price), the Function will let you calculate the final price with layered discounts.
8. Electricity Cost - Tadiwanashe Dondo 
This Function will take in three different electricity rates, a two-tiered rate for low and high electricity usage, as well as a flat rate, and the point where the first rate switches to the second rate (in kWh). It will also take in a base (daily) rate for each rate style, and a usage period. Then, given a certain usage, it will calculate the price using the two-tiered rate, and the flat rate, and tell you which is a better deal.
9. Data Log - (Jacob)
This Function will record all inputs and outputs used in a session, and save them to a text file, so that the results can be more easily stored, used, and tested.

### test_project.py — what each test checks.
### requirements.txt — which libraries, and why you need them.
### data/ — what is in it and where it came from.

## Design decisions
Why a dictionary here, why a class there, what you tried first and abandoned.
This is the section I read most closely. Explain your reasoning, not just your
structure.

## How to run it
pip install -r requirements.txt
python3 project.py

## How to run the tests
pytest test_project.py

## Known limitations
What it does not handle yet. Saying so scores better than staying quiet about it.

## Individual contributions
Name — which functions they wrote.

## Sources
Any external code, tutorial, or documentation you drew on, and where it is used.
