import math

def bb_ivalue(handler,latestYear,rate):
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
        print "This stock doesn't have dividend information."
    elif not old_book_value:
        print "This stock doesn't have 2006 book value data."
    elif not current_book_value:
        print "This stock doesn't have 2015 book value data."
    else:
        if current_dividend == None:
            print "This stock doesn't issue dividend."
            current_dividend = 0.0
        try:
            avg_book_value_rate= (math.pow((float(current_book_value)/float(old_book_value)),(1.0/(years-1)))-1)*100
            parr = float(current_book_value)*(math.pow((1+(avg_book_value_rate/100)),years))
            extra = math.pow((1+(treasure_rate)),years)
            intrinsic_value = float(current_dividend)*(1-(1/extra))/treasure_rate+parr/extra
            return intrinsic_value
        except Exception, e:
            print "Error calculate intrinsic value: ", e
    


    
    