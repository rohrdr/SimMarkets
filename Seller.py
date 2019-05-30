# -*- coding: utf-8 -*-

import numpy as np

class Seller():
    
    def __init__(self, money, goods, cost, high):
        
        self.money = money
        self.goods = goods
        self.cost = cost
        self.high = high
        
        return
    
    
    def make_ask(self):
        ask = np.random.uniform(low=self.cost, high=self.orderbook.ask)
#        print('SELLER: low: {:10.4f} high: {:10.4f} ask: {:10.4f}'.format(self.cost, self.orderbook.ask, ask))
        
        return ask
    
    
    def set_value(self, value):
        
        return


    def set_seller_orderbook(self, orderbook):
        
        self.orderbook = orderbook
        
        return


#    def make_trade(self, price):
#        
#        self.money += price
#        self.goods -= 1
#        
#        return
