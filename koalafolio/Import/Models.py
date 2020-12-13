# -*- coding: utf-8 -*-

import koalafolio.Import.RegexPatterns as pat
import koalafolio.Import.Converter as converter


class Importmodel:
    def __init__(self):
        self.modelName = ''
        self.modelHeaders = []
        self.headerRegexNeeded = []
        self.headerRegexAll = []
        self.contentRegexAll = []
        self.modelCallback = None

    def convertDataFrame(self, dataFrame):
        matchedHeaders, matchedHeaderNames = self.match(dataFrame.columns.tolist())
        return self.modelCallback(matchedHeaderNames, dataFrame)

    def isMatch(self, headers):  # check if all needed Headers are included in CSV Headers
        #        headerMatchs = []
        for headerRegex in self.headerRegexNeeded:
            headerMatch = 0
            for header in headers:
                if headerRegex.match(header):
                    headerMatch = 1
                    break
            if headerMatch == 0:
                return False
        #            headerMatchs.append(headerMatch)
        return True

    def match(self, headers):  # match every regexpattern of import model with CSV Headers
        headerMatchs = []
        headerMatchNames = []
        #        headerMatchNamesDict = {}
        #        i = -1
        for headerRegex in self.headerRegexAll:
            #            i += 1
            headerMatch = 0
            headerMatchName = ''
            for header in headers:
                matchTemp = headerRegex.match(header)
                if matchTemp:
                    headerMatch = 1
                    headerMatchName = matchTemp.group(0)
                    #                    headerMatchNamesDict[self.modelHeaders[i]] = headerMatchName
                    break
            headerMatchs.append(headerMatch)
            headerMatchNames.append(headerMatchName)
        return headerMatchs, headerMatchNames


IMPORT_MODEL_LIST = []
index = -1

# %% exodus [DATE,TYPE,OUTAMOUNT,OUTCURRENCY,FEEAMOUNT,FEECURRENCY,OUTTXID,OUTTXURL,INAMOUNT,INCURRENCY,INTXID,INTXURL,ORDERID]
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['DATE', 'TYPE', 'OUTAMOUNT', 'OUTCURRENCY', 'FEEAMOUNT', 'FEECURRENCY', 'OUTTXID', 'OUTTXURL',
                                         'INAMOUNT', 'INCURRENCY', 'INTXID', 'INTXURL', 'ORDERID']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.EXODUS_DATE_REGEX, pat.EXODUS_TYPE_REGEX,
                                              pat.EXODUS_OUTAMOUNT_REGEX, pat.EXODUS_OUTCURRENCY_REGEX,
                                              pat.EXODUS_FEEAMOUNT_REGEX, pat.EXODUS_FEECURRENCY_REGEX,
                                              pat.EXODUS_OUTTXID_REGEX, pat.EXODUS_OUTTXURL_REGEX,
                                              pat.EXODUS_INAMOUNT_REGEX, pat.EXODUS_INCURRENCY_REGEX,
                                              pat.EXODUS_INTXID_REGEX, pat.EXODUS_INTXURL_REGEX,
                                              pat.EXODUS_ORDERID_REGEX]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_exodus

# %% kraken ["txid","ordertxid","pair","time","type","ordertype","price","cost","fee","vol","margin","misc","ledgers"]
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['txid', 'ordertxid', 'pair', 'time', 'type', 'ordertype', 'price', 'cost',
                                         'fee', 'vol', 'margin', 'misc', 'ledgers']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.KRAKEN_TXID_REGEX, pat.KRAKEN_ORDERTXID_REGEX,
                                              pat.KRAKEN_PAIR_REGEX, pat.KRAKEN_TIME_REGEX, pat.KRAKEN_TYPE_REGEX,
                                              pat.KRAKEN_ORDERTYPE_REGEX,
                                              pat.KRAKEN_PRICE_REGEX, pat.KRAKEN_COST_REGEX, pat.KRAKEN_FEE_REGEX,
                                              pat.KRAKEN_VOL_REGEX,
                                              pat.KRAKEN_MARGIN_REGEX, pat.KRAKEN_MISC_REGEX, pat.KRAKEN_LEDGERS_REGEX]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_kraken

