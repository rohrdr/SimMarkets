# -*- coding: utf-8 -*-

import numpy as np

class Arbitrageur():
    
    def __init__(self, money=0, goods=0, cost=1.0, value=0.0, low=0.0, high=1.0):
        
        self.money = money
        self.goods = goods
        self.cost = cost
        self.value = value
        self.low = low
        self.high = high
        
        return
    
    def set_value(self, value):
        
        self.value = value
        
        return
    
    def set_cost(self, cost):
        
        self.cost = cost
        
        return
    
    def set_seller_orderbook(self, orderbook):
        
        self.seller_orderbook = orderbook
        
        return

    def set_buyer_orderbook(self, orderbook):
        
        self.buyer_orderbook = orderbook
        
        return
    
    def make_bid(self):
        bid = np.random.uniform(low=self.buyer_orderbook.bid, high=min(self.seller_orderbook.bid, self.high))
#        print('ARBBID: low: {:10.4f} high: {:10.4f} bid: {:10.4f}'.\
#              format(self.buyer_orderbook.bid, min(self.seller_orderbook.bid, self.high), bid))
        return bid
    
    def make_ask(self):
        ask = np.random.uniform(low=max(self.buyer_orderbook.ask, self.low), high=self.seller_orderbook.ask)
#        print('ARBASK: low: {:10.4f} high: {:10.4f} ask: {:10.4f}'.\
#              format(max(self.buyer_orderbook.ask, self.low), self.seller_orderbook.ask, ask))
        return ask
