import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'] / (df['height']/100) **
                    2).apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=[
                     'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    # Draw the catplot with 'sns.catplot()'

    fig = sns.catplot(x='variable', col='cardio', hue='value', kind='count',
                      data=df_cat).set_axis_labels("variable", "total").figure
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_clean = df[(df['ap_lo'] <= df['ap_hi']) &
                  (df['height'] >= df['height'].quantile(0.025)) &
                  (df['height'] <= df['height'].quantile(0.975)) &
                  (df['weight'] >= df['weight'].quantile(0.025)) &
                  (df['weight'] <= df['weight'].quantile(0.975))
                  ]

    # Calculate the correlation matrix
    Corr = df_clean.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(Corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    with sns.axes_style("white"):
        f, fig = plt.subplots(figsize=(12, 7))

    # Draw the heatmap with 'sns.heatmap()'
        fig = sns.heatmap(Corr, vmin=0, vmax=.25, square=True,
                          annot=True, linewidths=.5, fmt=".1f", mask=mask).figure

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
