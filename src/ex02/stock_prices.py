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
    
    argument = sys.argv[1].capitalize()
    x = COMPANIES.get(argument)

    if x is None:
        print("Unknown company")

    else:
        print(STOCKS[x]) 

if __name__ == '__main__':
    dictionary()           