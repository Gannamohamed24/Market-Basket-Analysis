import pandas as pd
from mlxtend.preprocessing import TransactionEncoder


# Group products into transactions using InvoiceNo
def create_transactions(df):

    print("\n========== TRANSACTION PREPARATION ==========")

    transactions = (
        df.groupby("InvoiceNo")["StockCode"]
        .apply(lambda products: sorted(set(products)))
        .tolist()
    )

    print("Total Transactions:", len(transactions))

    print("\nFirst 5 Transactions:")
    for i, transaction in enumerate(transactions[:5], start=1):
        print(f"Transaction {i}: {transaction}")

    return transactions


# Convert transactions into a Boolean pd.DataFrame
def encode_transactions(transactions):

    print("\n========== TRANSACTION ENCODING ==========")

    encoder = TransactionEncoder()

    encoded_array = encoder.fit(transactions).transform(transactions, sparse=True)

    encoded_df = pd.DataFrame.sparse.from_spmatrix(
        encoded_array, columns=encoder.columns_
    )

    print("Encoded Dataset Shape:", encoded_df.shape)

    print("\nFirst 5 Rows:")
    print(encoded_df.head())

    print("\nNumber of Products:", len(encoder.columns_))

    return encoded_df
