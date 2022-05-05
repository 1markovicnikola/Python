import pandas as pd
import nsepy as nse



def LTP(symbol_):
    market = nse.get_quote(symbol = symbol_)
    return market['data'][0]['lastPrice']



df = pd.read_csv('../investment.csv')
lst = [LTP(ticker) for ticker in list(df['TICKER'])]
ltp_without_commas = [float(ltp.replace(',', '')) for ltp in lst]
df['LTP'] = ltp_without_commas
#df['INVESTED'] = [df['QUANTITY'][i]*df['BUYPRICE'][i] for i in range(len(df['TICKER']))]


df['INVESTED'] = df['QUANTITY']*df['BUYPRICE']

df['PERCENTAGE'] = (df['LTP']/df['BUYPRICE'] - 1)*100

df['PROFITLOSS'] = (df['LTP'] - df['BUYPRICE'])*(df['QUANTITY'])

df.loc['Total', 'INVESTED'] = df['INVESTED'].sum()
df.loc['Total', 'PROFITLOSS'] = df['PROFITLOSS'].sum()
df.loc['Total', 'PERCENTAGE'] = round(df['PROFITLOSS']*100/df['INVESTED'], 2)

print(df)
print('Total Investment:', df['INVESTED'].sum())
print('Profit & Loss:', round(df['PROFITLOSS'].sum(), 2))
print('Net Percentage:', round(df['PROFITLOSS'].sum()*100/df['INVESTED'].sum(), 2))
