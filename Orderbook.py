# -*- coding: utf-8 -*-

import numpy as np


class Orderbook():
    
    def __init__(self, ask=None, bid=None):
        
        self.ask = ask
        self.bid = bid
                
        return
    
    def askbid(self, ask, bid):
        
        trade = False
        price = -999
        
        if ask < self.ask: self.ask = ask
        if bid > self.bid: self.bid = bid
        
        if self.ask < self.bid:
            trade = True
            price = (self.ask + self.bid) / 2.0
        
        return trade, price