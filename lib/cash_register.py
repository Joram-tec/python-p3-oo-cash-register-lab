#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.extend([title] * quantity)
        
    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total * (1 - self.discount/100))
            print(f"After the discount, the total comes to ${self.total}.")
            return True
        else:
            print("There is no discount to apply.")
            return False
            
    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0    