# %% krakenapi [txid,ordertxid,pair,dtime,type,ordertype,price,cost,fee,vol,margin,misc,postxid,time]
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['txid', 'ordertxid', 'pair', 'dtime', 'type', 'ordertype', 'price', 'cost',
                                         'fee', 'vol', 'margin', 'misc', 'postxid', 'time']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.KRAKENAPI_TXID_REGEX, pat.KRAKENAPI_ORDERTXID_REGEX,
                                              pat.KRAKENAPI_PAIR_REGEX, pat.KRAKENAPI_DTIME_REGEX,
                                              pat.KRAKENAPI_TYPE_REGEX, pat.KRAKENAPI_ORDERTYPE_REGEX,
                                              pat.KRAKENAPI_PRICE_REGEX, pat.KRAKENAPI_COST_REGEX,
                                              pat.KRAKENAPI_FEE_REGEX, pat.KRAKENAPI_VOL_REGEX,
                                              pat.KRAKENAPI_MARGIN_REGEX, pat.KRAKENAPI_MISC_REGEX,
                                              pat.KRAKENAPI_POSTXID_REGEX, pat.KRAKENAPI_TIME_REGEX]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_krakenapi

# %% binance ['Date(UTC)', 'Market', 'Type', 'Price', 'Amount', 'Total', 'Fee', 'Fee Coin']
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['Date', 'Market', 'Type', 'Price', 'Amount', 'Total', 'Fee', 'Fee Coin']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.BINANCE_DATE_REGEX, pat.BINANCE_MARKET_REGEX,
                                              pat.BINANCE_TYPE_REGEX, pat.BINANCE_PRICE_REGEX, pat.BINANCE_AMOUNT_REGEX,
                                              pat.BINANCE_TOTAL_REGEX,
                                              pat.BINANCE_FEE_REGEX, pat.BINANCE_FEECOIN_REGEX]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_binance

# %% poloniex model ['Date', 'Market', 'Category', 'Type', 'Price', 'Amount', 'Total', 'Fee', 'Order Number', 'Base Total Less Fee', 'Quote Total Less Fee']
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['Date', 'Market', 'Category', 'Type', 'Price', 'Amount', 'Total', 'Fee',
                                         'Order Number', 'Base Total Less Fee', 'Quote Total Less Fee']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.POLONIEX_DATE_REGEX, pat.POLONIEX_MARKET_REGEX,
                                              pat.POLONIEX_CATEGORY_REGEX,
                                              pat.POLONIEX_TYPE_REGEX, pat.POLONIEX_PRICE_REGEX,
                                              pat.POLONIEX_AMOUNT_REGEX, pat.POLONIEX_TOTAL_REGEX,
                                              pat.POLONIEX_FEE_REGEX, pat.POLONIEX_ORDERNUMBER_REGEX,
                                              pat.POLONIEX_BASETOTALLESSFEE_REGEX, pat.POLONIEX_QUOTETOTALLESSFEE_REGEX]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_poloniex

# model bittrex [Uuid	Exchange	TimeStamp	OrderType	Limit	Quantity	QuantityRemaining	Commission	Price	PricePerUnit	IsConditional	Condition	ConditionTarget	ImmediateOrCancel	Closed]
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['Uuid','Exchange','TimeStamp','OrderType','Limit','Quantity',
                                         'QuantityRemaining','Commission','Price','PricePerUnit','IsConditional',
                                         'Condition','ConditionTarget','ImmediateOrCancel','Closed']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.BITTREX_UUID_REGEX, pat.BITTREX_EXCHANGE_REGEX,
                                              pat.BITTREX_TIMESTAMP_REGEX, pat.BITTREX_ORDERTYPE_REGEX,
                                              pat.BITTREX_LIMIT_REGEX, pat.BITTREX_QUANTITY_REGEX,
                                              pat.BITTREX_QUANTITYREMAINING_REGEX, pat.BITTREX_COMMISSION_REGEX,
                                              pat.BITTREX_PRICE_REGEX, pat.BITTREX_PRICEPERUNIT_REGEX,
                                              pat.BITTREX_ISCONDITIONAL_REGEX, pat.BITTREX_CONDITION_REGEX,
                                              pat.BITTREX_CONDITIONTARGET_REGEX, pat.BITTREX_IMMEDIATEORCANCEL_REGEX,
                                              pat.BITTREX_CLOSED_REGEX]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_bittrex

