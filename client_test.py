import unittest

from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    result = [getDataPoint(quote) for quote in quotes]
    expected = [("ABC", 120.48,121.2,120.84),("DEF",117.87,121.68, 119.775)]
    self.assertEqual(result, expected)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    result = [getDataPoint(quote) for quote in quotes]
    expected = [("ABC", 120.48, 119.2, 119.84), ("DEF",117.87,121.68,119.775)]
    self.assertEqual(result, expected)

  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    test = [123.87, 258.25]
    error_margin = 0.0000000001

    result = getRatio(test[0],test[1])
    expected = 0.4796515004840271
    self.assertAlmostEqual(expected, result, error_margin)

  def test_getRatio_price_aIsZero(self):
    test = [0, 22.3]
    result = getRatio(test[0],test[1])
    expected = 0
    self.assertEqual(result,expected)
  def test_getRatio_price_bIsZero(self):
    test = [23.45, 0]
    result = getRatio(test[0],test[1])
    self.assertIsNone(result)
if __name__ == '__main__':
    unittest.main()
