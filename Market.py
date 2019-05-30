# -*- coding: utf-8 -*-

import numpy as np
from Buyer import Buyer
from Seller import Seller
from Orderbook import Orderbook

class Market():
    
    
    def __init__(self, buyer, seller, orderbook=Orderbook()):
        
        self.buyer = buyer
        self.seller = seller
        assert(seller.high > buyer.low)
        self.orderbook = orderbook
        self.orderbook.ask = self.seller.high
        self.orderbook.bid = self.buyer.low
        
        self.buyer.set_buyer_orderbook(self.orderbook)
        self.seller.set_seller_orderbook(self.orderbook)
        
        self.timesteps = 0
        self.ntransactions = 0
        self.transactions = []
        self.stats = []
        self.make_stats()
        
        return
    
    
    def time_step(self):
        
        self.timesteps += 1
        
        new_ask = self.seller.make_ask()
#        if new_ask < self.orderbook['ask']: self.orderbook['ask'] = new_ask
        
        new_bid = self.buyer.make_bid()
#        if new_bid > self.orderbook['bid']: self.orderbook['bid'] = new_bid
        
        trade, price = self.orderbook.askbid(new_ask, new_bid)
        self.make_stats()
        ask = self.orderbook.ask
        bid = self.orderbook.bid        
        
        if trade:
#            print('trade has been detected')
#            print('ASK: {:10.4f} BID: {:10.4f}'.format(ask, bid))
            self.make_transaction(price)
            self.orderbook.ask = self.seller.high
            self.orderbook.bid = self.buyer.low
            self.timesteps = 0
            self.make_stats()
            
        self.buyer.set_cost(self.orderbook.ask)
        self.seller.set_value(self.orderbook.bid)
        
        
        return trade, ask, bid, price
    
    
    def make_trade(self, price):
        
#        print('trade is being made at ', price)
        self.buyer.money -= price
        self.buyer.goods += 1
        self.seller.money += price
        self.seller.goods -= 1
        
        return

    
    def make_transaction(self, price):
        
        self.transactions.append([
                price,
                self.ntransactions
                ])
    
        self.make_trade(price)
        self.ntransactions += 1
        
    
        return


    def make_stats(self):
        
        self.stats.append([
                self.orderbook.ask, 
                self.orderbook.bid,
                self.timesteps
                ])
        
        return    
    
    
    def settle_ask(self):
        
        price = self.orderbook.ask
        self.make_transaction(price)
        self.orderbook.ask = self.seller.high
        self.buyer.set_cost(self.orderbook.ask)
        self.timesteps = 0
        self.make_stats()
        
        return
        
    
    def settle_bid(self):
        
        price = self.orderbook.bid
        self.make_transaction(price)
        self.orderbook.bid = self.buyer.low
        self.seller.set_value(self.orderbook.bid)
        self.timesteps = 0
        self.make_stats()
        
        return