# %% model 0: Date, Type, Pair, Average Price, Amount, (ID), (Total), (Fee), (FeeCoin), (State), (ExchangeName)
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['date', 'type', 'pair', 'price_average', 'amount', 'id', 'price_total', 'fee',
                                         'feeCoin', 'state', 'exchangeName']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.DATE_REGEX, pat.TYPE_REGEX, pat.PAIR_REGEX_0,
                                              pat.PRICE_AVERAGE_REGEX_0, pat.AMOUNT_SUB_REGEX_0]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded + [pat.ID_REGEX,
                                                                                        pat.AMOUNT_MAIN_REGEX_0,
                                                                                        pat.FEE_REGEX,
                                                                                        pat.FEECOIN_REGEX,
                                                                                        pat.STATUS_REGEX]
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_0

# %% model 1: Date, Type, Exchange, Average Price, Amount, (ID), (Total), (Fee), (FeeCoin)
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['date', 'type', 'exchange', 'price_average', 'amount', 'id', 'price_total',
                                         'fee', 'feeCoin']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.DATE_REGEX, pat.TYPE_REGEX, pat.PAIR_REGEX_1,
                                              pat.PRICE_AVERAGE_REGEX_1, pat.AMOUNT_SUB_REGEX_1]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded + [pat.ID_REGEX,
                                                                                        pat.AMOUNT_MAIN_REGEX_1,
                                                                                        pat.FEE_REGEX,
                                                                                        pat.FEECOIN_REGEX]
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_1

# %% model 2: Date, Type, Pair, Amount sub, Amount main, (id), (fee), (feecoin)
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['date', 'type', 'pair', 'amount_sub', 'amount_main', 'id', 'fee', 'feeCoin']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.DATE_REGEX, pat.TYPE_REGEX, pat.PAIR_REGEX_2, pat.AMOUNT_SUB_REGEX_2,
                                              pat.AMOUNT_MAIN_REGEX_2]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded + [pat.ID_REGEX, pat.FEE_REGEX,
                                                                                        pat.FEECOIN_REGEX]
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_2

# %% model 3: Date, type, Coin, Amount, (id), (fee)
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['date', 'type', 'coin', 'amount', 'id', 'fee']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.DATE_REGEX, pat.TYPE_REGEX, pat.COIN_REGEX_3, pat.AMOUNT_REGEX_3]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded + [pat.ID_REGEX, pat.FEE_REGEX]
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_3

# %% model 4 (bitcoin.de): Date, Type, Pair, amount_main_wo, amount_sub_wo, amount_main_w_fees, amount_sub_w_fees, (ID), (ZuAbgang)
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['date', 'type', 'pair', 'amount_main_wo_fee', 'amount_sub_wo_fee',
                                         'amount_main_w_fee', 'amount_main_w_fee_fidor', 'amount_sub_w_fee', 'id']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.DATE_REGEX, pat.TYPE_REGEX, pat.BITCOIN_PAIR_REGEX_4,
                                              pat.AMOUNT_MAIN_WO_FEE_REGEX_4, pat.AMOUNT_SUB_WO_FEE_REGEX_4,
                                              pat.AMOUNT_MAIN_W_FEE_REGEX_4, pat.AMOUNT_SUB_W_FEE_REGEX_4]
IMPORT_MODEL_LIST[index].headerRegexAll = \
    IMPORT_MODEL_LIST[index].headerRegexNeeded + [pat.ID_REGEX, pat.AMOUNT_ZUABGANG_REGEX_4,
                                                  pat.AMOUNT_MAIN_W_FEE_FIDOR_REGEX_4,
                                                  pat.BITCOINDE_EINHEIT_AMOUNT_MAIN_WO_FEE_REGEX,
                                                  pat.BITCOINDE_EINHEIT_AMOUNT_MAIN_W_FEE_REGEX,
                                                  pat.BITCOINDE_EINHEIT_KURS_REGEX]
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_4

