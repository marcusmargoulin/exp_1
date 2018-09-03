from __future__ import print_function
from __future__ import division

import pandas as pd
import utilsbook

class TradeStrat(object):
    
    def __init__(self, symbol, price, way):
        self.symbol = symbol
        self.price = price
        self.comdty = symbol[:2]
        assert int(way) in (-1, 1) 
        self.way = way

    def comp_commo(self, trade):
        return trade.comdty == self.comdty

    def print(self):
        template = '''
        {comdty}: symbol|price
        '''.format(comdty=self.comdty, symbol=self.symbol, price=self.price)
        print(template)


class TradeCouple(object):

    def __init__(self, target, hedge):
        self.target = target
        self.hedge = hedge


class TradeCoupleLME(TradeCouple):

    def __init__(self, target, hedge):
        assert target.comp_commo(hedge)
        assert target.way == -1 * hedge.way
        TradeCouple.__init__(target, hedge)


class SimpleInventory(object):

    def __init__(self, comdty, date):
        self.comdty = comdty
        self.date = date
        self.inv_trade = dict()
        self.max_key = 0

    def add_trade(self, trade):
        self.inv_trade[self.max_key] = trade
        self.max_key += 1

    def to_evolution(self, booker, ptf_main, ptf_client):
        if not self.inv_trade:
            return pd.DataFrame()
        else:
            res = pd.DataFrame()
            i = 0
            for _, trade in self.inv_trade.iteritems():
                res.loc[i] = booker.to_evolution(trade, ptf_main, ptf_client)
                i += 1
            return res

    def is_date(self, date):
        return utilsbook.get_date(self.date) == utilsbook.get_date(date)
    
    def is_comdty(self, comdty):
        return comdty == comdty

class StratInventory(object):

    def __init__(self, is_constraint):
        if is_constraint:
            self.ref_class = TradeCoupleLME
        else:
            self.ref_class = TradeCouple
                
