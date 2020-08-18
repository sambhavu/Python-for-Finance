from yahoo_fin import stock_info as si
import pandas as pd
import xlsxwriter

stock = 'NVDA'

directory = "/users/satish/Desktop/" + stock + "_fundamentals.xlsx"
writer = pd.ExcelWriter(directory, engine= 'xlsxwriter')



balance_sheet = si.get_balance_sheet(stock, True)
income_statement = si.get_income_statement(stock, True)
cash_flow = si.get_cash_flow(stock, True)
financials = si.get_financials(stock, yearly = True)



balance_sheet.to_excel(writer, sheet_name = 'Balance Sheet')
income_statement.to_excel(writer, sheet_name = 'Income Statement')
cash_flow.to_excel(writer, sheet_name = 'Cash Flow')
#financials.to_excel(writer, sheet_name = 'Financials')

writer.save()