# %% model 5: Date, Pair, Average Price, Amount, (ID), (Total), (Fee), (FeeCoin), (State)
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['date', 'pair', 'price_average', 'amount', 'id', 'price_total', 'fee',
                                         'feeCoin', 'state']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.DATE_REGEX, pat.PAIR_REGEX_5, pat.PRICE_AVERAGE_REGEX_5,
                                              pat.AMOUNT_SUB_REGEX_5]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded + [pat.ID_REGEX,
                                                                                        pat.AMOUNT_MAIN_REGEX_5,
                                                                                        pat.FEE_REGEX,
                                                                                        pat.FEECOIN_REGEX,
                                                                                        pat.STATUS_REGEX]
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_5

# %% model template1: "date","type","buy amount","buy cur","sell amount","sell cur",("exchange"),("fee amount"),("fee currency")
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelName = 'Template1'
IMPORT_MODEL_LIST[index].modelHeaders = ['DATE', 'TYPE', 'BUY_AMOUNT', 'BUY_CUR', 'SELL_AMOUNT', 'SELL_CUR',
                                         'EXCHANGE', 'FEE_AMOUNT', 'FEE_CURRENCY']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.TEMPLATE1_DATE_REGEX, pat.TEMPLATE1_TYPE_REGEX,
                                              pat.TEMPLATE1_BUY_AMOUNT_REGEX, pat.TEMPLATE1_BUY_CUR_REGEX,
                                              pat.TEMPLATE1_SELL_AMOUNT_REGEX, pat.TEMPLATE1_SELL_CUR_REGEX]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded \
                                          + [pat.TEMPLATE1_EXCHANGE_REGEX, pat.TEMPLATE1_FEE_AMOUNT_REGEX,
                                             pat.TEMPLATE1_FEE_CURRENCY_REGEX]
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_Template1


# %% model tradeList: 'date', 'type', 'coin', 'amount', 'id', 'tradePartnerId', 'valueLoaded', 'exchange', 'externId', 'wallet'
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['date', 'type', 'coin', 'amount', 'id', 'tradePartnerId',
                                         'valueLaoded', 'exchange', 'externId', 'wallet']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.TRADELIST_DATE_REGEX, pat.TRADELIST_TYPE_REGEX,
                                              pat.TRADELIST_COIN_REGEX, pat.TRADELIST_AMOUNT_REGEX]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded \
                                          + [pat.TRADELIST_ID_REGEX, pat.TRADELIST_TRADEPARTNERID_REGEX,
                                             pat.TRADELIST_VALUELOADED_REGEX, pat.TRADELIST_EXCHANGE_REGEX,
                                             pat.TRADELIST_EXTERNID_REGEX, pat.TRADELIST_WALLET_REGEX]
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_TradeList

# %% model rotki: ,timestamp,location,pair,trade_type,amount,rate,fee,fee_currency,link,notes
index = index + 1
IMPORT_MODEL_LIST.append(Importmodel())
IMPORT_MODEL_LIST[index].modelHeaders = ['timestamp', 'location', 'pair', 'trade_type', 'amount', 'rate',
                                         'fee', 'fee_currency', 'link']
IMPORT_MODEL_LIST[index].headerRegexNeeded = [pat.ROTKI_TIMESTAMP_REGEX, pat.ROTKI_LOCATION_REGEX, pat.ROTKI_PAIR_REGEX,
                                              pat.ROTKI_TRADE_TYPE_REGEX, pat.ROTKI_AMOUNT_REGEX, pat.ROTKI_RATE_REGEX,
                                              pat.ROTKI_FEE_REGEX, pat.ROTKI_FEE_CURRENCY_REGEX, pat.ROTKI_LINK_REGEX]
IMPORT_MODEL_LIST[index].headerRegexAll = IMPORT_MODEL_LIST[index].headerRegexNeeded
IMPORT_MODEL_LIST[index].modelCallback = converter.modelCallback_Rotki