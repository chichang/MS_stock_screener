from ms_data import MS_stockHandler
import gf_data
from globals import *


stock_exchange = "NYSE"
retrieve_num = 50
stocks = gf_data.retrieveStockList(stock_exchange, retrieve_num)

result_file = TEMP_DIR+"test_result.txt"
f = open(result_file, 'w')
result_str = " - Filtered result by MS_stock_screener - "


for stock in stocks:

    handler = MS_stockHandler(google_stock_dict_data = stock)

    print "analizing: ", handler.title.ljust(35), " ticker: ", handler.ticker
'''
    #if hander is initialized without error
    if handler.initialized:

        handler.parseBalanceSheet()
        handler.parseKeyRatios()

        latest_total_asset = handler.getFinancialData("balance_sheet", "2015", "Total assets")
        latest_current_ratio= handler.getFinancialData("key_ratios", "2015", "Current Ratio")
        latest_debt_equity = handler.getFinancialData("key_ratios", "2015", "Debt/Equity")

        if latest_debt_equity:
            latest_debt_equity = float(latest_debt_equity)
        if latest_current_ratio:
            latest_current_ratio = float(latest_current_ratio)

        #?? does None means no debt??? check.
        #if latest_debt_equity and latest_current_ratio:
        #if latest_debt_equity and latest_current_ratio:

        if latest_debt_equity < 0.5:
            if latest_current_ratio > 1.5:
                print "+----------------------------------------------------------"
                print "|    ",i
                print "+----------------------------------------------------------"
                print "|    Current Ratio: ", latest_current_ratio
                print "|    Debt/Equity: Ratio: ", latest_debt_equity
                print "+----------------------------------------------------------"
                print "\n"


                result_str += "+----------------------------------------------------------"+"\n"
                result_str += "|    "+i+"\n"
                result_str += "+----------------------------------------------------------"+"\n"
                result_str += "|    Current Ratio: "+ str(latest_current_ratio)+"\n"
                result_str += "|    Debt/Equity: Ratio: "+ str(latest_debt_equity)+"\n"
                result_str += "+----------------------------------------------------------"+"\n"
                result_str += "\n"+"\n"
    else:
        pass

f.write(result_str)
f.close()
'''