from ms_data import MS_dataHandler










handler = MS_dataHandler(ticker="NFLX")
handler.parseBalanceSheet()
print handler.getFinancialData("balance_sheet", "2015-12", "Total liabilities")
print handler.getFinancialData("balance_sheet", "2015-12", "Total stockholders' equity")









latest_total_asset = handler.getFinancialData("balance_sheet", "2015-12", "Total assets")
latest_total_debt = handler.getFinancialData("balance_sheet", "2015-12", "Total liabilities")

#debt equity
print float(latest_total_debt)/(float(latest_total_asset)-float(latest_total_debt))
