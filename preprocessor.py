import pandas as pd

df = pd.read_csv('C:/Users/Rinku Yadav/Downloads/olympics-data-analysis-web-app-main/.ipynb_checkpoints/athlete_events.csv')
regions_df = pd.read_csv("C:/Users/Rinku Yadav/Downloads/olympics-data-analysis-web-app-main/.ipynb_checkpoints/noc_regions.csv")

def preprocess(df,regions_df):
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(regions_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df