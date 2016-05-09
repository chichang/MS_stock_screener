import urllib
import pprint
import json
import ast

from globals import *

testfile = TEMP_DIR+"temp_gs_stock_list.txt"
import os
try:
    os.mkdir(TEMP_DIR)
except:
    pass

def retrieveStockList(exchange, retrieve_count=20):
    '''download a list of stocks from google finance api TODO: better error handling.
    '''
    url = "https://www.google.com/finance?output=json&start=0&amp&num="+str(retrieve_count)+"&noIL=1&q=[%28exchange%20%3D%3D%20%22"+exchange+"%22%29%20%26%20%28dividend_next_year%20%3E%3D%200%29%20%26%20%28dividend_next_year%20%3C%3D%201.46%29%20%26%20%28price_to_sales_trailing_12months%20%3C%3D%20850%29]&restype=company&ei=BjE7VZmkG8XwuASFn4CoDg"
    #download
    url_data = urllib.urlretrieve(url, testfile)
    #convert to dict. get json working if possible.
    f = open(testfile, 'r')
    texts = f.read()
    #print texts
    texts_dict = ast.literal_eval(texts)
    #pprint.pprint(texts_dict)
    return texts_dict["searchresults"]



#all_ticker = []
#for i in texts_dict:
    #current_stock = MS_stock(i)
    #print current_stock
    
    #all_ticker.append(i)
#print all_ticker