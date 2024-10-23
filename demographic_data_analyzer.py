import numpy as np
import pandas as pd



def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    enum = df['race'].value_counts()
    race_count = pd.Series(enum)

    # What is the average age of men?
  
    men = df.loc[df["sex"]=="Male"]
    average_age_men = round(men["age"].mean(), 1)


    # What is the percentage of people who have a Bachelor's degree?
    bach = df.loc[df["education"] == "Bachelors"]

    percentage_bachelors = round((len(bach)/len(df)*100) , 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[((df['education']=='Bachelors')| (df['education']=='Masters') | (df['education']=='Doctorate'))]
    r_higher = df[(df['salary']== '>50K') & 
((df['education']=='Bachelors')| (df['education']=='Masters') | (df['education']=='Doctorate'))]


    lower_education = df[(df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate') ]
    r_lower = df[(df['salary']== '>50K') & 
    ((df['education']!='Bachelors')& (df['education']!='Masters') & (df['education']!='Doctorate'))]

    # percentage with salary >50K
    higher_education_rich = round(len(r_higher)/len(higher_education)*100, 1)
    lower_education_rich = round(len(r_lower)/len(lower_education)*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week']== 1)]
    min_rich_workers = df[(df['salary'] == '>50K') & (df['hours-per-week']== 1)]
    rich_percentage = round(len(min_rich_workers)/len(num_min_workers)*100, 1)

    # What country has the highest percentage of people that earn >50K?
    foo = df.loc[df["salary"]== ">50K"]
    fur = foo['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = fur.idxmax()
    highest_earning_country_percentage = round(fur.max()*100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    bar = (df['salary'] == '>50K') & (df['native-country'] == 'India')
    in_rich = df[bar]
    top_IN_occupation = in_rich['occupation'].value_counts().idxmax()

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
