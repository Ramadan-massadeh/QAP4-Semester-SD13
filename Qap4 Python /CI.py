# Description: Project 1 – Python – Functions, Lists, and Data Files The One Stop Insurance Company 
# Needs a program to enter and calculate new insurance policy information for its customers.
# Author: Ramadan Masadekh
# Date(s): Nov 23 , 2024
 
 
# Define required libraries.
import datetime
import FormatValues as FV
import sys
import time


 
 
# Define program constants.
# Create a file and set up all the constants/default values in the file.
# Here at the constants section, I will open the and read
# each of the values and assign them to variables.
CURENT_DATE = datetime.datetime.now()
f = open('Default.dat', 'r')
POLICY_NUMBER= int(f.readline())
BASIC_PREMIUM = int(f.readline()) # Base premium for the first automobile
ADDITIONAL_CAR_DISCOUNT = float(f.readline()) # 25% discount for additional cars
EXTRA_LIABILITY_COST = int(f.readline()) # Cost for extra liability coverage
GLASS_COVERAGE_COST = int(f.readline())  # Cost for glass coverage
LOANER_CAR_COST = int(f.readline())  # Cost for loaner car option
HST_RATE = float(f.readline())  # HST rate as 15%
PROCESSING_FEE = float(f.readline())  # Processing fee for monthly payments
f.close()



# Define program functions.


# functions to calculate Insurance premiums are calculated using a basic rate
def  Calculate_basic_premium(Numcars):
    if Numcars == 1:
     return BASIC_PREMIUM
    else:
        AdditionalCarsPremium = (Numcars - 1 ) * BASIC_PREMIUM *(1 - ADDITIONAL_CAR_DISCOUNT)


    return Numcars , AdditionalCarsPremium

# functions to calculate Extra cost

def Calculate_extra_cost(ExtraLab , GlassCoverage , LoanerCar):
    if ExtraLab == 'Y':
        return EXTRA_LIABILITY_COST
    elif ExtraLab == 'N':
        return 0.0
    elif GlassCoverage == 'Y':
        return GLASS_COVERAGE_COST
    elif GlassCoverage == 'N':
        return 0.0
    elif LoanerCar == 'Y':
        return LOANER_CAR_COST
    elif LoanerCar == 'N':
        return 0.0
    
    return Numcars *(EXTRA_LIABILITY_COST + GLASS_COVERAGE_COST + LOANER_CAR_COST)

# functions to calculate Total Cost and Hst

def Calculate_total_cost(BASIC_PREMIUM, Extra):
   
    Subtotal = BASIC_PREMIUM + Extra
    Hst = Subtotal * HST_RATE
    Total_cost = Subtotal + Hst
    return Total_cost, Hst

# functions to calculate Monthly payment

def Calculate_Monthly_Payment(TotalCost, AmmDownPayment):
   
    total_cost_with_fee = TotalCost + PROCESSING_FEE
 
    Remaining_balance = total_cost_with_fee - AmmDownPayment

    return Remaining_balance / 8



        

 


 # Validation Lists
valid_prov = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]





# Main program starts here
# User Validated Inputs
# First name
while True:
 
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ- abcdefghijklmonpqrstuvwxz'")
    while True:
        FirstName=input("Enter the First name : ").title()

        if FirstName =="":
            print()
            print("   Data Entry Error - The first name must be entered ...")
            print()
        elif  set(FirstName).issubset(allowed_char) == False:
            print()
            print("First Name contains invalid characters. Please re-enter.")
            print()
        else:
            break
# Last name
    while True:
        LastName=input("Enter the last name: ").title()

        if LastName=="":
            print()
            print("   Data Entry Error - The Last name must be entered ...")
            print()
        elif set(LastName).issubset(allowed_char)== False:
            print()
            print("Last Name contains invalid characters. Please re-enter.")
            print()
        else :
            break
# Street Adress        
    while True:
         StrAdress= input ("Enter the street address: ").title()
         if StrAdress == "":
            print()
            print("   Data Entry Error - The Street Adress must be entered ...")
            print()
         else :
                break
# City         
    while True:
         City= input ("Enter the City: ").title()
         if City == "":
            print()
            print("   Data Entry Error - The City  must be entered ...")
            print()
         else :
                break
         
# province
    while True:
        Prov = input ("Enter the province: ").upper()
        if Prov == "":
            print("   Data Entry Error - Province cannot be blank.")
        elif len(Prov) != 2:
            print("   Data Entry Error - Provice is a 2 character code only.")
        elif Prov not in valid_prov:
            print("   Data Entry Error - province is not valid.")
        else:
            break
    
