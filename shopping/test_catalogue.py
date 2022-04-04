import unittest
from item import Item
from catalogue import Catalogue




class MyTestCase(unittest.TestCase):

    def test_create_item(self):
        catalogue = Catalogue([])
        item1 = Item('test item',2,1000)
        catalogue.create_item(item1)
        self.assertEqual(catalogue.catalogue_dict, {0:item1})

    def test_view_catalogue(self):
        catalogue = Catalogue([])
        item1 = Item('test item',2,1000)
        catalogue.create_item(item1)
        self.assertEqual(catalogue.view_catalogue(), [[0, 'test item', 2, 1000]])




if __name__ == '__main__':
    unittest.main()
