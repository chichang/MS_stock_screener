
import urllib2
import urllib
import time
import csv
import pprint

ticker="DWA" #78096  2412.034008
temp_csv = "/USERS/chichang/Documents/temp_csv/dwa/dwa_balance_sheet.csv"


YEAR_MONTH_ROW = 3

class MS_dataParser:
    def __init__(self, data_handler):
        pass



    '''
    parse balance sheet csv.
    this parser is based on the following csv data structure from http://financials.morningstar.com
    balance sheet raw data structure:

    \---Assets
    |   +---Current assets
    |   |    |
    |   |    +---Cash
    |   |    |    +---Cash and cash equivalents
    |   |    |    +---Total cash
    |   |    |
    |   |    +---Receivables
    |   |    +---Inventories
    |   |    +---Prepaid expenses
    |   |    +---Other current assets
    |   |    +---Total current assets
    |   |
    |   +---Non-current assets
    |   |    |
    |   |    +---Property, plant and equipment
    |   |    |    +---Gross property, plant and equipment
    |   |    |    +---Accumulated Depreciation
    |   |    |    +---Net property, plant and equipment
    |   |    |
    |   |    +---Equity and other investments
    |   |    +---Goodwill
    |   |    +---Intangible assets
    |   |    +---Deferred income taxes
    |   |    +---Other long-term assets
    |   |    +---Total non-current assets
    |   |
    |   +---Total assets
    |
    \---Liabilities and stockholders' equity
    |   +---Liabilities
    |   |    |
    |   |    +---Current liabilities
    |   |    |    +---Accounts payable
    |   |    |    +---Accrued liabilities
    |   |    |    +---Deferred revenues
    |   |    |    +---Other current liabilities
    |   |    |    +---Total current liabilities
    |   |    |
    |   |    +---Non-current liabilities
    |   |    |    +---Long-term debt
    |   |    |    +---Minority interest
    |   |    |    +---Other long-term liabilities
    |   |    |    +---Total non-current liabilities
    |   |    |
    |   |    +---Total liabilities
    |   |
    |   +---Stockholders' equity
    |   |    |
    |   |    +---Common stock
    |   |    +---Additional paid-in capital
    |   |    +---Retained earnings
    |   |    +---Treasury stock
    |   |    +---Accumulated other comprehensive income
    |   |    +---Total stockholders' equity
    |   |
    |   +---Total liabilities and stockholders' equity
    +

    '''


def _parseBalanceSheet(data_handler, statement_type = "annual", period = 5):    #need to pay for 10 years data.
    '''parsed data structure:

    {'2011-12': {'Accounts payable': '3',
                 'Accrued liabilities': '99',
                 'Accumulated Depreciation': '-125',
                .....
    }

    '''
    print "parsing balance sheet for: ", data_handler.ticker

    csv_file = data_handler.csv_files["balance_sheet"]

    row_len_with_data= period + 1
    YEAR_MONTH_ROW = 1
    KEY_COLUMN = 0
    
    data_handler.parsed_bs_data = dict()
    
    with open(csv_file, 'rb') as csvfile:
        
        #read the csv file
        reader = csv.reader(csvfile)
        data = list(reader)

        for idx_row, row in enumerate(data):

            for idx_col, item in enumerate(row):
            
                # hard coded here. we only care about row with data.
                if len(row) == row_len_with_data:
    
                    if idx_row == YEAR_MONTH_ROW:  #this is the row where date is
                        
                        #skip
                        if idx_col == 0:
                            continue

                        #the year and month will be used as key.
                        year_key = row[idx_col]
                        
                        #print "getting data for year: ", year_key

                        data_handler.parsed_bs_data[year_key] = dict()
                        data_handler.parsed_bs_data[year_key]["Year"] = year_key.split("-")[0]
                        data_handler.parsed_bs_data[year_key]["Month"] = year_key.split("-")[1]

                    else:    #fill here
                        
                        if idx_col == 0:
                            continue

                        data_key = row[KEY_COLUMN]
                        
                        #fill the data
                        data_handler.parsed_bs_data[data[YEAR_MONTH_ROW][idx_col]][data_key]=data[idx_row][idx_col]
                        #data[YEAR_MONTH_ROW][idx_col]
                        #print data_key, "date:", data[YEAR_MONTH_ROW][idx_col], "value: ", data[idx_row][idx_col]



    #pprint.pprint(parsed_bs_data)
