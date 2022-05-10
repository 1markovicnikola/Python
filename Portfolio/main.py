import pandas as pd
import nsepy as nse
def LTP(symbol_):
    market = nse.get_quote(symbol = symbol_)
    return float(market['data'][0]['lastPrice'].replace(',', ''))
df = pd.read_csv('portfolio.csv')
#print(df)
df['INVESTED'] = df['QUANTITY']*df['PRICE']
df
data = {}
TICKER = []
QUANTITY = []
PRICE = []
INVESTED = []
ticker_list = list(set(df['TICKER']))
for tkr in ticker_list:
    total_quantity = sum(list(df['QUANTITY'][df['TICKER'] == tkr]))
    price_tkr = round(sum(list(df['INVESTED'][df['TICKER'] == tkr])), 2)
    TICKER.append(tkr)
    QUANTITY.append(total_quantity)
    PRICE.append(round(price_tkr/total_quantity, 2))
    INVESTED.append(price_tkr)
lst = [TICKER, QUANTITY, PRICE, INVESTED]
cnt = 0
for x in df:
    data[x] = lst[cnt]
    cnt += 1
df2 = pd.DataFrame(data)
df2['CLOSINGPRICE'] = [LTP(i) for i in df2['TICKER']]
df2['PROFITLOSS'] = (df2['CLOSINGPRICE'] - df2['PRICE'])*(df2['QUANTITY'])
df2['PERCENTAGE'] = round((df2['CLOSINGPRICE']/df2['PRICE'] - 1)*100, 2)
df2 = sorted_df = df2.sort_values(by=['PERCENTAGE'], ascending=False)
#df2['PERCENTAGE'] = 
df2.loc['Total', 'INVESTED'] = df2['INVESTED'].sum()
df2.loc['Total', 'PROFITLOSS'] = round(df2['PROFITLOSS'].sum(), 2)
df2.loc['Total', 'PERCENTAGE'] = round(df2['PROFITLOSS'].sum()*100/df2['INVESTED'].sum(), 2)
print(df2)