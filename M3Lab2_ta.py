# Calculating a mortgage loan with monthly compound interest
# By C. Calongne, 01/14/2019
# Pseudocode & Python with Strings, M3Lab2_student.py
# Write the statements requested in Steps 1-7 below
# 
# See the examples in the provided code
# Use structured programming and indent your code.
# Programmer Name: *****Taryn Aranda****

print()
print("Welcome to the Mortgage Loan Calculator.")
print("****************************************")

# ****Instructions****
# Complete Steps 1-7 in the comments below. The remaining comments explain the logic.
# Customers can check a variety of loans and interest rates. When finished, type quit

# Step 1: add an input statement to enter name or type quit to exit
def hello():
        name=str(input("enter the name : "))
        print("hello " + str(name))
        return
        hello()
# Step 2: add a while loop to keep asking for a name until the user types quit
        if_name==('name')
        print('Thank you for entering your name.')
        loop=True
        else(loop+('name'))

    # Step 3: declare two variables for loan and interest, like months below, 
    # convert them to float, and ask the user to input their values to the screen. 
    import math
    Label(window, text = "Annual Interest Rate").grid(row = 1,column = 1, sticky = W)
    Label(window, text = "Number of Years").grid(row = 2,column = 1, sticky = W)
    Label(window, text = "Loan Amount").grid(row = 3,column = 1, sticky = W)
    Label(window, text = "Monthly Payment").grid(row = 4,column = 1, sticky = W)
    Label(window, text = "Total Payment").grid(row = 5, column = 1, sticky = W)

  ComputePayment = Button(window, text = "Compute Payment",command = self.computePayment).grid( row = 6, column = 2, sticky = E)

months = float(input("How many months will it take to repay your loan? "))

    print("***************************************************************")
    print (name, "you requested an estimate on a loan for {0:.2f}" .format(loan))

    # Step 4: add a print statement to display the interest and # of months

    def computePayment(self):
                 
        monthlyPayment = self.getMonthlyPayment(
        float(self.loanAmountVar.get()),
        float(self.annualInterestRateVar.get()) / 1200,
        int(self.numberOfYearsVar.get()))
 
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
                                * int(self.numberOfYearsVar.get())
 
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
 
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1
        - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;
        root = Tk()
    print("*******************************************************************************")
    print("Here are the rates for simple interest, compound interest, and monthly interest", "\n") 
    interest_rate = float((interest/12)+1)
    compound_interest = float(1-((interest/12)+1) ** -months)


    # Step 5: print the interest_rate and compound_interest to the display screen
        print('interest_rate+compound_interest')

    monthly_interest = float((interest/12)/ compound_interest)
    print(monthly_interest, "\n")
    payments = float(loan * monthly_interest)


    # Step 6: write a print statement that displays the monthly payments to two decimal points
    # Tip: use the 0:.2f format from an earlier example, only for the payments

    

    print("*******************************************")
    # Step 7: add an input statement to enter name or type quit to exit


print(Quit)
print("Thank you for using the Mortgage Loan Calculator")
