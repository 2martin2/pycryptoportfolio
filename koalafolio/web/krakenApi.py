# -*- coding: utf-8 -*-
"""
Created on Sun Sep  15 15:15:19 2019

@author: Martin
"""
import pandas as pd
import krakenex
import pykrakenapi
import datetime

# help(pykrakenapi.KrakenAPI)

def initApi(key, secret):
    api = krakenex.API(key=key, secret=secret)
    k = pykrakenapi.KrakenAPI(api)
    return k

def getTradeHistory(key, secret):
    k = initApi(key, secret)
    trades = []
    tradeHistory = k.get_trades_history()
    trades.append(tradeHistory[0])
    numTrades = len(trades[0])
    while(numTrades < tradeHistory[1]):
        tradeHistory = k.get_trades_history(ofs=numTrades)
        trades.append(tradeHistory[0])
        numTrades += len(trades[-1])
    newTradeHistory = pd.concat(trades).reset_index()

    def removeNs(date):
        return str(date)[:-3]
    newTradeHistory['dtime'] = newTradeHistory['dtime'].apply(removeNs)
    return newTradeHistory




# k = initApi(apiKey, privateKey)

# balances = k.get_account_balance()
# assets = k.get_asset_info()
# closed_orders = k.get_closed_orders()
# ledgers = k.get_ledgers_info()
# servertime = k.get_server_time()
# trade_history = k.get_trades_history()



