import pandas as pd
import nsepy as nse



def LTP(symbol_):
    market = nse.get_quote(symbol = symbol_)
    return market['data'][0]['lastPrice']


df = pd.read_csv('C:/Users/1954513/Desktop/StudioCodes/NSE_Stock/PortfolioHealth/investment.csv')
lst = [LTP(ticker) for ticker in list(df['TICKER'])]
ltp_without_commas = [float(ltp.replace(',', '')) for ltp in lst]
df['LTP'] = ltp_without_commas


#df['INVESTED'] = [df['QUANTITY'][i]*df['BUYPRICE'][i] for i in range(len(df['TICKER']))]


df['INVESTED'] = df['QUANTITY']*df['BUYPRICE']
df['PERCENTAGE'] = (df['LTP']/df['BUYPRICE'] - 1)*100
df['PROFITLOSS'] = (df['LTP'] - df['BUYPRICE'])*(df['QUANTITY'])
df.loc['Total', 'INVESTED'] = df['INVESTED'].sum()
df.loc['Total', 'PROFITLOSS'] = round(df['PROFITLOSS'].sum(), 2)
df.loc['Total', 'PERCENTAGE'] = round(df['PROFITLOSS'].sum()*100/df['INVESTED'].sum(), 2)
print(df)