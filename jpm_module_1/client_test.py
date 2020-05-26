import unittest
from client import getDataPoint
from client import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """
  # tests for getRatio method
  def test_getRatio_computeRatio(self):
    # fake data
    prices = [ 
      {'A': 2.00, 'B': 5.00}, {'A': 7.00, 'B': 3.00}, {'A': 9.34, 'B': 7.34}, {'A': 25.76, 'B': 98.75}, {'A': 105.24, 'B': 53.64}
    ]
    # assertion to test method
    for price in prices:
      self.assertEqual(getRatio(price['A'], price['B']), (price['A']/price['B']))
  
  def test_getRatio_computeRatioPriceBZero(self):
    # fake data
    prices = [ 
      {'A': 2.00, 'B': 0}, {'A': 7.00, 'B': 0}, {'A': 9.34, 'B': 0}, {'A': 25.76, 'B': 0}, {'A': 105.24, 'B': 0}
    ]
    # assertion to test method
    for price in prices:
      self.assertEqual(getRatio(price['A'], price['B']), None)

  def test_getRatio_computeRatioPriceAZero(self):
    # fake data
    prices = [ 
      {'A': 0, 'B': 5.00}, {'A': 0, 'B': 3.00}, {'A': 0, 'B': 7.34}, {'A': 0, 'B': 98.75}, {'A': 0, 'B': 53.64}
    ]
    # assertion to test method
    for price in prices:
      self.assertEqual(getRatio(price['A'], price['B']), 0)
      
if __name__ == '__main__':
    unittest.main()
