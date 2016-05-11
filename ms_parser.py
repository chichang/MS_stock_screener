'''parsers takes MS_dataHandler as argument and parse the csvs' to
    initialize data for the handler.
'''

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
    #print "parsing balance sheet for: ", data_handler.ticker

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

                        #data_handler.parsed_bs_data[year_key] = dict()
                        year = year_key.split("-")[0]
                        data_handler.parsed_bs_data[year] = dict()
                        data_handler.parsed_bs_data[year]["Year"] = year_key.split("-")[0]
                        data_handler.parsed_bs_data[year]["Month"] = year_key.split("-")[1]

                    else:    #fill here
                        
                        if idx_col == 0:
                            continue

                        data_key = row[KEY_COLUMN]
                        item_data = data[idx_row][idx_col]

                        if item_data == '' :
                            item_data = None
                        
                        #fill the data
                        year_key = data[YEAR_MONTH_ROW][idx_col]
                        year = year_key.split("-")[0]

                        data_handler.parsed_bs_data[year][data_key]=item_data

                        #data_handler.parsed_bs_data[data[YEAR_MONTH_ROW][idx_col]][data_key]=item_data
                        #data[YEAR_MONTH_ROW][idx_col]
                        #print data_key, "date:", data[YEAR_MONTH_ROW][idx_col], "value: ", data[idx_row][idx_col]



    #pprint.pprint(parsed_bs_data)






