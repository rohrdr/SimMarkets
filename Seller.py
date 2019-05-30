# -*- coding: utf-8 -*-

import numpy as np

class Seller():
    
    def __init__(self, name, money=0, goods=1, cost=0.3, high=1.0):
        
        self.money = money
        self.goods = goods
        self.cost = cost
        self.high = high
        self.name = name
        
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
