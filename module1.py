def calculate_compound_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate : "))
    time = float(input("Enter the time period : "))

    compound_interest = principal * ((1 + rate) ** time - 1)
    print( compound_interest)
def main():
    calculate_compound_interest()
    

if __name__ == "__main__":
    main()
   
