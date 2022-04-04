import unittest

from shopping_cart_items import ShoppingCartItems
from catalogue import Catalogue
from item import Item




class MyTestCase(unittest.TestCase):
    def test_get_total_price(self):
        item1 = Item('test item 1', 2, 1000)
        item2 = Item('test item 2', 3, 2000)
        catalogue = Catalogue([item1,item2])
        cart = ShoppingCartItems(catalogue)
        cart.add_item(0,3)
        self.assertEqual(cart.get_total_price(), 6)

    def test_add_item(self):
        item1 = Item('test item 1', 2, 1000)
        item2 = Item('test item 2', 3, 2000)
        catalogue = Catalogue([item1,item2])
        cart = ShoppingCartItems(catalogue)
        cart.add_item(0,3)
        self.assertEqual(cart.cart, {item1:3})

    def test_add_item_duplicate(self):
        item1 = Item('test item 1', 2, 1000)
        item2 = Item('test item 2', 3, 2000)
        catalogue = Catalogue([item1,item2])
        cart = ShoppingCartItems(catalogue)
        cart.add_item(0,3)
        cart.add_item(0,3)
        self.assertEqual(cart.cart, {item1:6})

    def test_add_item_that_doesnt_exist(self):
        item1 = Item('test item 1', 2, 1000)
        item2 = Item('test item 2', 3, 2000)
        catalogue = Catalogue([item1,item2])
        cart = ShoppingCartItems(catalogue)
        cart.add_item(2,3)
        self.assertEqual(cart.cart, {})

    def test_add_item_negative_quantity(self):
        item1 = Item('test item 1', 2, 1000)
        item2 = Item('test item 2', 3, 2000)
        catalogue = Catalogue([item1,item2])
        cart = ShoppingCartItems(catalogue)
        cart.add_item(0,-3)
        self.assertEqual(cart.cart, {})

    def test_add_remove_item(self):
        item1 = Item('test item 1', 2, 1000)
        item2 = Item('test item 2', 3, 2000)
        catalogue = Catalogue([item1,item2])
        cart = ShoppingCartItems(catalogue)
        cart.add_item(0,3)
        cart.remove_item(0)
        self.assertEqual(cart.cart, {})

    def test_add_remove_item_not_in_cart(self):
        item1 = Item('test item 1', 2, 1000)
        item2 = Item('test item 2', 3, 2000)
        catalogue = Catalogue([item1,item2])
        cart = ShoppingCartItems(catalogue)
        cart.add_item(0,3)
        cart.remove_item(2)
        self.assertEqual(cart.cart, {item1 : 3})





if __name__ == '__main__':
    unittest.main()