# todo set up github actions to recompute these monthly 

def get_data(asset_list=None):
    '''
    asset_list is a list of tickers, allowing this to be used with custom list 
    of assets.
    
    If none given, uses the default list of ETF assets picked by WSB team.
    '''
  
    import csv
    from datetime import datetime
    import numpy as np
    from dateutil.relativedelta import relativedelta
    import pandas_datareader as pdr
    import yfinance as yf

    from pypfopt import expected_returns, risk_models

    # get etf prices

    if not asset_list:
        with open('inputs/sp500_tickers.csv', newline='') as f:
            reader = csv.reader(f)
            asset_list = [l[0] for l in reader]
      
    #asset_list = ['SPY', 'IVV', 'VOO', 'SPLG', 'SPXL', 'SPXS', 'SPDN', 'SPUU', 'NSPI', 'SPXU', 'UPRO', 
    #             'SDS', 'SH', 'SSO','JMOM', 'VUG', 'VONV', 'IUSV', 'FREL', 'XSW', 'VHT', 'MGK', 'JVAL', 
    #             'VOT', 'VIOG', 'NURE', 'GLD', 'XLU', 'TQQQ', 'VCR', 'FNCL', 'IFRA',
    #            'PBD', 'RYT', 'FTEC', 'SCHI', 'SUSC', 'VTC', 'VCIT','VEA','IEFA','EFA',
    #             'SCHF','EFV','SCZ','SPDW','FNDF','EWC','DBEF','GSIE']

    start  = datetime.now() - relativedelta(years=10)
    end    = datetime.now() 

    asset_prices = yf.download(asset_list, start=start, end=end, progress=False)
    asset_prices = asset_prices.filter(like='Adj Close') # reduce to just columns with this in the name
    asset_prices.columns = asset_prices.columns.get_level_values(1)

    # drop assets with insufficient data (2 years, or 20% of request)
    
    valid_cols = asset_prices.isin([' ','NULL',np.nan]).mean() < .8
    asset_prices = asset_prices.loc[:, valid_cols]

    # get risk free rate

    risk_free_rate = pdr.DataReader("IRLTLT01USM156N", "fred", start,end)
    risk_free_rate = risk_free_rate.iloc[-1]/100
    risk_free_rate = risk_free_rate.item()

    # compute e_returns (capm with current rf), cov_mat

    e_returns = expected_returns.capm_return(asset_prices,risk_free_rate=risk_free_rate )#, span = 200)
    cov_mat   = risk_models.exp_cov(asset_prices)#,span=100)

    return e_returns, cov_mat, risk_free_rate
  
if __name__ == "__main__":

  e_returns, cov_mat, risk_free_rate = get_data()
  
  e_returns.to_csv('inputs/e_returns.csv')
  cov_mat.to_csv('inputs/cov_mat.csv')

  with open('inputs/risk_free_rate.txt', 'w') as f:
      f.write('%f' % risk_free_rate)


# def get_theme_assets(option, start_year, end_year, risk_level):
#     """
#     Returns a list of assets based on the selected theme and risk level.
#     """
#     stocks = pd.read_csv('sp500_stocks.csv')

#     if option == 'ESG Investing':
#         esg_scores = pd.read_csv('esg_scores.csv')
#         stocks = stocks.sort_values('Total-Score', ascending=False)
#         asset_list = stocks['Ticker'].tolist()[:100]
#     elif option == 'L,E,H,I,G,H':
#         asset_list = stocks[stocks['Ticker'].str.contains('L|E|H|I|G', case=False)]['Ticker'].tolist()
#    elif option == 'I like my beta low':
#     stocks = stocks[stocks['Beta'].notnull()]  # Exclude rows with missing 'Beta' values
#     stocks = stocks.sort_values('Beta', ascending=True)
#     asset_list = stocks['Symbol'].tolist()[:10]
#     elif option == 'I am not high, beta is':
#         stocks = stocks[stocks['Sector'] == 'Technology']
#         asset_list = stocks['Symbol'].tolist()
#     elif option == 'Highest Price per Shares':
#         stocks = stocks.sort_values('Price', ascending=False)
#         asset_list = stocks['Symbol'].tolist()[:10]
#     elif option == 'Sector':
#         stocks = stocks[stocks['Sector'].isin(selected_sectors)]
#         asset_list = stocks['Symbol'].tolist()

#     if risk_level == ':rainbow[Mild Risk]':
#         asset_list = asset_list[:20]
#     elif risk_level == ':rainbow[Moderate]':
#         asset_list = asset_list[:50]
#     elif risk_level == ':rainbow[Elevated Risk]':
#         asset_list = asset_list[:80]
#     elif risk_level == ':rainbow[Severe Risk]':
#         asset_list = asset_list[:100]
#     elif risk_level == ':rainbow[Extreme Risk]':
#         asset_list = asset_



