import pandas as pd
import json

# Load JSON data from a local file
file_path = "OpenAPIScripMaster.json"  # Update with the actual file path if needed
with open(file_path, "r") as file:
    d = json.load(file)

# Convert JSON data to DataFrame
token_df = pd.DataFrame.from_dict(d)

# Convert 'expiry' column to date format (if applicable)
if 'expiry' in token_df.columns:
    token_df['expiry'] = pd.to_datetime(token_df['expiry'], errors='coerce').dt.date

# Get the Token id for HDFC Bank
print(token_df[token_df.symbol == 'NIFTY'])

# Get the Token id for Nifty Futures
print(token_df[token_df.symbol == 'HDFC'])
