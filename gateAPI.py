#!/usr/bin/python
# -*- coding: utf-8 -*-

from HttpUtil import getSign,httpGet,httpPost

class GateIO:

    def __init__(self,url,apikey,secretkey):
        self.__url = url
        self.__apikey = apikey
        self.__secretkey = secretkey

    # All trading pairs
    def pairs(self):
        URL = "/api2/1/pairs"
        params=''
        return httpGet(self.__url,URL,params)


    # Market order parameters
    def marketinfo(self):
        URL = "/api2/1/marketinfo"
        params=''
        return httpGet(self.__url,URL,params)

    # Подробные рыночные операции
    def marketlist(self):
        URL = "/api2/1/marketlist"
        params=''
        return httpGet(self.__url,URL,params)

    # All trading quotes
    def tickers(self):
        URL = "/api2/1/tickers"
        params=''
        return httpGet(self.__url,URL,params)

    # Single transaction market
    def ticker(self,param):
        URL = "/api2/1/ticker"
        return httpGet(self.__url,URL,param)


    # Все сделки на рынке
    def orderBooks(self):
        URL = "/api2/1/orderBooks"
        param=''
        return httpGet(self.__url, URL, param)


    # Individual transactions on the market depth
    def orderBook(self,param):
        URL = "/api2/1/orderBook"
        return httpGet(self.__url, URL, param)


    # Исторические записи
    def tradeHistory(self, param):
        URL = "/api2/1/tradeHistory"
        return httpGet(self.__url, URL, param)

    # Get account funds balance
    def balances(self):
        URL = "/api2/1/private/balances"
        param = {}
        return httpPost(self.__url,URL,param,self.__apikey,self.__secretkey)


    # Получить адрес пополнения
    def depositAddres(self,param):
        URL = "/api2/1/private/depositAddress"
        params = {'currency':param}
        return httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)


    # Get reload history
    def depositsWithdrawals(self, start,end):
        URL = "/api2/1/private/depositsWithdrawals"
        params = {'start': start,'end':end}
        return httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)


    # Buy
    def buy(self, currencyPair,rate, amount):
        URL = "/api2/1/private/buy"
        params = {'currencyPair': currencyPair,'rate':rate,'amount':amount}
        return httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)

    # Sell
    def sell(self, currencyPair, rate, amount):
        URL = "/api2/1/private/sell"
        params = {'currencyPair': currencyPair, 'rate': rate, 'amount': amount}
        return httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)

    # cancel order
    def cancelOrder(self, orderNumber, currencyPair):
        URL = "/api2/1/private/cancelOrder"
        params = {'orderNumber': orderNumber, 'currencyPair': currencyPair}
        return httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)


    # Cancel all orders
    def cancelAllOrders(self, type, currencyPair):
        URL = "/api2/1/private/cancelAllOrders"
        params = {'type': type, 'currencyPair': currencyPair}
        return httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)


    # Get order status
    def getOrder(self, orderNumber, currencyPair):
        URL = "/api2/1/private/getOrder"
        return httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)


    # Get my current pending list
    def openOrders(self):
        URL = "/api2/1/private/openOrders"
        params = {}
        return httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)


    # Get my 24 hours transaction records
    def mytradeHistory(self,currencyPair,orderNumber):
        URL = "/api2/1/private/tradeHistory"
        params = {'currencyPair': currencyPair, 'orderNumber': orderNumber}
        return httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)

    # withdraw
    def withdraw(self,currency,amount,address):
        URL = "/api2/1/private/withdraw"
        params = {'currency': currency, 'amount': amount,'address':address}
        return httpPost(self.__url, URL, params, self.__apikey, self.__secretkey)
