import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    melt_df=pd.melt(products,id_vars=['product_id'], var_name='store', value_name='price')
    melt_df.dropna(inplace=True)
    return melt_df