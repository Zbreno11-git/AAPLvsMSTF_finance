# AAPLvsMSTF_finance

## Stock Data Analysis (AAPL vs MSFT)
This project analyzes historical stock data for Apple (AAPL) and Microsoft (MSFT) using Python. 
It demonstrates a complete data workflow: from data collection to transformation and visualization.
-
### Project Overview
The goal of this project is to:
Collect stock market data
Clean and restructure complex datasets
Perform exploratory data analysis (EDA)
Visualize trends in stock prices and trading volume

## Technologies Used
Python
Pandas
Plotly
(Optional) yFinance

### Data Collection
Stock data was originally collected using the yfinance library:
import yfinance as yfinance

## Data Cleaning & Transformation
The dataset comes with a multi-level column structure, which requires restructuring.

Steps performed:

Extract header rows separately
Rebuild a MultiIndex
Stack data into a long format
Use melt() to normalize the dataset
-
## Visualizations
1. Closing Price Over Time
Line chart comparing daily closing prices
Highlights trends and performance differences
- 
3. Trading Volume
Bar chart comparing daily trading volume
Shows market activity and liquidity
- 
## Final Conclusion
While both AAPL and MSFT demonstrate positive performance over the analyzed period, MSFT stands out for its more stable and consistent growth, whereas AAPL shows higher volatility, which may present more short-term trading opportunities but also greater risk.
