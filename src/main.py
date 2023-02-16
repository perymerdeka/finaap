
from pprint import pprint

from modules.floatrates.spider import FloatratesSpider

if __name__ == '__main__':
    floatrates: FloatratesSpider = FloatratesSpider(url="http://www.floatrates.com/daily/usd.json")
    response = floatrates.parse()
    print(response)
    # pprint(response)