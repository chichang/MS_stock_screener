import math

#setup logger
import logging
from logger import setup_logging
logger = logging.getLogger(__name__)
setup_logging()

def bb_ivalue(handler, latestYear, rate):
    #getting value for calculating intrinsit value
    current_year = str(latestYear)
    years = 10
    old_year = str(int(current_year) - (years-1))
    current_book_value = handler.getFinancialData("key_ratios", current_year, "Book Value Per Share USD")
    old_book_value = handler.getFinancialData("key_ratios", old_year , "Book Value Per Share USD")
    current_dividend = handler.getFinancialData("key_ratios", "2015", "Dividends USD")
    treasure_rate = rate/100 
          
    #calculate intrinsit value
    if current_dividend == False:
        logger.warning("%s doesn't have dividend information.", handler.ticker)
    elif not old_book_value:
        logger.warning("%s doesn't have 2006 book value data.", handler.ticker)
    elif not current_book_value:
        logger.warning("%s doesn't have 2015 book value data.", handler.ticker)
    else:
        if current_dividend == None:
            logger.warning("%s doesn't issue dividend.", handler.ticker)
            current_dividend = 0.0
        try:
            avg_book_value_rate= (math.pow((float(current_book_value)/float(old_book_value)),(1.0/(years-1)))-1)*100
            parr = float(current_book_value)*(math.pow((1+(avg_book_value_rate/100)),years))
            extra = math.pow((1+(treasure_rate)),years)
            intrinsic_value = float(current_dividend)*(1-(1/extra))/treasure_rate+parr/extra
            return intrinsic_value

        except Exception, e:
            logger.error('Error calculate intrinsic value', exc_info=True)


def bb_dcf_ivalue(handler, latestYear, rate):
    current_year = str(latestYear)
    years = 10
    y = int(current_year)
    total_free_cash_flow = 0.0
    for i in range(0, years):
        free_cash_flow = handler.getFinancialData("key_ratios", str(y - i), "Free Cash Flow USD Mil")
        free_cash_flow = free_cash_flow.replace(",", ".")
        print float(free_cash_flow)
        total_free_cash_flow += float(free_cash_flow)

    print total_free_cash_flow
    print total_free_cash_flow/years