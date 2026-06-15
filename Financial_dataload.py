import pandas as pd

INPUT_FILE = "transactions_data.csv"
OUTPUT_FILE = "transactions_2019.csv"

chunksize = 100_000

filtered_chunks = []

for chunk in pd.read_csv(
    INPUT_FILE,
    chunksize=chunksize,
    parse_dates=["date"]
):

    chunk_2019 = chunk[
        chunk["date"].dt.year == 2019
    ]

    filtered_chunks.append(chunk_2019)

transactions_2019 = pd.concat(
    filtered_chunks,
    ignore_index=True
)

transactions_2019.to_csv(
    OUTPUT_FILE,
    index=False
)

print(transactions_2019.shape)