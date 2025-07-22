# Stock Tracker 📈

A simple command-line stock portfolio tracker that helps you calculate and manage your stock investments using predefined stock prices.

## 🎯 Features

- **Portfolio Management**: Add stocks to your portfolio and track quantities
- **Real-time Calculations**: Calculate total investment value based on current holdings
- **Multiple Export Options**: Save portfolio data as TXT or CSV files
- **User-Friendly Interface**: Simple menu-driven navigation
- **8 Popular Stocks**: Pre-loaded with major tech stocks (AAPL, TSLA, GOOGL, etc.)

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher

### Running the Application
1. Clone this repository
2. Run the stock tracker:
   ```bash
   python main.py
   ```

## 📊 Available Stocks

The application includes these predefined stocks with current prices:

| Stock Symbol | Company | Price |
|--------------|---------|--------|
| AAPL | Apple Inc. | $180.50 |
| TSLA | Tesla Inc. | $250.75 |
| GOOGL | Alphabet Inc. | $2,800.25 |
| MSFT | Microsoft Corp. | $350.00 |
| AMZN | Amazon.com Inc. | $3,200.75 |
| META | Meta Platforms Inc. | $320.50 |
| NVDA | NVIDIA Corp. | $450.25 |
| NFLX | Netflix Inc. | $400.00 |

## 🎮 How to Use

### Main Menu Options:

1. **Add Stock to Portfolio**
   - Enter stock symbol (case-insensitive)
   - Specify quantity of shares
   - Stocks are automatically added or quantities updated

2. **View Portfolio Summary**
   - See all your holdings in a formatted table
   - View individual stock values and total portfolio worth
   - Real-time calculation of investment value

3. **Save Portfolio to File**
   - Export as TXT file (detailed summary format)
   - Export as CSV file (spreadsheet-compatible format)
   - Files include timestamp for easy tracking

4. **Exit**
   - Safely close the application

### Sample Workflow:
```
🚀 Welcome to Simple Stock Tracker!
Available stocks and their current prices:
----------------------------------------
AAPL: $180.50
TSLA: $250.75
...

Enter your choice (1-4): 1
Enter stock symbol (e.g., AAPL): AAPL
Enter quantity of AAPL shares: 10
Added 10 shares of AAPL to your portfolio
```

## 📁 File Exports

### TXT Format
- Detailed summary with timestamp
- Individual stock breakdown
- Total portfolio value

### CSV Format
- Spreadsheet-compatible format
- Easy to import into Excel or Google Sheets
- Includes headers and totals

## 🛠️ Code Structure

- `stock_tracker()`: Main application logic and menu system
- `save_to_txt()`: Export portfolio data to text file
- `save_to_csv()`: Export portfolio data to CSV file
- **Input validation**: Ensures valid stock symbols and quantities
- **Error handling**: Graceful handling of file operations and user input

## 🔧 Customization

Want to add more stocks or update prices? Modify the `stock_prices` dictionary:

```python
stock_prices = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "YOUR_STOCK": 123.45,
    # Add more stocks here
}
```

## 📋 Key Programming Concepts

This project demonstrates:
- **Dictionaries**: Stock prices and portfolio storage
- **Input/Output**: User interaction and data validation
- **File Handling**: CSV and TXT file operations
- **Basic Arithmetic**: Investment calculations
- **Control Flow**: Menu-driven program structure
- **Error Handling**: Input validation and file operations

## 🎯 Learning Objectives

Perfect for learning:
- Python dictionaries and data structures
- File I/O operations
- User input validation
- Menu-driven program design
- Basic financial calculations
