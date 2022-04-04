from catalogue import Catalogue
from customer import Customer
from item import Item
from shopping_cart_items import ShoppingCartItems
from order import Order


class Shopping:
    def __init__(self, some_items):
        self.customer = Customer()
        self.catalogue = Catalogue(some_items)
        self.cart = ShoppingCartItems(self.catalogue)
        self.order = 0
        self.order_number = 1



    def shopping(self):
        print("enter 'help' for a list of commands")
        checkout_flag = True
        while checkout_flag:
            customer_input = input('Please enter a command: ')
            if customer_input == 'help':
                print('show catalogue, show basket, show total price,'
                      ' add item, remove item, checkout')
            elif customer_input == 'show catalogue':
                self.catalogue.pretty_print_catalogue()
            elif customer_input == 'show basket':
                print(self.cart)
            elif customer_input == 'show total price':
                print('£' + str(self.cart.get_total_price()))
            elif customer_input == 'add item':
                product_id = int(input('Enter a product ID: '))
                quantity = int(input('Enter a quantity: '))
                self.cart.add_item(product_id,quantity)
            elif customer_input == 'remove item':
                product_id = int(input('Enter a product ID: '))
                self.cart.remove_item(product_id)
            elif customer_input == 'checkout':
                self.checkout()
                checkout_flag = False
            elif customer_input == 'quit':
                for product in self.catalogue.catalogue_dict.keys():
                    self.cart.remove_item(product)
                checkout_flag = False





    def checkout(self):

        print('Please enter delivery address')
        self.customer.set_delivery_address()
        print('Please enter invoice address')
        self.customer.set_invoice_address()
        print('Please enter delivery note')
        self.customer.set_delivery_note()
        print('Please enter payment details')
        self.customer.set_payment_card()
        print('Please enter an email for the receipt')
        customer_email = input('email address: ')
        self.order_number += 1
        self.order = Order(self.order_number,self.cart,self.cart.get_total_price(),
                           self.customer.invoice_address, self.customer.delivery_address,
                           self.customer.delivery_note,self.customer.payment_card)
        print(f'A receipt has been sent to {customer_email}')


    def run_program(self):
        orders = []
        while True:
            customer_input = input('Would you like to shop? (yes/no): ')
            if customer_input == 'yes':
                shopping_session = Shopping(items)
                shopping_session.shopping()
                orders.append(shopping_session.order)


            elif customer_input == 'no':
                if self.order_number >= 1:
                    print(f'You made {self.order_number-1} orders:')
                    for order in orders:
                        print(order)
                break

            else:
                pass


item0 = Item('The Fame',4.70,1000)
item1 = Item('The Fame Monster', 5.98, 1500)
item2 = Item('Born This Way', 4.39, 2000)
item3 = Item('ARTPOP', 6.19, 2000)
item4 = Item('Cheek to Cheek', 6.79, 2000)
item5 = Item('Joanne', 6.99, 2000)
item6 = Item('A Star Is Born Soundtrack', 5.62, 2000)
item7 = Item('Chromatica', 9.00, 0)
item8 = Item('BORN THIS WAY THE TENTH ANNIVERSARY', 14.49, 2000)
item9 = Item('Dawn of Chromatica', 10.99, 2000)
item10 = Item('Love For Sale', 8.94, 2000)
items = [item0,item1,item2,item3,item4,item5,item6,item7,item8,item9,item10]

Shopping(items).run_program()