def _parseKeyRatios(data_handler, statement_type = "annual", period = 11):    #need to pay for 10 years data.
    '''parsed data structure:

 '2015-12': {'': '2015-12',                                                                                                                                                          
             '10-Year Average': '',                                                                                                                                                  
             '3-Year Average': '',                                                                                                                                                   
             '5-Year Average': '',                                                                                                                                                   
             'Accounts Payable': '0.55',                                                                                                                                             
             'Accounts Receivable': '25.48',                                                                                                                                         
             'Accrued Liabilities': '9.61',                                                                                                                                          
             'Asset Turnover': '0.47',                                                                                                                                               
             'Asset Turnover (Average)': '0.47',                                                                                                                                     
             'Balance Sheet Items (in %)': '2015-12',                                                                                                                                
             'Book Value Per Share MXN': '217.08',                                                                                                                                   
             'COGS': '57.46',                                                                                                                                                        
             'Cap Ex as a % of Sales': '2.48',                                                                                                                                       
             'Cap Spending USD Mil': '-23',                                                                                                                                          
             'Cash & Short-Term Investments': '5.63',                                                                                                                                
             'Cash Conversion Cycle': '650.80',                                                                                                                                      
             'Cash Flow Ratios': '2015-12',                                                                                                                                          
             'Current Ratio': '3.72',                                                                                                                                                
             'Days Inventory': '571.60',                                                                                                                                             
             'Days Sales Outstanding': '86.09',                                                                                                                                      
             'Debt/Equity': '0.31',                                                                                                                                                  
             'Dividends USD': '',                                                                                                                                                    
             'EBT Margin': '-5.43',                                                                                                                                                  
             'Earnings Per Share USD': '-0.64',                                                                                                                                      
             'Efficiency': '2015-12',                                                                                                                                                
             'Financial Leverage': '1.72',                                                                                                                                           
             'Financial Leverage (Average)': '1.72',                                                                                                                                 
             'Fixed Assets Turnover': '8.39',                                                                                                                                        
             'Free Cash Flow Growth % YOY': '',                                                                                                                                      
             'Free Cash Flow Per Share MXN': '-9.91',                                                                                                                                
             'Free Cash Flow USD Mil': '30',                                                                                                                                         
             'Free Cash Flow/Net Income': '-0.54',                                                                                                                                   
             'Free Cash Flow/Sales %': '3.25',                                                                                                                                       
             'Gross Margin': '42.54',                                                                                                                                                
             'Gross Margin %': '42.5',                                                                                                                                               
             'Intangibles': '18.43',                                                                                                                                                 
             'Interest Coverage': '',                                                                                                                                                
             'Inventory': '41.65',                                                                                                                                                   
             'Inventory Turnover': '0.64',                                                                                                                                           
             'Liquidity/Financial Health': '2015-12',                                                                                                                                
             'Long-Term Debt': '18.27',                                                                                                                                              
             'Margins % of Sales': '2015-12',                                                                                                                                        
             'Month': '12',                                                                                                                                                          
             'Net Income USD Mil': '-55',                                                                                                                                            
             'Net Int Inc & Other': '-7.22',                                                                                                                                         
             'Net Margin %': '-5.98',                                                                                                                                                
             'Net PP&E': '1.92',                                                                                                                                                     
             'Operating Cash Flow Growth % YOY': '',                                                                                                                                 
             'Operating Cash Flow USD Mil': '53',                                                                                                                                    
             'Operating Income USD Mil': '16',                                                                                                                                       
             'Operating Margin': '1.79',                                                                                                                                             
             'Operating Margin %': '1.8',                                                                                                                                            
             'Other': '-0.86',                                                                                                                                                       
             'Other Current Assets': '1.48',                                                                                                                                         
             'Other Long-Term Assets': '5.42',                                                                                                                                       
             'Other Long-Term Liabilities': '3.71',                                                                                                                                  
             'Other Short-Term Liabilities': '9.81',                                                                                                                                 
             'Payables Period': '6.89',                                                                                                                                              
             'Payout Ratio %': '',                                                                                                                                                   
             'Profitability': '2015-12',                                                                                                                                             
             'Quick Ratio': '1.56',                                                                                                                                                  
             'R&D': '0.51',                                                                                                                                                          
             'Receivables Turnover': '4.24',                                                                                                                                         
             'Return on Assets %': '-2.78',                                                                                                                                          
             'Return on Equity %': '-4.77',                                                                                                                                          
             'Return on Invested Capital %': '-3.45',                                                                                                                                
             'Revenue': '100.00',                                                                                                                                                    
             'Revenue USD Mil': '916',                                                                                                                                               
             'SG&A': '41.10',                                                                                                                                                        
             'Shares Mil': '86',                                                                                                                                                     
             'Short-Term Debt': '',                                                                                                                                                  
             'Tax Rate %': '',                                                                                                                                                       
             'Taxes Payable': '',                                                                                                                                                    
             'Total Assets': '100.00',                                                                                                                                               
             'Total Current Assets': '74.24',                                                                                                                                        
             'Total Current Liabilities': '19.97',                                                                                                                                   
             'Total Liabilities': '41.95',                                                                                                                                           
             'Total Liabilities & Equity': '100.00',                                                                                                                                 
             "Total Stockholders' Equity": '58.05',                                                                                                                                  
             'Working Capital USD Mil': '1,069',                                                                                                                                     
             'Year': '2015',                                                                                                                                                         
             'Year over Year': ''}, 

    '''
    #print "parsing key ratios for: ", data_handler.ticker

    csv_file = data_handler.csv_files["key_ratios"]

    row_len_with_data= period + 1

    YEAR_MONTH_ROW = 2
    KEY_COLUMN = 0
    
    data_handler.parsed_kr_data = dict()
    
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

                        #data_handler.parsed_bs_data[year_key] = dict()
                        year = year_key.split("-")[0]
                        data_handler.parsed_kr_data[year] = dict()


                        if year_key == "TTM":
                            data_handler.parsed_kr_data[year]["Year"] = "TTM"

                        else:
                            data_handler.parsed_kr_data[year]["Year"] = year_key.split("-")[0]
                            data_handler.parsed_kr_data[year]["Month"] = year_key.split("-")[1]

                    else:    #fill here
                        
                        if idx_col == 0:
                            continue

                        data_key = row[KEY_COLUMN]
                        item_data = data[idx_row][idx_col]

                        if item_data == '' :
                            item_data = None

                        #fill the data

                        year_key = data[YEAR_MONTH_ROW][idx_col]
                        year = year_key.split("-")[0]

                        data_handler.parsed_kr_data[year][data_key]=item_data


                        #data_handler.parsed_kr_data[data[YEAR_MONTH_ROW][idx_col]][data_key]=item_data
                        #data[YEAR_MONTH_ROW][idx_col]
                        #print data_key, "date:", data[YEAR_MONTH_ROW][idx_col], "value: ", data[idx_row][idx_col]
    #print data_handler.parsed_kr_data.keys()
    #pprint.pprint(data_handler.parsed_kr_data)
