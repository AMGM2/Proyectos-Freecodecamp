import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

pd.head(df)
# Add 'overweight' column
df['overweight'] = pd.df(columns=['overweight'])

Calculo = (df['height']/100)*(df['height']/100)
IMC = df['weight'] / Calculo 
df.loc[IMC <= 25, 'overweight'] = 0 
df.loc[IMC > 25, 'overweight'] = 1 
df['overweight'] = pd.df(columns=['IMC'],
                  index=range(1))
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol']==1, 'cholesterol'] = 0 
df.loc[df['cholesterol']>1, 'cholesterol'] = 1 
df.loc[df['gluc']==1, 'gluc'] = 0 
df.loc[df['gluc']>1, 'gluc'] = 1

# Draw Categorical Plot

plt.show()
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None
    

    # Draw the catplot with 'sns.catplot()'
sns.catplot(x='variable',col='cardio',hue='value',kind='count',data=df_cat)


    # Get the figure for the output
    fig = 


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = N

    # Calculate the correlation matrix
     Corr = df_filtered.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(Corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, fig = plt.subplots(figsize=(12, 7))
    fig = sns.heatmap(Corr,vmin=0,vmax=.25,square=True,annot=True,linewidths=.5,fmt=".1f",mask=mask)



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
