import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    print.tail(df)
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value.counts()

    # What is the average age of men?
    average_age_men = df['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors =(df.loc[df['education']=='Bachelors']  / df.loc[df['education']=='Bachelors'].sum()) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K
  more_50k = df.loc[salary >= '50K']
  
percentage_ae = (df.loc[df['education']=='Bachelors' & 'Master' | 'Doctorade']  / df.loc[df['education']=='Bachelors' & 'Master' | 'Doctorade'].sum()) * 100
    # What percentage of people without advanced education make more than 50K?
percentage_withouth_ae = (df.loc[df['education']!='Bachelors' & 'Master' | 'Doctorade']  / df.loc[df['education']!='Bachelors' & 'Master' | 'Doctorade'].sum()) * 100
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[df['education'] == 'Bachelors' & 'Master' | 'Doctorade']
    lower_education = df.loc[df['education']!= 'Bachelors' & 'Master' | 'Doctorade']

    # percentage with salary >50K
    higher_education_rich = (df.loc[df['salary' => 50K] / df.loc[df['salary' => 50K].sum()) * 100

    # percentage with salary <50K
    lower_education_rich = (df.loc[df['salary' =< 50K] / df.loc[df['salary' =< 50K].sum()) * 100


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df['hours-per-week'].min & df['salary' => 50k] / df['hours-per-week'].min.sum()) * 100

    rich_percentage = df['salary' => 50K] / df['salary' => 50K].sum() * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country =  df.query(df['salary' => 50K] IN df['native-country']).max()
    highest_earning_country_percentage = df.query((df['native-country'] and df['salary' => 50K] / df['native-country'] and df['salary' => 50K].sum()) * 100).max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (df['occupation'] and df.['country ' == 'India'] and df['salary' => 50K])

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
