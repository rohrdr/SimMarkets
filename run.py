# -*- coding: utf-8 -*-

from Market import Market
from Seller import Seller
from Buyer import Buyer
from Arbitrageur import Arbitrageur
from Orderbook import Orderbook
import numpy as np


def print_stats(stats):

    print('AGG      ASK        BID        PRICE      ITERATIONS')

    stats = np.array(stats)
    average = stats.mean(axis=0)
    standarddev = stats.std(axis=0)
    maximum = stats.max(axis=0)
    minimum = stats.min(axis=0)

    print('mean {:10.4f} {:10.4f} {:10.4f} {:10.4f}'.\
          format(average[0], average[1], average[2], average[3]))
    print('std  {:10.4f} {:10.4f} {:10.4f} {:10.4f}'.\
          format(standarddev[0], standarddev[1], standarddev[2], standarddev[3]))
    print('min  {:10.4f} {:10.4f} {:10.4f} {:10.4f}'.\
          format(minimum[0], minimum[1], minimum[2], minimum[3]))
    print('max  {:10.4f} {:10.4f} {:10.4f} {:10.4f}'.\
          format(maximum[0], maximum[1], maximum[2], maximum[3]))
    
    return


def seller_buyer_game(ngames=1000, maxiterations=100, print_level=0):

    stats = []
    for i in range(ngames):
        mymarket = Market()
        iterations = 0
        loop = True
        if print_level > 0: print('ITERATIONS   CURRENT ASK   CURRENT BID')    
        while(loop):
            
            price_made, ask, bid, price = mymarket.time_step()
            iterations += 1
            if price_made: loop = False
            if print_level > 0: print('  {:3}       {:10.4f}      {:10.4f}'.\
                                      format(iterations, mymarket.orderbook.ask, mymarket.orderbook.bid))
            
        stats.append([ask, bid, price, iterations])
    print_stats(stats)
    
    return


def init_game(nmarkets, scale):
    
    bmoney = 1.0 * scale
    bgoods = 0
    bvalue = 0.8
    blow = 0.0
    
    smoney = 0.0
    sgoods = 1 * scale
    bhigh = 1.0
    bcost = 0.3
    
    narbiters = nmarkets-1
    amoney=0
    agoods=0
    acost=1.0
    avalue=0.0
    alow=0.0
    ahigh=1.0
    
    buyer = Buyer(money=bmoney, goods=bgoods, value=bvalue, low=blow)
    seller = Seller(money=smoney, goods=sgoods, high=bhigh, cost=bcost)
    
    arbiters = []
    for i in range(narbiters):
        arbiters.append(
                Arbitrageur(
                        money=amoney,
                        goods=agoods,
                        cost=acost,
                        value=avalue,
                        low=alow,
                        high=ahigh
                ))
        
    markets = [ Market(buyer=buyer, seller=arbiters[0], orderbook=Orderbook()) ]
    # we set i=0 so the also works for nmarkets=2
    i = 0
    for i in range(nmarkets-2):
        markets.append(Market(buyer=arbiters[i+1], seller=arbiters[i]))
    markets.append(Market(buyer=arbiters[i], seller=seller))
    
    return buyer, seller, arbiters, markets

f = ' {:7.4f}'
def print_agents(buyer, arbiters, seller):
    
    d = ' $:'
    g = ' goods:'
    c = ' cost:'
    v = ' value:'
    string = d + f + g + f + c + f + v + f
    bstring = 'BUYER  :' + string
    astring = 'ARBITER:' + string
    sstring = 'SELLER :' + string
            
    print(bstring.format(buyer.money, buyer.goods, 0, buyer.value))
    for arbiter in arbiters:
        print(astring.format(arbiter.money, arbiter.goods, arbiter.cost, arbiter.value))
    print(sstring.format(seller.money, seller.goods, seller.cost, 0))
    return

def print_markets(markets):
    
    for i, market in enumerate(markets):
        print('MARKET {}'.format(i))
        print_market(market)
    
    return

def print_market(market):
#    string = 'ASK:' + f + ' BID:' + f
#    print(string.format(market.orderbook.ask, market.orderbook.bid))
#     print('stats')
#     for i in market.stats:
#         print(i)

    for trans in market.transactions:
        print('Transaction # {:3}    Price: {:10.4f} '.format(trans[0], trans[1]))
        print('Orderbook')
        for orders in trans[2]:
            print('ASK: {:10.4f} BID: {:10.4f}'.format(orders[0], orders[1]))
        print('\n')

    return

def seller_arbitrageur_buyer_game(ngames=1000, nmarkets=2, maxiterations=100, print_level=0):
    

    buyer, seller, arbiters, markets = init_game(nmarkets, ngames)

    for i in range(ngames):
        print_agents(buyer, arbiters, seller)    
        iterations = 0
        loop = True
    
        while(loop):
            for index, market in enumerate(markets):
                trade, ask, bid, price = market.time_step()
                if print_level > 0: print_markets(markets)                
                if trade:
                    if print_level > 0:
                        print('trade was made in market ', index)
                        print_markets(markets)
                        print_agents(buyer, arbiters, seller)
                    loop = False
                    break
        
            iterations += 1
        
        for i, market in enumerate(markets[:index]):
            if print_level > 0: print('ask is settled in market ', i)
            market.settle_ask()
            if print_level > 0: print_agents(buyer, arbiters, seller)
            if print_level > 0: print_markets(markets)
            
        for i, market in enumerate(markets[index+1:]):
            if print_level > 0: print('bid is settled in market ', i)
            market.settle_bid()
            if print_level > 0: print_agents(buyer, arbiters, seller)
            if print_level > 0: print_markets(markets)
            
    print_markets(markets)
    print_agents(buyer, arbiters, seller)
    
    return

def main():

#    seller_buyer_game(ngames=10, print_level=0)
    
    seller_arbitrageur_buyer_game(ngames=1, print_level=0)

if __name__ == "__main__":
    main()
