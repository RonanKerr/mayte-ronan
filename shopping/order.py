from address import Address
from card import Card


class Order:
    # feel free to change according to your model
    def __init__(self, order_number: int, order_quantity_by_item: dict,
                 order_cost: float, invoice_address: Address,
                 delivery_address: Address, delivery_note: str, payment_card: Card):
        self.order_number = order_number
        self.order_quantity_by_item = order_quantity_by_item
        self.order_cost = order_cost
        self.invoice_address = invoice_address
        self.delivery_address = delivery_address
        self.delivery_note = delivery_note
        self.payment_card = payment_card

    def __repr__(self):
        return f'''
------------ order {self.order_number} ------------
{self.order_quantity_by_item}
Total Cost: £{self.order_cost}

Invoice Address:

{self.invoice_address}
    
Delivery Address:

{self.delivery_address}

Delivery Note: {self.delivery_note}

Payment Details:
{self.payment_card}
---------------------------------

              '''
