"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget, exchange_rate):
    """
    This function will exchange money based on the exchange rate. 
    
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    This function will calculate currency left after an exchange.
    
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    This function will calculate the value of bills.
    
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    This function will calculate the number of bills.
    
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    # Use the // twice to truncate since bills need to be whole numbers; no such thing as partial bills unless you use scissors.
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """
    This function will calculate the leftover after exchanging into bills.
    
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    This function will calculate value after exchange.
    
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    if spread == 0:
        new_budget = budget / exchange_rate
    
    else: 
        adjusted_exchange = spread * .01 * exchange_rate 
        final_rate = exchange_rate + adjusted_exchange
        new_budget = budget / final_rate
    # (budget // denomination) * denomination
    return (new_budget // denomination) * denomination  
