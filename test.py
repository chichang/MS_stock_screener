from ms_data import MS_dataHandler

#list of stocks for test
#stocks = ["DWA"]

'''
#import json
import urllib
import simplejson as json
import pprint

import ast

exchange="NYSE"
retrieve_count = "5"

testfile = "/USERS/chichang/Downloads/e.txt"
url = "https://www.google.com/finance?output=json&start=0&amp;num=3&noIL=1&q=[%28exchange%20%3D%3D%20%22"+exchange+"%22%29%20%26%20%28dividend_next_year%20%3E%3D%200%29%20%26%20%28dividend_next_year%20%3C%3D%201.46%29%20%26%20%28price_to_sales_trailing_12months%20%3C%3D%20850%29]&restype=company&ei=BjE7VZmkG8XwuASFn4CoDg"

url_data = urllib.urlretrieve(url, testfile)


f = open(testfile, 'r')
texts = f.read()
print texts
texts_dict = ast.literal_eval(texts)
print texts_dict


all_ticker = []
for i in texts_dict["searchresults"]:
    all_ticker.append(i["ticker"])
print all_ticker
'''
stock = ["ACN"]
stocks = ["NFLX", "TESTING", "C", "DWA", "KO", "FLY"]

sp500_2015_10 = [
    'A', 'AA', 'AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACE', 'ACN', 'ADBE',
    'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'ADT', 'AEE', 'AEP', 'AES', 'AET',
    'AFL', 'AGN', 'AIG', 'AIV', 'AIZ', 'AKAM', 'ALL', 'ALLE', 'ALTR', 'ALXN',
    'AMAT', 'AME', 'AMG', 'AMGN', 'AMP', 'AMT', 'AMZN', 'AN', 'ANTM', 'AON',
    'APA', 'APC', 'APD', 'APH', 'ARG', 'ATVI', 'AVB', 'AVGO', 'AVY', 'AXP',
    'AZO', 'BA', 'BAC', 'BAX', 'BBBY', 'BBT', 'BBY', 'BCR', 'BDX', 'BEN',
    'BF.B', 'BHI', 'BIIB', 'BK', 'BLK', 'BLL', 'BMY', 'BRCM', 'BRK.B', 'BSX',
    'BWA', 'BXLT', 'BXP', 'C', 'CA', 'CAG', 'CAH', 'CAM', 'CAT', 'CB', 'CBG',
    'CBS', 'CCE', 'CCI', 'CCL', 'CELG', 'CERN', 'CF', 'CHK', 'CHRW', 'CI',
    'CINF', 'CL', 'CLX', 'CMA', 'CMCSA', 'CMCSK', 'CME', 'CMG', 'CMI', 'CMS',
    'CNP', 'CNX', 'COF', 'COG', 'COH', 'COL', 'COP', 'COST', 'CPB', 'CPGX',
    'CRM', 'CSC', 'CSCO', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVC', 'CVS',
    'CVX', 'D', 'DAL', 'DD', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DIS',
    'DISCA', 'DISCK', 'DLPH', 'DLTR', 'DNB', 'DO', 'DOV', 'DOW', 'DPS', 'DRI',
    'DTE', 'DUK', 'DVA', 'DVN', 'EA', 'EBAY', 'ECL', 'ED', 'EFX', 'EIX', 'EL',
    'EMC', 'EMN', 'EMR', 'ENDP', 'EOG', 'EQIX', 'EQR', 'EQT', 'ES', 'ESRX',
    'ESS', 'ESV', 'ETFC', 'ETN', 'ETR', 'EW', 'EXC', 'EXPD', 'EXPE', 'F',
    'FAST', 'FB', 'FCX', 'FDX', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLIR',
    'FLR', 'FLS', 'FMC', 'FOSL', 'FOX', 'FOXA', 'FSLR', 'FTI', 'FTR', 'GAS',
    'GD', 'GE', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GMCR', 'GME', 'GNW', 'GOOG',
    'GOOGL', 'GPC', 'GPS', 'GRMN', 'GS', 'GT', 'GWW', 'HAL', 'HAR', 'HAS',
    'HBAN', 'HBI', 'HCA', 'HCBK', 'HCN', 'HCP', 'HD', 'HES', 'HIG', 'HOG',
    'HON', 'HOT', 'HP', 'HPQ', 'HRB', 'HRL', 'HRS', 'HSIC', 'HST', 'HSY', 'HUM',
    'IBM', 'ICE', 'IFF', 'INTC', 'INTU', 'IP', 'IPG', 'IR', 'IRM', 'ISRG',
    'ITW', 'IVZ', 'JBHT', 'JCI', 'JEC', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KEY',
    'KHC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KO', 'KORS', 'KR', 'KSS', 'KSU',
    'L', 'LB', 'LEG', 'LEN', 'LH', 'LLL', 'LLTC', 'LLY', 'LM', 'LMT', 'LNC',
    'LOW', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MA', 'MAC', 'MAR', 'MAS',
    'MAT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDLZ', 'MDT', 'MET', 'MHFI', 'MHK',
    'MJN', 'MKC', 'MLM', 'MMC', 'MMM', 'MNK', 'MNST', 'MO', 'MON', 'MOS', 'MPC',
    'MRK', 'MRO', 'MS', 'MSFT', 'MSI', 'MTB', 'MU', 'MUR', 'MYL', 'NAVI', 'NBL',
    'NDAQ', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NKE', 'NLSN', 'NOC', 'NOV',
    'NRG', 'NSC', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWS', 'NWSA', 'O',
    'OI', 'OKE', 'OMC', 'ORCL', 'ORLY', 'OXY', 'PAYX', 'PBCT', 'PBI', 'PCAR',
    'PCG', 'PCL', 'PCLN', 'PCP', 'PDCO', 'PEG', 'PEP', 'PFE', 'PFG', 'PG',
    'PGR', 'PH', 'PHM', 'PKI', 'PLD', 'PM', 'PNC', 'PNR', 'PNW', 'POM', 'PPG',
    'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'PYPL',
    'QCOM', 'QRVO', 'R', 'RAI', 'RCL', 'REGN', 'RF', 'RHI', 'RHT', 'RIG', 'RL',
    'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'RTN', 'SBUX', 'SCG', 'SCHW', 'SE',
    'SEE', 'SHW', 'SIAL', 'SIG', 'SJM', 'SLB', 'SLG', 'SNA', 'SNDK', 'SNI',
    'SO', 'SPG', 'SPLS', 'SRCL', 'SRE', 'STI', 'STJ', 'STT', 'STX', 'STZ',
    'SWK', 'SWKS', 'SWN', 'SYK', 'SYMC', 'SYY', 'T', 'TAP', 'TDC', 'TE', 'TEL',
    'TGNA', 'TGT', 'THC', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV',
    'TSCO', 'TSN', 'TSO', 'TSS', 'TWC', 'TWX', 'TXN', 'TXT', 'TYC', 'UA', 'UAL',
    'UHS', 'UNH', 'UNM', 'UNP', 'UPS', 'URBN', 'URI', 'USB', 'UTX', 'V', 'VAR',
    'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSK', 'VRSN', 'VRTX', 'VTR', 'VZ',
    'WAT', 'WBA', 'WDC', 'WEC', 'WFC', 'WFM', 'WHR', 'WM', 'WMB', 'WMT', 'WRK',
    'WU', 'WY', 'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XOM', 'XRAY', 'XRX',
    'XYL', 'YHOO', 'YUM', 'ZBH', 'ZION', 'ZTS']



for i in sp500_2015_10:

	handler = MS_dataHandler(ticker = i)

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
		if latest_debt_equity < 0.5:
			if latest_current_ratio > 1.5:
				print "+----------------------------------------------------------"
				print "|	",i
				print "+----------------------------------------------------------"
				print "|	Current Ratio: ", latest_current_ratio
				print "|	Debt/Equity: Ratio: ", latest_debt_equity
				print "+----------------------------------------------------------"
				print "\n"

	else:
		pass