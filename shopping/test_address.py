import unittest

from address import Address


class MyTestCase(unittest.TestCase):
    def test_address_constructor(self):
        address = Address('line1', 'line2', 'city', 'postcode')
        self.assertEqual(address.line1, 'line1')
        self.assertEqual(address.line2, 'line2')
        self.assertEqual(address.city, 'city')
        self.assertEqual(address.postcode,'postcode')


if __name__ == '__main__':
    unittest.main()
