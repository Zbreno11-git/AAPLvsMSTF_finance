import pandas as pd
import plotly.express as px

#AAPL = Apple
#MSFT = Microsoft
""""
import yfinance as yf
    - Using yfinance to gather the data
df = yf.download(['AAPL', 'MSFT'], period='1y')

    - Putting in a CSV file so I can work with it offline
df.to_csv('aaplXmstf.csv', index=False)
"""
df = pd.read_csv('aaplXmstf.csv')

print(df.head())
print(df.info())
print(df.describe(include='all'))

    #Organizing the DataFrame for easier
hdr = pd.read_csv('aaplXmstf.csv', nrows=2, header=None)
df = pd.read_csv('aaplXmstf.csv', skiprows=2, header=None)
df.columns = pd.MultiIndex.from_arrays([hdr.iloc[0], hdr.iloc[1]])
df = df.stack(future_stack=True).reset_index()

    #Renaming the columns
df = df.rename(columns={'level_0': 'Date_idx', 1: 'Ticker'})
    #Making a longer DataFrame
df_melt = df.melt(id_vars=['Date_idx', 'Ticker'], var_name='attribute', value_name='value')

    #How the 'closing' values change during the year:
df_close = df_melt[df_melt['attribute'] == 'Close']
fig1 = px.line(df_close, x='Date_idx', y='value', color='Ticker', template='plotly_dark',
               title='CLOSE: the last traded price of each day.')
#fig1.show()
fig1.write_html('../closing_values_finance.html')

    #How the Volume values change during the year:
df_vol = df_melt[df_melt['attribute'] == 'Volume']
fig2 = px.bar(df_vol, x='Date_idx', y='value', color='Ticker', template='plotly_dark', barmode='group',
              title='VOLUME: how many shares were traded each day.')
#fig2.show()
fig2.write_html('../volume_changes_finance.html')


