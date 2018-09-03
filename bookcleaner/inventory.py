from __future__ import print_function
from __future__ import division

import pandas as pd

class TradeStrat(object):
    
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.comdty = symbol[:2]

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
        TradeCouple.__init__(target, hedge)



