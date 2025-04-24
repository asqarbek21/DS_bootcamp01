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
    
    argument = sys.argv[1]
    entries = argument.split(',')

    if any(e.strip() == '' for e in entries):
        return
    
    for item in entries:
        item = item.strip()
        normalized = item.capitalize()

        if normalized in COMPANIES:
            ticker = COMPANIES[normalized]
            price = STOCKS[ticker]
            print(f"{normalized} stock price is {price}")

        elif item.upper() in STOCKS:
            ticker = item.upper()
            company = next((name for name, code in COMPANIES.items() if code == ticker), None)
            if company:
                print(f"{ticker} is a ticker symbol for {company}")
            else:
                print(f"{item} is an unknown company or an unknown ticker symbol")

        else:
            print(f"{item} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    dictionary()            