def clean_data(df):

    print("\n========== DATA CLEANING ==========")

    # Remove duplicate rows
    initial_rows = len(df)

    df = df.drop_duplicates()

    print("\nRemoved Duplicates:", initial_rows - len(df))

    # Remove cancelled invoices
    cancelled_invoices = df["InvoiceNo"].astype(str).str.startswith("C")

    cancelled_count = cancelled_invoices.sum()

    df = df[~cancelled_invoices]

    print("Removed Cancelled Invoices:", cancelled_count)

    # Remove negative quantities
    invalid_quantities = df["Quantity"] <= 0

    negative_count = invalid_quantities.sum()

    df = df[~invalid_quantities]

    print("Removed Negative Quantities:", negative_count)

    # Remove non-positive prices
    invalid_prices = df["UnitPrice"] <= 0

    price_count = invalid_prices.sum()

    df = df[~invalid_prices]

    print("Removed Non-positive Prices:", price_count)

    # Remove missing product descriptions
    missing_desc_count = df["Description"].isnull().sum()

    df = df.dropna(subset=["Description"])

    print("Removed Missing Descriptions:", missing_desc_count)

    df = df.reset_index(drop=True)

    print("\nCleaned Dataset Shape:", df.shape)

    return df


# Remove non-product transactions and standardize product codes
def filter_products(df):

    print("\n========== PRODUCT FILTERING ==========")

    df = df.copy()
    df["StockCode"] = df["StockCode"].astype(str).str.strip().str.upper()

    # Codes that do not represent actual products
    excluded_codes = {
        "POST",  # Postage
        "DOT",  # Dotcom postage
        "M",  # Manual transaction
        "BANK CHARGES",  # Bank charges
        "AMAZONFEE",  # Amazon fee
        "S",  # Samples
        "B",  # Bad debt adjustment
        "GIFT_0001_10",
        "GIFT_0001_20",
        "GIFT_0001_30",
        "GIFT_0001_40",
        "GIFT_0001_50",
    }

    excluded_products = df["StockCode"].isin(excluded_codes)

    removed_count = excluded_products.sum()

    df = df.loc[~excluded_products].copy()

    df.reset_index(drop=True)

    print("Removed Non-product Rows:", removed_count)
    print("Remaining Rows:", len(df))
    print("Remaining Unique Products:", df["StockCode"].nunique())
    print("Remaining Unique Invoices:", df["InvoiceNo"].nunique())

    return df
