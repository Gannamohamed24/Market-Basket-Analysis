from mlxtend.frequent_patterns import apriori

# Find frequent itemsets using the Apriori algorithm


def find_frequent_itemsets(encoded_df, min_support=0.01):

    print("\n========== FREQUENT ITEMSETS ==========")
    print("Minimum Support:", min_support)

    frequent_itemsets = apriori(
        encoded_df, min_support=min_support, use_colnames=True, low_memory=True
    )

    # Calculate the number of products in each itemset
    frequent_itemsets["Length"] = frequent_itemsets["itemsets"].apply(len)

    # Sort results by itemset length and support
    frequent_itemsets = frequent_itemsets.sort_values(
        by=["Length", "support"], ascending=[True, False]
    ).reset_index(drop=True)

    print("\nTotal Frequent Itemsets:", len(frequent_itemsets))

    print("\nFrequent Itemsets by Length:")
    print(frequent_itemsets["Length"].value_counts().sort_index())

    return frequent_itemsets
