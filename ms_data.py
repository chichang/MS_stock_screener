import sys
import os
import errno
import urllib
import urllib2
import logging
import time
import csv

import ms_parser

class MS_dataHandler:

    def __init__(self, ticker):
        '''Constructs the handler instance.

        useage:

        '''

        print "initial data handler for: ", ticker

        logging.info("initialize data from financials.morningstar.com  ticker: %s", ticker)

        #ticker
        self.ticker = ticker
        self.csv_urls = dict()
        self.csv_files = dict()
        
        #project dir.  TODO: use current working dir. hard code for dev now.
        self.temp_csv_dir = "/USERS/chichang/Documents/temp_csv/"+ticker.lower()
        #create the temp dir for csv files
        logging.debug("making directory for csv files: %s", self.temp_csv_dir)
        self.makeCsvTempDir()

        #statement type
        income_statement_str = "is"     #income statement
        balance_sheet_str = "bs"        #balance sheet
        cash_flow_str = "cf"            #cash flow statement

        #financials.morningstar.com urls
        key_ratios_url = self.getKeyRatiosURL()
        self.csv_urls["key_ratios"] = key_ratios_url
        logging.debug("key ratios url: %s", key_ratios_url)

        income_statement_url = self.getFinancialReportsURL(report_type=income_statement_str)
        self.csv_urls["income_statement"] = income_statement_url
        logging.debug("income statement url: %s", income_statement_url)

        balance_sheet_url = self.getFinancialReportsURL(report_type=balance_sheet_str)
        self.csv_urls["balance_sheet"] = balance_sheet_url
        logging.debug("balance sheet url: %s", balance_sheet_url)

        cash_flow_url = self.getFinancialReportsURL(report_type=cash_flow_str)
        self.csv_urls["cash_flow"] = cash_flow_url
        logging.debug("cash flow url: %s", cash_flow_url)


        print "requesting csv data : ", ticker


        result = self.retrieveCsv()
        if not result:
            logging.error("Error initializing data. skipping %s", self.ticker)
            return None


        #print self.csv_files

    def __str__(self):
        '''get basic info for the data.
        '''
        return str("MS_dataHandler for "+self.ticker)


    def getKeyRatiosURL(self):
        '''returns the url to the key ratios from financials.morningstar.com
        '''
        #key racio url
        kr_url1 = "http://financials.morningstar.com/ajax/exportKR2CSV.html?&callback=?&t="    #ticker gose here
        kr_url2 = "&region=sgp&culture=en-US&cur=&order=asc"
        return kr_url1 + self.ticker + kr_url2


    def getFinancialReportsURL(self, report_type):
        '''returns the url to financial reports from financials.morningstar.com
        '''
        #financial statements url
        fs_url1 = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t="    #ticker gose here
        fs_url2 = "&region=usa&culture=en-US&cur=USD&reportType="   #report type goes here
        fs_url3 = "&period=12&dataType=A&order=asc&columnYear=10&rounding=3&view=raw&r=337541&denominatorView=raw&number=3"
        return fs_url1 + self.ticker + fs_url2 + report_type + fs_url3


    def makeCsvTempDir(self):
        ''' Create temp dir to store csv files for current ticker
        $workingdir/temp_csv/(ticker)
        '''
        try:
            os.makedirs(self.temp_csv_dir)

        except OSError , e:
            if e.errno != errno.EEXIST:
                raise  # raises the error again

    def retrieveCsv(self):
        '''retrieve all csv files.
        return False if there is an error downloading files.
        '''
        for key in self.csv_urls:
            csv_file_name = "%s_%s.csv" % (self.ticker.lower(), key)
            csv_full_path = os.path.join(self.temp_csv_dir, csv_file_name)

            logging.debug("retrieving data : %s", csv_full_path)
            self.download(self.csv_urls[key], csv_full_path)

            #TODO: error check here by simply checking downloaded file size for now.
            if os.path.getsize(csv_full_path) > 0:
                self.csv_files[key] = csv_full_path
                continue
            else:
                logging.error("Error retrieving data for %s", self.ticker)
                return False
                break

        #all csv downloaded
        return True

    def download(self, url, dest):
        '''downlads file.
        TODO: better error handling here.
        '''
        try:
            #retrieve the url.
            urllib.urlretrieve(url, dest)
        except:
            pass


    def getData(self):
        '''this is the main function to aquire data from the handler.
        '''
        pass

    def validateCsv(self):
        '''check the csv file.
        '''
        pass


    def parseIncomeStatement(self):
        print "parsing and creating income statement data ..."
        ms_parser._parseIncomeStatement(self)

    def parseBalanceSheet(self):
        print "parsing and creating balance sheet data ..."
        ms_parser._parseBalanceSheet(self)

    def parseCashFlow(self):
        print "parsing and creating cash flow data ..."
        ms_parser._parseCashFlow(self)



    def getFinancialData(self, statement_type, key, item):

        if statement_type == "balance_sheet":
            if hasattr(self, 'parsed_bs_data'):
                #try get the data
                return self.parsed_bs_data[key][item]
                #except
            else:
                print "no parsed balance sheet data found. Please parse data. handler.parseBalanceSheet()"
                return False

        if statement_type == "income_statement":
            if hasattr(self, 'parsed_is_data'):
                return self.parsed_is_data[key][item]

            else:
                print "no parsed income statement data found. Please parse data. handler.parseIncomeStatement()"
                return False


        if statement_type == "cash_flow":
            if hasattr(self, 'parsed_cf_data'):
                return self.parsed_cf_data[key][item]

            else:
                print "no parsed cash flow data found. Please parse data. handler.parseCashFlow()"
                return False





#test run
#dwa_handler = MS_dataHandler(ticker="DWA")














'''

#urllib.urlretrieve(dataLink, temp_csv)

with open(temp_csv, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row):
            #print row[0]
            if row[0] == 'R&D':
                print "Net Income USD Mil: " + row[1]
        #print(row['first_name'], row['last_name'])


import json
import urllib
import pprint
from bs4 import BeautifulSoup


pp = pprint.PrettyPrinter(depth=6)
ticker="DWA"
report_type = "is"
#:param report_type: Type of the report ('is', 'bs', 'cf').
print 'http://financials.morningstar.com/ajax/ReportProcess4HtmlAjax.html?&t=' + ticker +'&region=usa&culture=en-US&cur=USD&reportType=' + report_type + '&period=12&dataType=A&order=asc&columnYear=5&rounding=3&view=raw'

url = (r'http://financials.morningstar.com/ajax/' +r'ReportProcess4HtmlAjax.html?&t=' + ticker +r'&region=usa&culture=en-US&cur=USD' +r'&reportType=' + report_type + r'&period=12' +r'&dataType=A&order=asc&columnYear=5&rounding=3&view=raw')
response = urllib.urlopen(url)
json_text = response.read().decode('utf-8')
json_data = json.loads(json_text)
print json_data
pp.pprint(json_data)

print json_data['result']


#result_soup = BeautifulSoup(json_data['result'], "html.parser")
result_soup = BeautifulSoup(json_data['result'], "html.parser")
print result_soup.find('div')

left = result_soup.find('div', 'left').div
print left

main = soup.find('div', 'main').find('div', 'rf_table')
print main






import sys
sys.path.append("/USERS/chichang/Downloads/python_dist/Python-2.7.11/Lib/site-packages")

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

'''

