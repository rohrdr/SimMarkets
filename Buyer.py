# -*- coding: utf-8 -*-

import numpy as np

class Buyer():
    
    def __init__(self, money, goods, value, low):
        
        self.money = money
        self.goods = goods
        self.value = value
        self.low = low
        
        return
    
    
    def make_bid(self):
        bid = np.random.uniform(low=self.orderbook.bid, high=min(self.value, self.money))
#        print('BUYER: low: {:10.4f} high: {:10.4f} bid: {:10.4f}'.format(self.orderbook.bid, min(self.value, self.money),bid))        
        return bid
    
    
    def set_cost(self, cost):
        
        return
    
    def set_buyer_orderbook(self, orderbook):
        
        self.orderbook = orderbook
        
        return
    
    
#    def make_trade(self, price):
#        
#        self.money -= price
#        self.goods += 1
#
#        return