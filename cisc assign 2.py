# week 3: loops and lists
# i used some of my original code along with some of the sample code provided in the class announcements

def main():

    # ask for input values and checking to see if theyre valid inputs

    # planned payment term (between 1 and 30)
    term = int(input("enter the planned payment term in years: "))
    while term < 1 or term > 30 :
        term = int(input("are you sure? please try again: "))

    # annual interest percent (between 1 and 10)
    annualInterest = float(input("enter your annual interest rate as a percentage: "))
    while annualInterest < 1 or annualInterest > 10 :
        annualInterest = float(input("are you sure? please try again: "))

    # principal dollar amount (between 1,000 and 500,000)
    principal = float(input("enter principal dollar amount: "))
    while principal < 1000 or principal > 500000 :
        principal = float(input("are you sure? please try again: "))

    # anniversary payment (either 'y' or 'n')
    doAnniversaryPayment = str(input("would you like to make anniversary payments? y or no: "))
    if (doAnniversaryPayment != "y" and doAnniversaryPayment != "Y" and doAnniversaryPayment != "n" and doAnniversaryPayment != "N"):
        doAnniversaryPayment = str(input("are you sure? please try again: "))

    termInMonths = 12 * term
    monthlyInterestRate = annualInterest / 1200

    totalInterestPayments = 0
    totalMonthlyPayments = 0
    totalAnniversaryPayments = 0
    monthlyPayment = principal * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** - termInMonths)

    month = 1
    while principal > 0:
        # monthly calculations
        
        interestPayment = monthlyInterestRate * principal

        principal = principal - (monthlyPayment - interestPayment)

        totalInterestPayments = totalInterestPayments + interestPayment
        totalMonthlyPayments = totalMonthlyPayments + monthlyPayment

        print("Monthly payment is ${0:.2f}".format(monthlyPayment))
        print(month)

        if (doAnniversaryPayment == 'y' or doAnniversaryPayment == 'Y') and month % 12 == 0:
            # calculate anniversary payment
            anniversaryPayment = min(5000,0.05*principal)
            principal = principal - anniversaryPayment
            totalAnniversaryPayments = totalAnniversaryPayments + anniversaryPayment
            print("Anniversary payment made: ${0:.2f}, principal: ${1:.2f}".format(anniversaryPayment, principal))



        print("Remaining principle is ${0:.2f}".format(principal))
        month = month + 1
    
    print("Total interest payments: ${0:.2f}".format(totalInterestPayments))
    print("Total monthly payments: ${0:.2f}".format(totalMonthlyPayments))
    if doAnniversaryPayment == 'y' or doAnniversaryPayment == 'Y':
        print("Total of anniversary payments: ${0:.2f}".format(totalAnniversaryPayments))
        print("Paid off mortgage %s months early" % (totalAnniversaryPayments/monthlyPayment))



main()