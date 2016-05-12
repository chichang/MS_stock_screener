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
import math
from globals import *
from ms_data import MS_stockHandler
import gf_data
from charting import drawChart



#from exchange to get a "random" umber of stocks. TODO: put these as commandline args.
stock_exchange = "NYSE"
retrieve_num = 20

test_stocks = ["AXP","DIS","KO"]



#get the stock data
stocks_to_analyze = []
if test_stocks:
    for i in test_stocks:
        stocks_to_analyze.append(gf_data.getQuote(i))
else:
    stocks_to_analyze = gf_data.retrieveStockList(stock_exchange, retrieve_num)


#file to save the filtered restults.
result_file = TEMP_DIR+"test_result.txt"
f = open(result_file, 'w')
result_str = " - Filtered result by MS_stock_screener - \n"

#going through each stock aquired.
for stock in stocks_to_analyze:

    #create handler for the stock
    handler = MS_stockHandler(google_stock_dict_data = stock)
    print "analizing: ", handler.title.ljust(50), " ticker: ", handler.ticker

    #if hander is initialized without error
    if handler.initialized:

        #parse and initialize data before analize
        handler.parseBalanceSheet()
        handler.parseKeyRatios()

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

        #getting value for calculating intrinsit value
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

        #calculate intrinsit value
        avg_book_value_rate= (math.pow((float(current_book_value)/float(old_book_value)),(1.0/(years-1)))-1)*100
        #print avg_book_value_rate
        parr = float(current_book_value)*(math.pow((1+(avg_book_value_rate/100)),years))
        #print parr
        extra = math.pow((1+(treasure_rate)),years)
        #print extra
        intrinsic_value = float(current_dividend)*(1-(1/extra))/treasure_rate+parr/extra
        print "Intrinsic Value: ", intrinsic_value 


        #?? does None means no debt??? check.

        #perform some calcalations here ....
        if latest_debt_equity < 0.5:
            if latest_current_ratio > 1.5:
                print "+----------------------------------------------------------"
                print "|    ",handler.ticker
                print "+----------------------------------------------------------"
                print "|    Current Ratio: ", latest_current_ratio
                print "|    Debt/Equity: Ratio: ", latest_debt_equity
                print "|    Intrinsit Value: ", intrinsit_value
                print "+----------------------------------------------------------"
                print "\n"


                result_str += "+----------------------------------------------------------"+"\n"
                result_str += "|    "+handler.ticker+"\n"
                result_str += "+----------------------------------------------------------"+"\n"
                result_str += "|    Current Ratio: "+ str(latest_current_ratio)+"\n"
                result_str += "|    Debt/Equity: Ratio: "+ str(latest_debt_equity)+"\n"
                result_str += "|    Intrinsit Value: "+ str(intrinsit_value)+"\n"
                result_str += "+----------------------------------------------------------"+"\n"
                result_str += "\n"+"\n"

                #test charting
                drawChart(handler)
    else:
        pass

f.write(result_str)
f.close()


if __name__ == "__main__":
    pass