# Postal Code
    allowed_char2 = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
    while True:
        PosCode = input("Enter the Postal Code (XXX000): ").upper()
    
        if PosCode == "":
            print()
            print("   Data Entry Error - Postal Code  must be entered ...")
            print()
        elif len(PosCode) != 6:
            print()
            print("   Data Entry Error - Postal Code  must be 6 characters only ...")
            print()
        elif set(PosCode).issubset(allowed_char2) == False:
            print()
            print("   Data Entry Error - Postal Code  must start with 3 letters ...")
            print()
        else:
            break

# Phone number    

    allowed_char = set("1234567890")
    while True:
        Phone = input("Enter the phone number (XXX-XXXX-XXX): ")
    
        if Phone == "":
            print()
            print("   Data Entry Error - Phone number must be entered ...")
            print()
        elif set(Phone).issubset(allowed_char) == False:
            print()
            print("   Data Entry Error - Phone number contains invalid characters ...")
            print()
        elif len(Phone) != 10:
            print()
            print("   Data Entry Error - Phone number must be 10 digits only ...")
            print()
        else:
            Phone = "(" + Phone[0:3] + ") " + Phone[3:6] + "-" + Phone[6:10]
            break

# Number of cars to insure
    while True:
        try:
            Numcars = int(input("Number of cars to insure:      "))
        except:
            print("Please enter a valid number")
        else:
            if Numcars < 1:
                print("Please enter a number greater than 1")
            else:
                break

# Extra liability
    while True:

        ExtraLab= input ("Add extra liability coverage up to $1,000,000 (Y/N): ").upper()

        if ExtraLab == 'Y' or ExtraLab == 'N':
            break
        else:
            print()
            print("   Data Entry Error - Extra liability must be entered ...")
            print()

# Glass Coverage
    while True:

        GlassCoverage= input("Add optional glass coverage (Y/N): ").upper()

        if GlassCoverage == 'Y' or GlassCoverage == 'N':
            break
        else:
            print()
            print("   Data Entry Error - Glass Coverage must be entered ...")
            print()

# loaner car
    while True:

        LoanerCar= input ("Add optional loaner car (Y/N): ").upper()

        if LoanerCar == 'Y' or LoanerCar == 'N':
            break
        else:
            print()
            print("   Data Entry Error - loaner car must be entered ...")
            print()

     
# pay in full or monthly (Full or Monthly or Down Pay 

    while True:

        Payments= input ("Would you like to pay (Full or Monthly or Down ) ").upper()
        AmmDownPayment=0

    

        if Payments == 'DOWN':
            AmmDownPayment= input ("Enter the amount of the down payment ")
            AmmDownPayment = float (AmmDownPayment)
            break
        else:
           break
    
    # Finally enter the Claim number, claim date, and the claim amount of all previous claims for the customer

    claims = []

    while True:
        ClaimNum = input("Enter Claim Number (or 'done' to finish): ").lower()
        if ClaimNum == 'done':
            break

        ClaimDate = input("Enter Claim Date (YYYY-MM-DD): ")
        ClaimDate = datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")

        ClaimAmmount = float(input("Enter the claim amount: "))

        claims.append({"number": ClaimNum, "Date": ClaimDate, "Ammount": ClaimAmmount})

   
   
# Perform required calculations.

    
    AddCars=Calculate_basic_premium(Numcars)
    BasicPremium= AddCars + BASIC_PREMIUM

    ExtraCost= Calculate_extra_cost(ExtraLab , GlassCoverage , LoanerCar)

    # Total Insurance Premium is the sum of the Basic Premium and Extra Costs
    TotalInnPremium = BasicPremium + ExtraCost
# HST Calculation , 15%(HST rate) of total insurance premium and Total Cost
    TotalCost ,Hst=Calculate_total_cost(BASIC_PREMIUM , ExtraCost)

# Monthy Payment
    if Payments == 'MONTHLY':
     total_cost_with_fee = TotalCost + PROCESSING_FEE
     MonthlyPayment = Calculate_Monthly_Payment(total_cost_with_fee, AmmDownPayment)
    else:
     MonthlyPayment = 0.0

# The invoice date is the current date

    InvoiceDate= CURENT_DATE.strftime("%Y-%m-%d")
   
    FtimePay=CURENT_DATE.replace(month=CURENT_DATE.month + 1, day=1)

    FtimePayD=FtimePay.strftime("%Y-%m-%d")






    




# Display results

