import pandas as pd
from pathlib import Path

# Get the project folder path
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Define the Excel file path
DATA_PATH = PROJECT_DIR / "data" / "Online Retail.xlsx"


def load_data():

    print("\n========== LOADING DATA ==========")

    df = pd.read_excel(DATA_PATH)

    print("Dataset loaded successfully!")
    return df


def explore_data(df):

    print("\n========== DATASET OVERVIEW ==========")

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns)

    print("\nDataset Information:")
    df.info()

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nNumber of Duplicate Rows:")
    print(df.duplicated().sum())

    print("\nNumber of Unique Invoices:")
    print(df["InvoiceNo"].nunique())

    print("\nNumber of Unique Products:")
    print(df["StockCode"].nunique())

    print("\nNumber of Unique Customers:")
    print(df["CustomerID"].nunique())

    print("\nCancelled Invoices:")
    print(df["InvoiceNo"].astype(str).str.startswith("C").sum())

    print("\nNegative Quantities:")
    print((df["Quantity"] < 0).sum())

    print("\nZero Quantities:")
    print((df["Quantity"] == 0).sum())

    print("\nNon-positive Unit Prices:")
    print((df["UnitPrice"] <= 0).sum())

    print("\nMissing Descriptions:")
    print(df["Description"].isnull().sum())


# understand product distribution and identify non-numeric stock codes
def inspect_products(df):

    print("\n========== PRODUCT INSPECTION ==========")

    print("\nTop 20 Products:")

    print(df["Description"].value_counts().head(20))

    # Inspect all non-numeric stock codes
    print("\nAll Non-numeric Stock Codes:")

    non_numeric = df[~df["StockCode"].astype(str).str.isnumeric()]

    non_numeric_products = (
        non_numeric.groupby(["StockCode", "Description"])
        .size()
        .reset_index(name="Frequency")
        .sort_values("Frequency", ascending=False)
    )

    print(non_numeric_products.to_string(index=False))

    # Unique products
    print("\nUnique Stock Codes:")
    print(df["StockCode"].nunique())

    print("\nUnique Product Descriptions:")
    print(df["Description"].nunique())
