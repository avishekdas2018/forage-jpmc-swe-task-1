import unittest
from client3 import getDataPoint, getRatio

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
  class ClientTest(unittest.TestCase):
    def test_getRatio_PriceBZero(self):
        price_a = 10.0
        price_b = 0.0
        expected_result = "Cannot divide by Zero"
        self.assertEqual(getRatio(price_a, price_b), expected_result)

    def test_getRatio_PriceAZero(self):
        price_a = 0.0
        price_b = 20.0
        expected_result = 0.0
        self.assertEqual(getRatio(price_a, price_b), expected_result)

    def test_getRatio_PriceAAndBZero(self):
        price_a = 0.0
        price_b = 0.0
        expected_result = "Cannot divide by Zero"
        self.assertEqual(getRatio(price_a, price_b), expected_result)

    def test_getRatio_NormalCase(self):
        price_a = 15.0
        price_b = 5.0
        expected_result = 3.0
        self.assertEqual(getRatio(price_a, price_b), expected_result)








if __name__ == '__main__':
    unittest.main()
