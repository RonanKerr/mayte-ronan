from collections import defaultdict



class ShoppingCartItems:
    def __init__(self, catalogue):
        self.cart = defaultdict(int)
        self.catalogue = catalogue


    def get_total_price(self):
        total = 0
        for key in self.cart.keys():
            total += key.price * self.cart[key]
        return total

    def add_item(self,product_id, quantity = 1):
        try:
            if self.catalogue.catalogue_dict[product_id].stock_quantity - quantity >= 0 and quantity >= 0:
                self.cart[self.catalogue.catalogue_dict[product_id]] += quantity
                self.catalogue.catalogue_dict[product_id].stock_quantity -= quantity
                print('item added successfully')
            elif quantity < 0:
                print('Cant add a negative number of items to cart')
            else:
                print(f'There is only {self.catalogue.catalogue_dict[product_id].stock_quantity} of this item in stock \n'
                            'Would you like to add the maximum stock of this item?')
                user_input = str(input('y/n: '))
                if user_input == 'y':
                    self.add_item(product_id,self.catalogue.catalogue_dict[product_id].stock_quantity)
        except AttributeError:
            print('That product does not exist!')
            self.catalogue.catalogue_dict.pop(product_id) # for some reason, the above 'try' creates an
                                                          # item in the dictionary, even when that item
                                                          # didn't exist, so if it didnt exist we have to
                                                          # remove it at the end

    def remove_item(self,product_id):
        if self.catalogue.catalogue_dict[product_id] in self.cart:
            self.catalogue.catalogue_dict[product_id].stock_quantity += self.cart[self.catalogue.catalogue_dict[product_id]]
            self.cart.pop(self.catalogue.catalogue_dict[product_id])
            print('item removed successfully')

    def print_cart(self):
        print(self.cart)

    def __repr__(self):
        keys = self.cart.keys()
        string = ''
        for key in keys:
            string = string + f'Product: {key}, Quantity: {self.cart[key]}\n'
        return string








#item0 = Item('really long item name',15,1000)
#item1 = Item('item1', 12, 1500)
#item2 = Item('item2', 13, 2000)

#catalogue = Catalogue(item0,item1,item2)


#my_cart = ShoppingCartItems(catalogue)
#print(item0)

#my_cart.add_item(0,100)
#my_cart.add_item(1,10)

#print(my_cart.cart)
#catalogue.pretty_print_catalogue()

#my_cart.remove_item(1)
#print(my_cart.cart)
#catalogue.pretty_print_catalogue()

#print(my_cart.get_total_price())


#catalogue = Catalogue(item0, item1, item2)






