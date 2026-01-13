# Advanced Level

import math

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    
    Formula: SI = P × R × T / 100
    
    Args:
        principal (float): Principal amount
        rate (float): Annual interest rate (percentage)
        time (float): Time period in years
    
    Returns:
        dict: Dictionary with interest and total amount
    """
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    
    return {
        "interest": interest,
        "total_amount": total_amount,
        "principal": principal,
        "rate": rate,
        "time": time
    }


def calculate_compound_interest(principal, rate, time, frequency=1):
    """
    Calculate compound interest.
    
    Formula: A = P(1 + r/n)^(nt)
    CI = A - P
    
    Args:
        principal (float): Principal amount
        rate (float): Annual interest rate (percentage)
        time (float): Time period in years
        frequency (int): Compounding frequency per year
            1 = Annually, 2 = Semi-annually, 4 = Quarterly, 12 = Monthly, 365 = Daily
    
    Returns:
        dict: Dictionary with interest and total amount
    """
    # Convert percentage to decimal
    r = rate / 100
    
    # Calculate compound amount
    amount = principal * math.pow((1 + r / frequency), frequency * time)
    
    # Calculate interest
    interest = amount - principal
    
    return {
        "interest": interest,
        "total_amount": amount,
        "principal": principal,
        "rate": rate,
        "time": time,
        "frequency": frequency
    }


def get_frequency_name(frequency):
    """Get readable name for compounding frequency."""
    frequencies = {
        1: "Annually",
        2: "Semi-annually",
        4: "Quarterly",
        12: "Monthly",
        52: "Weekly",
        365: "Daily"
    }
    return frequencies.get(frequency, f"{frequency} times per year")


def display_simple_interest_result(result):
    """Display simple interest calculation results."""
    print("\n" + "=" * 80)
    print("SIMPLE INTEREST CALCULATION")
    print("=" * 80)
    
    print(f"\n📊 Input Values:")
    print(f"   Principal (P):        ${result['principal']:,.2f}")
    print(f"   Interest Rate (R):    {result['rate']:.2f}% per annum")
    print(f"   Time Period (T):      {result['time']:.2f} years")
    
    print(f"\n💰 Calculation:")
    print(f"   Formula:              SI = P × R × T / 100")
    print(f"   SI = {result['principal']:,.2f} × {result['rate']} × {result['time']} / 100")
    print(f"   SI = ${result['interest']:,.2f}")
    
    print(f"\n📈 Results:")
    print(f"   Simple Interest:      ${result['interest']:,.2f}")
    print(f"   Principal Amount:     ${result['principal']:,.2f}")
    print(f"   Total Amount:         ${result['total_amount']:,.2f}")
    
    print(f"\n🎯 Summary:")
    print(f"   You will earn ${result['interest']:,.2f} in interest")
    print(f"   Your investment will grow to ${result['total_amount']:,.2f}")
    
    print("=" * 80)


def display_compound_interest_result(result):
    """Display compound interest calculation results."""
    freq_name = get_frequency_name(result['frequency'])
    
    print("\n" + "=" * 80)
    print("COMPOUND INTEREST CALCULATION")
    print("=" * 80)
    
    print(f"\n📊 Input Values:")
    print(f"   Principal (P):        ${result['principal']:,.2f}")
    print(f"   Interest Rate (R):    {result['rate']:.2f}% per annum")
    print(f"   Time Period (T):      {result['time']:.2f} years")
    print(f"   Compounding:          {freq_name}")
    
    print(f"\n💰 Calculation:")
    r_decimal = result['rate'] / 100
    print(f"   Formula:              A = P(1 + r/n)^(nt)")
    print(f"   A = {result['principal']:,.2f} × (1 + {r_decimal}/{result['frequency']})^({result['frequency']} × {result['time']})")
    print(f"   A = ${result['total_amount']:,.2f}")
    
    print(f"\n📈 Results:")
    print(f"   Compound Interest:    ${result['interest']:,.2f}")
    print(f"   Principal Amount:     ${result['principal']:,.2f}")
    print(f"   Total Amount:         ${result['total_amount']:,.2f}")
    
    print(f"\n🎯 Summary:")
    print(f"   You will earn ${result['interest']:,.2f} in interest")
    print(f"   Your investment will grow to ${result['total_amount']:,.2f}")
    
    print("=" * 80)


def compare_interests(principal, rate, time):
    """Compare simple and compound interest for different frequencies."""
    print("\n" + "=" * 80)
    print("INTEREST COMPARISON")
    print("=" * 80)
    
    print(f"\n📊 Parameters:")
    print(f"   Principal:     ${principal:,.2f}")
    print(f"   Rate:          {rate:.2f}% per annum")
    print(f"   Time:          {time:.2f} years")
    
    # Calculate simple interest
    si_result = calculate_simple_interest(principal, rate, time)
    
    # Calculate compound interest for different frequencies
    frequencies = {
        "Annually": 1,
        "Semi-annually": 2,
        "Quarterly": 4,
        "Monthly": 12,
        "Weekly": 52,
        "Daily": 365
    }
    
    print(f"\n💰 Interest Earned Comparison:")
    print(f"{'Type':<20} {'Interest':<20} {'Total Amount':<20} {'Difference':<15}")
    print("-" * 80)
    
    # Simple Interest
    print(f"{'Simple Interest':<20} ${si_result['interest']:>15,.2f}   ${si_result['total_amount']:>15,.2f}   {'Baseline':<15}")
    
    # Compound Interest for each frequency
    for name, freq in frequencies.items():
        ci_result = calculate_compound_interest(principal, rate, time, freq)
        difference = ci_result['interest'] - si_result['interest']
        print(f"{name:<20} ${ci_result['interest']:>15,.2f}   ${ci_result['total_amount']:>15,.2f}   ${difference:>12,.2f}")
    
    # Best option
    daily_ci = calculate_compound_interest(principal, rate, time, 365)
    max_benefit = daily_ci['interest'] - si_result['interest']
    
    print("\n" + "=" * 80)
    print(f"🏆 Best Option: Compound Interest (Daily compounding)")
    print(f"   Additional benefit over Simple Interest: ${max_benefit:,.2f}")
    print("=" * 80)


def generate_year_by_year_breakdown(principal, rate, time, interest_type="compound", frequency=1):
    """Generate year-by-year breakdown of interest accumulation."""
    print("\n" + "=" * 80)
    print(f"YEAR-BY-YEAR BREAKDOWN ({interest_type.upper()} INTEREST)")
    print("=" * 80)
    
    print(f"\n{'Year':<8} {'Starting':<18} {'Interest':<18} {'Ending':<18}")
    print("-" * 80)
    
    current_principal = principal
    total_interest = 0
    
    for year in range(1, int(time) + 1):
        if interest_type == "simple":
            # Simple interest
            interest = (principal * rate * 1) / 100
            ending_balance = current_principal + interest
        else:
            # Compound interest
            r = rate / 100
            ending_balance = current_principal * math.pow((1 + r / frequency), frequency * 1)
            interest = ending_balance - current_principal
        
        total_interest += interest
        
        print(f"{year:<8} ${current_principal:>15,.2f}  ${interest:>15,.2f}  ${ending_balance:>15,.2f}")
        current_principal = ending_balance
    
    # Handle remaining fraction of year if time is not whole number
    if time % 1 != 0:
        remaining_time = time % 1
        year_label = f"{int(time) + 1}"
        
        if interest_type == "simple":
            interest = (principal * rate * remaining_time) / 100
            ending_balance = current_principal + interest
        else:
            r = rate / 100
            ending_balance = current_principal * math.pow((1 + r / frequency), frequency * remaining_time)
            interest = ending_balance - current_principal
        
        total_interest += interest
        print(f"{year_label:<8} ${current_principal:>15,.2f}  ${interest:>15,.2f}  ${ending_balance:>15,.2f}")
    
    print("-" * 80)
    print(f"{'TOTAL':<8} ${principal:>15,.2f}  ${total_interest:>15,.2f}  ${current_principal:>15,.2f}")
    print("=" * 80)


def get_valid_number(prompt, min_value=0, allow_zero=False):
    """Get valid numeric input from user."""
    while True:
        try:
            value = float(input(prompt))
            if not allow_zero and value <= min_value:
                print(f"⚠️  Value must be greater than {min_value}. Try again.")
                continue
            if allow_zero and value < min_value:
                print(f"⚠️  Value must be at least {min_value}. Try again.")
                continue
            return value
        except ValueError:
            print("⚠️  Invalid input. Please enter a valid number.")


def main():
    """Main program execution."""
    print("=" * 80)
    print("           SIMPLE & COMPOUND INTEREST CALCULATOR")
    print("=" * 80)
    print("\nCalculate interest earnings on your investments!")
    print("\nFormulas:")
    print("  Simple Interest:   SI = P × R × T / 100")
    print("  Compound Interest: A = P(1 + r/n)^(nt)")
    
    while True:
        print("\n" + "-" * 80)
        print("Options:")
        print("  1. Calculate Simple Interest")
        print("  2. Calculate Compound Interest")
        print("  3. Compare Simple vs Compound Interest")
        print("  4. Year-by-Year Breakdown")
        print("  5. View Formulas & Guide")
        print("  q. Quit")
        print("-" * 80)
        
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == 'q':
            print("\n💰 Happy investing! Goodbye!")
            break
        
        try:
            if choice == '1':
                # Simple Interest
                print("\n" + "=" * 80)
                print("SIMPLE INTEREST CALCULATOR")
                print("=" * 80)
                
                principal = get_valid_number("\nEnter principal amount ($): ")
                rate = get_valid_number("Enter annual interest rate (%): ")
                time = get_valid_number("Enter time period (years): ")
                
                result = calculate_simple_interest(principal, rate, time)
                display_simple_interest_result(result)
            
            elif choice == '2':
                # Compound Interest
                print("\n" + "=" * 80)
                print("COMPOUND INTEREST CALCULATOR")
                print("=" * 80)
                
                principal = get_valid_number("\nEnter principal amount ($): ")
                rate = get_valid_number("Enter annual interest rate (%): ")
                time = get_valid_number("Enter time period (years): ")
                
                print("\nCompounding frequency:")
                print("  1. Annually")
                print("  2. Semi-annually")
                print("  3. Quarterly")
                print("  4. Monthly")
                print("  5. Weekly")
                print("  6. Daily")
                
                freq_choice = input("Select frequency (1-6): ").strip()
                frequency_map = {"1": 1, "2": 2, "3": 4, "4": 12, "5": 52, "6": 365}
                frequency = frequency_map.get(freq_choice, 1)
                
                result = calculate_compound_interest(principal, rate, time, frequency)
                display_compound_interest_result(result)
            
            elif choice == '3':
                # Comparison
                print("\n" + "=" * 80)
                print("INTEREST COMPARISON TOOL")
                print("=" * 80)
                
                principal = get_valid_number("\nEnter principal amount ($): ")
                rate = get_valid_number("Enter annual interest rate (%): ")
                time = get_valid_number("Enter time period (years): ")
                
                compare_interests(principal, rate, time)
            
            elif choice == '4':
                # Year-by-year breakdown
                print("\n" + "=" * 80)
                print("YEAR-BY-YEAR BREAKDOWN")
                print("=" * 80)
                
                principal = get_valid_number("\nEnter principal amount ($): ")
                rate = get_valid_number("Enter annual interest rate (%): ")
                time = get_valid_number("Enter time period (years): ")
                
                print("\nInterest type:")
                print("  1. Simple Interest")
                print("  2. Compound Interest")
                
                type_choice = input("Select type (1 or 2): ").strip()
                
                if type_choice == "1":
                    generate_year_by_year_breakdown(principal, rate, time, "simple")
                else:
                    print("\nCompounding frequency:")
                    print("  1. Annually")
                    print("  2. Quarterly")
                    print("  3. Monthly")
                    
                    freq_choice = input("Select frequency (1-3): ").strip()
                    frequency_map = {"1": 1, "2": 4, "3": 12}
                    frequency = frequency_map.get(freq_choice, 1)
                    
                    generate_year_by_year_breakdown(principal, rate, time, "compound", frequency)
            
            elif choice == '5':
                # Formulas and guide
                print("\n" + "=" * 80)
                print("FORMULAS & GUIDE")
                print("=" * 80)
                
                print("\n📚 SIMPLE INTEREST")
                print("-" * 80)
                print("Formula: SI = (P × R × T) / 100")
                print("\nWhere:")
                print("  P = Principal amount (initial investment)")
                print("  R = Annual interest rate (percentage)")
                print("  T = Time period (in years)")
                print("  SI = Simple Interest")
                print("\nTotal Amount = Principal + Simple Interest")
                
                print("\n📚 COMPOUND INTEREST")
                print("-" * 80)
                print("Formula: A = P(1 + r/n)^(nt)")
                print("         CI = A - P")
                print("\nWhere:")
                print("  P = Principal amount")
                print("  r = Annual interest rate (as decimal)")
                print("  n = Number of times interest compounds per year")
                print("  t = Time period (in years)")
                print("  A = Final amount")
                print("  CI = Compound Interest")
                
                print("\n📊 COMPOUNDING FREQUENCIES")
                print("-" * 80)
                print("  Annually:      n = 1   (once per year)")
                print("  Semi-annually: n = 2   (twice per year)")
                print("  Quarterly:     n = 4   (four times per year)")
                print("  Monthly:       n = 12  (twelve times per year)")
                print("  Weekly:        n = 52  (52 times per year)")
                print("  Daily:         n = 365 (365 times per year)")
                
                print("\n💡 KEY DIFFERENCES")
                print("-" * 80)
                print("Simple Interest:")
                print("  • Interest calculated only on principal")
                print("  • Linear growth")
                print("  • Lower returns")
                print("  • Easier to calculate")
                
                print("\nCompound Interest:")
                print("  • Interest calculated on principal + accumulated interest")
                print("  • Exponential growth")
                print("  • Higher returns")
                print("  • 'Interest on interest' effect")
                
                print("\n🎯 TIPS")
                print("-" * 80)
                print("  1. More frequent compounding = higher returns")
                print("  2. Compound interest grows exponentially over time")
                print("  3. Small rate differences have big long-term impacts")
                print("  4. Time is your best friend in compound interest")
                
                print("=" * 80)
            
            else:
                print("\n❌ Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Operation cancelled.")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()