import pandas as pd
import numpy as np

transactions = pd.read_csv(
    '~/philly_transactions/citizensunited/philly_transactions2011.csv'
    )

transactions.drop(['Unnamed: 0'], axis=1, errors='ignore', inplace=True)
# transactions['Year'] = transactions['Year'].astype(np.int64)
# transactions['Cycle'] = transactions['Cycle'].astype(np.int64)
# fix column types


# remove any non-categorized document types
transactions.dropna(subset=['DocType'], axis=0, inplace=True)

# contributions are all schedule I
contributions = transactions[transactions['DocType'].str.contains('Schedule I -')]

print(contributions)
