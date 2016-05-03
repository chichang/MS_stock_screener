import urllib2
import urllib
import time
import csv


ticker="DWA"
temp_csv = "/USERS/chichang/Documents/temp_csv/dwa/dwa_balance_sheet.csv"


YEAR_MONTH_ROW = 3

class MS_dataParser:
	def __init__(self):
		pass


def _parseBalanceSheet(statement_type = "annual", period = 5):    #need to pay for 10 years data.
	'''parse balance sheet csv.
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
	print "parsing data......."





    row_len_with_data= period + 1
    YEAR_MONTH_ROW = 1
    
    parsed_data = dict()
    
    with open(temp_csv, 'rb') as csvfile:
        
        reader = csv.reader(csvfile)
        data = list(reader)
        
        year_month = data[YEAR_MONTH_ROW]

       #store year and month

        
        print year_month
        for i in range(len(year_month)):
            parsed_data[str(year_month[i])] = dict()

        print parsed_data
        
        #for row in data:
            #if len(row):
                #print row
                #print len(row)

_parseBalanceSheet()
        