# Display variables
    full_name = (f"{FirstName} {LastName}")
    dsp_first_car_cost = "${:,.2f}".format(BASIC_PREMIUM)
    dsp_add_car_cost = "${:,.2f}".format(AddCars)
    dsp_basic_prem = "${:,.2f}".format(BasicPremium)
    dsp_ex_insurance_cost = "${:,.2f}".format(TotalInnPremium)
    dsp_glass_cov_cost = "${:,.2f}".format(GLASS_COVERAGE_COST)
    dsp_loaner_car_cost = "${:,.2f}".format(LOANER_CAR_COST)
    dsp_hst = "${:,.2f}".format(Hst)
    dsp_total_cost = "${:,.2f}".format(TotalCost)
    dsp_extra_costs = "${:,.2f}".format(ExtraCost)
    dsp_MON_PRO_FEE = "${:,.2f}".format(PROCESSING_FEE)
    dsp_monthly_payment = "${:,.2f}".format(MonthlyPayment)



    # Receipt generation
    print()
    print()
    print(f"         1         2         3         4         5         6         7")
    print(f"123456789012345678901234567890123456789012345678901234567890123456789012345678")
    print()
    
    
    print(f'One Stop Insurance Company                      Invoice Date:     {InvoiceDate :<14s}')
    print(f'Insurance Claim Receipt                         Policy Number:        {POLICY_NUMBER}')
    print()

    print(f"Client Name: {full_name}                         ")
    print(f"Phone Number: {Phone}                            ")
    print(f'Address:             {StrAdress}, {City}, {Prov} ')
    print(f"                           {PosCode}")        
    print(f"                                          ---------------------------------")         
    print(f"Number of Cars Insured: {Numcars:>2d}                First Car Cost:           {dsp_first_car_cost:>7s} ")
    print(f"Payment Frequency:       {Payments:<7s}          Additional Car Cost:    {dsp_add_car_cost:>9s}   ")
    print(f"                                          Basic Premium Total:   {dsp_basic_prem:>10s}")
    print(f"                                          ---------------------------------")
    print(f"                                          Extra Liability Cost:  {dsp_ex_insurance_cost:>10s}")
    print(f"                                          Glass Coverage Cost:   {dsp_glass_cov_cost:>10s}")
    print(f"                                          Loaner Car Cost:       {dsp_loaner_car_cost:>10s}")
    print(f"                                          Total Extra Costs:     {dsp_extra_costs:>10s}")
    print(f"                                          ---------------------------------")
    print(f"                                          HST:                   {dsp_hst:>10s}")
    if Payments == "MONTHLY":
        print(f"                                          Processing Fee:           {dsp_MON_PRO_FEE:>6s}")
    print(f"                                          Total Cost:            {dsp_total_cost:>10s}")
    print()

    if Payments == "MONTHLY":
        print(f"                                          Monthly Payment:       {dsp_monthly_payment:>10s}")
    else:
        print(f"                                          Yearly Payment:        {dsp_total_cost:>10s}")

    print()
    print(f"Next Payment date: {FtimePayD}")
    
    print("---------------------------------------------------------------------------")
    print()


    print()
    # Print all entered claims in the required format
    print("\nClaim #   Claim Date   Amount")
    print("-----------------------------------")
    for claim in claims:
        print(f"{claim['number'].rjust(6)}   {claim['Date'].strftime('%Y-%m-%d')}   ${claim['Ammount']:,.2f}")





    
    

# Blinking message for the user.

    print()

    Message = "Saving Movie Data ..."
    for _ in range(5):  # Change to control no. of 'blinks'
        print(Message, end='\r')
    time.sleep(.3)  # To create the blinking effect
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
    time.sleep(.3)

    print()

    # Write the values to a data file for storage.
    f = open("Def.dat", "a") # Mode can be 'a' for append, 'w' for overwrite, 'r' to read.


    f.write(f"{str(POLICY_NUMBER)}\n")
    f.write(f"{str(BASIC_PREMIUM)}\n")
    f.write(f"{str(ADDITIONAL_CAR_DISCOUNT)}\n")
    f.write(f"{str(EXTRA_LIABILITY_COST)}\n")
    f.write(f"{str(GLASS_COVERAGE_COST)}\n")
    f.write(f"{str(LOANER_CAR_COST)}\n")
    f.write(f"{str(HST_RATE)}\n")
    f.write(f"{str(PROCESSING_FEE)}\n")
    f.write(f"\n")




    f.close()




    # Update any values for the next claim

    POLICY_NUMBER +=1


    Countinue = input("Do you want process another claim (Y / N):  ").upper()
    if Countinue == 'N':
     break

   
# Any housekeeping duties at the end of the program.

# Now we need to save the updated values back to the constants/defualts file.
