import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read.csv("fcc-forum-pageviews.csv")

# Clean data
df = df.dropna()
df = df.shape()


def draw_line_plot():
  # Draw line plot
  plt.plot(df['Date'],df['Page Views'])
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
plt.xlabel('Date')
pla.ylabel('Page Views')
plt.grid(True)
plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = plt.bar(df['years'],df['Average Page Views'])
 

    # Draw bar plot
colors = [green,blue,yellow,purple, black, orange,red,gray, pink, brown, skyblue,darkgreen]


   plt.legend('Months','green'= January, 'blue'= February, 'yellow' = March, 'purple' = April , 'black' = May , 'orange' = June , 'red' = August , 'gray' = September , 'pink' = October , 'brown' = November , 'skyblue' = December , 'darkgreen' = December)
plt.show("df_bar")


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
plt.figure(figsize=(10,6))
plt.title("Year-wise Box Plot (Trend)")
sns.barplot(x =df['Page Views'] , y = df['Year'] )


 plt.figure(figsize=(10,6))
 plt.title("Month-wise Box Plot (Seasonality)")
sns.barplot(x =df['Page Views'], y = df['Months'])




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
