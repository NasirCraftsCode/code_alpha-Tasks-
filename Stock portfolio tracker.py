
import csv
from datetime import datetime

def stock_tracker():
    # Hardcoded stock prices dictionary
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "GOOGL": 2800.25,
        "MSFT": 350.00,
        "AMZN": 3200.75,
        "META": 320.50,
        "NVDA": 450.25,
        "NFLX": 400.00
    }
    
    print(" Welcome to Simple Stock Tracker!")
    print("Available stocks and their current prices:")
    print("-" * 40)
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f}")
    print("-" * 40)
    
    portfolio = {}
    total_investment = 0.0
    
    while True:
        print("\nOptions:")
        print("1. Add stock to portfolio")
        print("2. View portfolio summary")
        print("3. Save portfolio to file")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            stock_name = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
            
            if stock_name not in stock_prices:
                print(f"Sorry, {stock_name} is not available. Available stocks: {', '.join(stock_prices.keys())}")
                continue
            
            try:
                quantity = int(input(f"Enter quantity of {stock_name} shares: "))
                if quantity <= 0:
                    print("Quantity must be a positive number.")
                    continue
            except ValueError:
                print("Please enter a valid number for quantity.")
                continue
            
            # Add to portfolio or update existing holding
            if stock_name in portfolio:
                portfolio[stock_name] += quantity
                print(f"Added {quantity} more shares of {stock_name}. Total: {portfolio[stock_name]} shares")
            else:
                portfolio[stock_name] = quantity
                print(f"Added {quantity} shares of {stock_name} to your portfolio")
        
        elif choice == "2":
            if not portfolio:
                print("Your portfolio is empty. Add some stocks first!")
                continue
            
            print("\n📊 Portfolio Summary:")
            print("-" * 60)
            print(f"{'Stock':<8} {'Shares':<8} {'Price':<10} {'Total Value':<12}")
            print("-" * 60)
            
            total_investment = 0.0
            for stock, shares in portfolio.items():
                stock_price = stock_prices[stock]
                stock_value = shares * stock_price
                total_investment += stock_value
                print(f"{stock:<8} {shares:<8} ${stock_price:<9.2f} ${stock_value:<11.2f}")
            
            print("-" * 60)
            print(f"{'TOTAL PORTFOLIO VALUE:':<38} ${total_investment:.2f}")
            print("-" * 60)
        
        elif choice == "3":
            if not portfolio:
                print("Your portfolio is empty. Nothing to save!")
                continue
            
            save_format = input("Save as (1) TXT or (2) CSV? Enter 1 or 2: ").strip()
            
            if save_format == "1":
                save_to_txt(portfolio, stock_prices)
            elif save_format == "2":
                save_to_csv(portfolio, stock_prices)
            else:
                print("Invalid choice. Please enter 1 or 2.")
        
        elif choice == "4":
            print("Thank you for using Stock Tracker! 📈")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def save_to_txt(portfolio, stock_prices):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    try:
        with open(filename, 'w') as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write("=" * 50 + "\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            total_investment = 0.0
            for stock, shares in portfolio.items():
                stock_price = stock_prices[stock]
                stock_value = shares * stock_price
                total_investment += stock_value
                
                file.write(f"Stock: {stock}\n")
                file.write(f"Shares: {shares}\n")
                file.write(f"Price per share: ${stock_price:.2f}\n")
                file.write(f"Total value: ${stock_value:.2f}\n")
                file.write("-" * 30 + "\n")
            
            file.write(f"\nTOTAL PORTFOLIO VALUE: ${total_investment:.2f}\n")
        
        print(f"Portfolio saved successfully to {filename}")
    
    except Exception as e:
        print(f"Error saving file: {e}")

def save_to_csv(portfolio, stock_prices):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Write header
            writer.writerow(['Stock Symbol', 'Shares', 'Price per Share', 'Total Value'])
            
            total_investment = 0.0
            for stock, shares in portfolio.items():
                stock_price = stock_prices[stock]
                stock_value = shares * stock_price
                total_investment += stock_value
                writer.writerow([stock, shares, f"${stock_price:.2f}", f"${stock_value:.2f}"])
            
            # Write total row
            writer.writerow(['', '', 'TOTAL:', f"${total_investment:.2f}"])
        
        print(f"Portfolio saved successfully to {filename}")
    
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    stock_tracker()
