"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python screener.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

from time import gmtime, strftime
import math
from globals import *
from ms_data import MS_stockHandler
import gf_data
#import algo
from calculators import bb_ivalue
from calculators import bb_dcf_ivalue
from charting import drawChart


#setup logger
import logging
from logger import setup_logging
logger = logging.getLogger(__name__)
setup_logging()
Mastering Python for Finance
print "=================================================="
print   "Starting Stock Screener."
print "=================================================="

#from exchange to get a "random" number of stocks. TODO: put these as commandline args.
stock_exchange = "NYSE"
retrieve_num = 5
test_stocks = []#["AP"]

#get the stock indexes to screen.
stocks_to_analyze = []
if test_stocks:
    for i in test_stocks:
        gf_stock_data = gf_data.getQuote(i)
        if gf_stock_data:
            stocks_to_analyze.append(gf_stock_data)
else:
    stocks_to_analyze = gf_data.retrieveStockList(stock_exchange, retrieve_num)

logging.info("Filtering through " + str(len(stocks_to_analyze)) + " stocks. \n")

#setup file to save the filtered restults.
result_file = TEMP_DIR + "test_result.txt"
f = open(result_file, 'w')
result_str = "\n - Filtered result by MS_stock_screener - \n"
result_str += " - " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - \n"


#going through each stock aquired.
for stock in stocks_to_analyze:
    #initialize the stock handler
    handler = MS_stockHandler(google_stock_dict_data = stock)
    #if hander is initialized without error
    if handler.initialized:
        #parse and initialize data before analize
        handler.parseBalanceSheet()
        handler.parseKeyRatios()

        #calculate intrinsic value using buffettsbooks.com formula
        latest_year = 2016
        non_risk_rate = 1.77
    
        #buffet books intrinsic algo
        bb_intrinsic_value = bb_ivalue(handler,latest_year,non_risk_rate)
        #bb_ncf_intrinsic_value = bb_dcf_ivalue(handler,latest_year,non_risk_rate)
        

        #fits criteria? a class to handle criteria. and logic.
        #something like
        #   criteria = SearchCriteia(criteria="some_rule.txt")
        #   fits_criteria = criteria.fitsCriteria(handler)

        print "+----------------------------------------------------------"
        print "|    "+handler.title + "  ".ljust(20) + "ticker: "+handler.ticker
        print "|    Market Value: ", handler.quote
        print "+----------------------------------------------------------"
        print "|    Data Period: " + str(latest_year-9) + "-" + str(latest_year)
        print "|    Non-risk Rate (%):",non_risk_rate
        print "|    (Buffettsbooks.com Formula)"
        print "|    Intrinsit Value: ", bb_intrinsic_value
        #print "|    NCF Intrinsit Value: ", bb_ncf_intrinsic_value
        print "+----------------------------------------------------------"
        print "\n"

        if bb_intrinsic_value and float(bb_intrinsic_value) > float(handler.quote):
            result_str +=  "+----------------------------------------------------------" +"\n"
            result_str +=   "|    "+handler.title + "  ".ljust(20) + "ticker: "+ handler.ticker +"\n"
            result_str +=   "|    Market Value: " + str(handler.quote) +"\n"
            result_str +=   "+----------------------------------------------------------" +"\n"
            result_str +=   "|    Data Period: " + str(latest_year-9) + "-" + str(latest_year) +"\n"
            result_str +=   "|    Non-risk Rate (%):"+ str(non_risk_rate) +"\n"
            result_str +=   "|    (Buffettsbooks.com Formula)" +"\n"
            result_str +=   "|    Intrinsit Value: " + str(bb_intrinsic_value) +"\n"
            #print "|    NCF Intrinsit Value: ", bb_ncf_intrinsic_value
            result_str +=   "+----------------------------------------------------------" +"\n"
            result_str +=   "\n"
            #test charting
            #drawChart(handler)


    """
        #get the numbers for calcalation.
        latest_current_ratio= handler.getFinancialData("key_ratios", "2015", "Current Ratio")
        latest_debt_equity = handler.getFinancialData("key_ratios", "2015", "Debt/Equity")
        #TODO: wrap this check into the get data function.
        if latest_debt_equity:
            latest_debt_equity = float(latest_debt_equity)
        if latest_current_ratio:
            latest_current_ratio = float(latest_current_ratio)

        # test getting some values
        latest_total_asset = handler.getFinancialData("balance_sheet", "2015", "Total assets")
        book_value_ps = handler.getFinancialData("key_ratios", "2015", "Book Value Per Share USD")
        dividen = handler.getFinancialData("key_ratios", "2015", "Dividends USD")
        erngins_ps = handler.getFinancialData("key_ratios", "2015", "Earnings Per Share USD")
        print "Total assets".ljust(50) ,latest_total_asset
        print "Book Value Per Share USD".ljust(50), book_value_ps
        print "Dividends USD".ljust(50), dividen
        print "Earnings Per Share USD".ljust(50),erngins_ps
        print "Current market quote: ".ljust(50),stock["quote"]    #get this into the handler

        #getting value for calculating intrinsic value
        current_year = "2015"
        years = 10
        old_year = str(int(current_year) - (years-1))
        current_book_value = handler.getFinancialData("key_ratios", current_year, "Book Value Per Share USD")
        old_book_value = handler.getFinancialData("key_ratios", old_year , "Book Value Per Share USD")
        current_dividend = handler.getFinancialData("key_ratios", "2015", "Dividends USD")
        treasure_rate = 1.77/100
        #print current_dividend
        #print current_book_value
        #print old_book_value
        try:
            #calculate intrinsic value
            avg_book_value_rate= (math.pow((float(current_book_value)/float(old_book_value)),(1.0/(years-1)))-1)*100
            #print avg_book_value_rate
            parr = float(current_book_value)*(math.pow((1+(avg_book_value_rate/100)),years))
            #print parr
            extra = math.pow((1+(treasure_rate)),years)
            #print extra
            intrinsic_value = float(current_dividend)*(1-(1/extra))/treasure_rate+parr/extra
            print "Intrinsic Value: ".ljust(50), intrinsic_value
        except:
            intrinsic_value = "None"
            print "Intrinsic Value: ".ljust(50), None 

        #?? does None means no debt??? check.
        #perform some calcalations here ....
        if latest_debt_equity < 0.5:
            if latest_current_ratio > 1.5:
                print "+----------------------------------------------------------"
                print "|    ",handler.ticker
                print "+----------------------------------------------------------"
                print "|    Current Ratio: ", latest_current_ratio
                print "|    Debt/Equity: Ratio: ", latest_debt_equity
                print "|    Intrinsit Value: ", intrinsic_value
                print "+----------------------------------------------------------"
                print "\n"

                result_str += "+----------------------------------------------------------"+"\n"
                result_str += "|    "+handler.ticker+"\n"
                result_str += "+----------------------------------------------------------"+"\n"
                result_str += "|    Current Ratio: "+ str(latest_current_ratio)+"\n"
                result_str += "|    Debt/Equity: Ratio: "+ str(latest_debt_equity)+"\n"
                result_str += "|    Intrinsit Value: "+ str(intrinsic_value)+"\n"
                result_str += "+----------------------------------------------------------"+"\n"
                result_str += "\n"+"\n"

                #test charting
                drawChart(handler)
    else:
        pass
    """

f.write(result_str)
f.close()


if __name__ == "__main__":
    pass
