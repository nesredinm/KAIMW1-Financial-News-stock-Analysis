import os
import pandas as pd

# Set the base folder path where all the files are stored
BASE_FOLDER = ".gitignore/data_folder"

def read_company_data(ticker):
    """
    Reads a company's stock price file based on its ticker symbol.

    Parameters:
        ticker (str): The stock ticker symbol (e.g., "AAPL", "MSFT").

    Returns:
        pd.DataFrame: DataFrame containing the stock price data for the given ticker.
    """
    # Construct the file path by appending '.csv' to the ticker
    file_path = os.path.join(BASE_FOLDER, f"{ticker}_historical_data.csv")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No data file found for ticker: {ticker} at {file_path}")
    
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data for {ticker}")
        return df
    except Exception as e:
        raise ValueError(f"Error reading data for {ticker}: {e}")

def read_multiple_companies(tickers):
    """
    Reads stock price files for multiple tickers and combines them into one DataFrame.

    Parameters:
        tickers (list of str): List of stock ticker symbols (e.g., ["AAPL", "MSFT"]).

    Returns:
        pd.DataFrame: Combined DataFrame containing data for all tickers.
    """
    combined_data = []
    
    for ticker in tickers:
        try:
            df = read_company_data(ticker)
            df['Company'] = ticker  # Add a column to identify the company
            combined_data.append(df)
        except Exception as e:
            print(f"Skipping {ticker} due to error: {e}")
    
    if not combined_data:
        raise ValueError("No valid data files could be read for the provided tickers.")
    
    combined_df = pd.concat(combined_data, ignore_index=True)
    print(f"Successfully combined data for {len(combined_data)} companies.")
    return combined_df
