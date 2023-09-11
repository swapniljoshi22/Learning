import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filtered_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    output = filtered_df[['product_id']]
    return output