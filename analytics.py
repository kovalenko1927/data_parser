import pandas as pd


def perform_analysis(data_file):
    # Get data from CSV
    data = pd.read_csv(data_file)

    # Total products count
    total_products = len(data.index)

    # Available products count
    available_products = data[data['product_availability'].isin([True])]
    num_available_products = len(available_products.index)

    # Products with markdown count
    discounted_products = data[data['product_price_regular'] > data['product_price']]
    num_discounted_products = len(discounted_products.index)

    # Median price of available products
    average_price = available_products['product_price'].median()

    # Median markdown percent
    markdown_percent = (discounted_products['product_price_regular'] - discounted_products['product_price']) / \
        discounted_products['product_price_regular']
    median_markdown_percent = round(markdown_percent.median(), 4)

    # Outputting results
    print("Total products count:", total_products)
    print("Available products count:", num_available_products)
    print("Products with markdown count:", num_discounted_products)
    print("Median price of available products:", average_price)
    print("Median markdown percent:", median_markdown_percent)


# Main function
def main():
    data_file = 'comfy_products_list.csv'
    perform_analysis(data_file)


if __name__ == '__main__':
    main()
