
import pandas as pd

transaction_ids = set()

for chunk in pd.read_csv(
    "transactions_data.csv",
    usecols=["id"],
    chunksize=100_000
):
    transaction_ids.update(chunk["id"])

print("Unique transaction IDs:", len(transaction_ids))
