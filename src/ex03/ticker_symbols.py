import sys

def dictionary():
    
    COMPANIES = {
  'Apple': 'AAPL',
  'Microsoft': 'MSFT',
  'Netflix': 'NFLX',
  'Tesla': 'TSLA',
  'Nokia': 'NOK'
  }

    STOCKS = {
  'AAPL': 287.73,
  'MSFT': 173.79,
  'NFLX': 416.90,
  'TSLA': 724.88,
  'NOK': 3.37
  }
    
    if len(sys.argv) != 2:
        return
    
    argument = sys.argv[1].upper()
    
    if argument not in STOCKS:
        print("Unknown ticker")
        return
    
    company_name = None
    for name, symbol in COMPANIES.items():
        if symbol == argument:
            company_name = name
            break

    print(f"{company_name} {STOCKS[argument]}")    

if __name__ == '__main__':
    dictionary()           