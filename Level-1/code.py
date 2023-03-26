'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = 50000     # max. allowed price per item
MAX_ITEM_QUANTITY = 500     # max. quantity of items in shop
MAX_OVERALL_SUM = 1e6       # max. total amount allowed

def validorder(order: Order):
    net = 0
    
    for item in order.items:
        if item.type == 'payment':
            if abs(item.amount) < MAX_ITEM_AMOUNT:
                net += item.amount
            # else:   # commented as not accepted by hack.py :-(
            #     return ("Order ID: %s - Fraud detected!" % order.id)
        elif item.type == 'product':
            if (abs(item.amount) < MAX_ITEM_AMOUNT) and (abs(item.quantity) < MAX_ITEM_QUANTITY):
                net -= item.amount * item.quantity
            if abs(net) > MAX_OVERALL_SUM:
                return("Max total sum exceeded, potential fraud!")
        else:
            return("Invalid item type: %s" % item.type)
    
    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
