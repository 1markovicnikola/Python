from nsetools import Nse
import pandas as pd
market = Nse()
get_lu = market.get_top_gainers()
#get_lu = market.get_top_losers()
hedr = get_lu[0].keys()
d = {}
for ind, ele in enumerate(hedr):
    d[ele] = [get_lu[ro][ele] for ro in range(len(get_lu))]
bf = pd.DataFrame.from_dict(d)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(bf)
