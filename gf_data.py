import urllib
import urllib2
import pprint
import sys
import threading
import datetime
import ast
import random

from globals import *

testfile = TEMP_DIR+"temp_gs_stock_list.txt"
import os
try:
    os.mkdir(TEMP_DIR)
except:
    pass

def retrieveStockList(exchange, retrieve_count=20):
    '''get a list of stocks from google finance api

    Args:
        exchange (str): The exchange to find stocks from.
        retrieve_count (int): the number of stocks you want to retrieve

    Usage:
        retrieveStockList('NYSE', retrieve_count=20)

    Returns:
        returns a list of stocks as dictionary.

    TODO:   better error handling.
            double check url see if we can grab more useful info.

    '''
    retrieve_all = 1000
    url = "https://www.google.com/finance?output=json&start=0&amp&num="+str(retrieve_all)+"&noIL=1&q=[%28exchange%20%3D%3D%20%22"+exchange+"%22%29%20%26%20%28dividend_next_year%20%3E%3D%200%29%20%26%20%28dividend_next_year%20%3C%3D%201.46%29%20%26%20%28price_to_sales_trailing_12months%20%3C%3D%20850%29]&restype=company&ei=BjE7VZmkG8XwuASFn4CoDg"

    #download
    url_data = urllib.urlretrieve(url, testfile)
    #convert to dict. get json working if possible.
    f = open(testfile, 'r')
    texts = f.read()
    #print texts
    stock_text_dict = ast.literal_eval(texts)
    #pprint.pprint(texts_dict)

    search_result = stock_text_dict["searchresults"]
    result = []
    for i in range(1, retrieve_count):
        rand_pick = random.choice(search_result)
        stock_data = getQuote(rand_pick['ticker'])

        #if we got the data from google
        if stock_data:
            #append stock title.
            stock_data['title'] = rand_pick['title']
            #over ride exchange
            stock_data['exchange'] = rand_pick['exchange']
            result.append(stock_data)

    return result


def getQuote(ticker):
    '''use this function to get current market quote and the exchange the stock is listed.
    takes a stock ticker return a dictionary with the follwing data structure:

    Args:
        ticker (str): The ticker of the stock.

    Usage:
        getQuote('dis')

    Returns:
        returns a dictionary of data, False otherwise.

        {
            'id': '123456789'
            'quote': '106.65', 
            'ticker': 'XXX', 
            'exchange': 'NYSE',
            'title: 'The Company Name'
        }

    Note:
        this will sometime return the wrong exchange. use exchange data from retrieveStockList
        when possible.

    '''
    #threading.Timer(1.0, getquote).start()
    #target_url = "http://finance.google.com/finance/info?client=ig&q=" + ticker.lower()
    target_url = "http://www.google.com/finance/info?infotype=infoquoteall&q=" + ticker.lower()
    
    try:
        data = urllib2.urlopen(target_url)
    except:
        print "error getting stock quote from url: ", target_url
        return False

    data_dict = ast.literal_eval(data.read()[4:])[0]

    #pprint.pprint(data_dict)
    #timestamp = st = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
    #print  ticker + " --- " + timestamp + " --- " + data.readlines()[8].replace(',"l_cur" : ', "").replace('"',"")
    try:
        stock_quote_dict = dict(    id=data_dict["id"], 
                                    ticker=data_dict["t"], 
                                    exchange=data_dict["e"], 
                                    quote=data_dict["l"],
                                    title=data_dict["name"])

    except Exception, e:
        print "error getting stock quote from ticker: ", ticker
        print e
        return False
    #print stock_quote_dict
    return stock_quote_dict