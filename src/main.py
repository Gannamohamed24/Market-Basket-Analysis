from pathlib import Path
from src.data_preparation import load_data, explore_data, inspect_products
from src.data_cleaning import clean_data, filter_products
from src.transactions import create_transactions, encode_transactions
from src.frequent_itemsets import find_frequent_itemsets

# Define the project and output directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def main():

    # Load Dataset
    df = load_data()

    # Explore Dataset
    explore_data(df)
    inspect_products(df)

    # Clean Dataset
    cleaned_df = clean_data(df)

    # Filter Non-Product Items
    filtered_df = filter_products(cleaned_df)

    # Create Transactions
    transactions = create_transactions(filtered_df)

    # Encode Transactions
    encoded_df = encode_transactions(transactions)

    # Save Encoded Transactions
    encoded_df.to_csv(OUTPUT_DIR / "encoded_transactions.csv", index=False)

    print("\nEncoded Transactions Saved Successfully!")

    # Find Frequent Itemsets using Apriori
    frequent_itemsets = find_frequent_itemsets(encoded_df, min_support=0.01)

    # Convert itemsets into readable strings before saving
    frequent_itemsets["itemsets"] = frequent_itemsets["itemsets"].apply(
        lambda itemset: ", ".join(sorted(itemset))
    )

    # Save Frequent Itemsets
    frequent_itemsets.to_csv(OUTPUT_DIR / "frequent_itemsets.csv", index=False)

    print("Frequent Itemsets Saved Successfully!")


if __name__ == "__main__":
    main()
