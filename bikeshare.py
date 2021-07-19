#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        
    cities = ('Chicago', 'New York City', 'Washington')

    while True:
        city = input('Please enter the city you would like to explore: ')
        if city in cities: break
        else:
            print("Sorry, invalid option. Please try again.")
   
    # TO DO: get user input for month (all, january, february, ... , june)

    months = ('January', 'February', 'March', 'April', 'May', 'June', 'all')
    
    while True:
        month = input('Please choose a month you would like to explore: ')
        if month in months: break
        else:
            print("Sorry, invalid option. Please try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all')

    while True:
        day = input('Please choose the day of the week you would like to explore: ')
        if day in days: break
        else:
            print("Sorry, invalid option. Please try again.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

# Load data for specified city
    df = pd.read_csv(CITY_DATA[city])

# Convert starting times to datetime
    df['Start_Time'] = pd.to_datetime(df['Start Time'])
    
# Convert Start Time to months, days amd hours
    df['month'] = df['Start_Time'].dt.month
    df['day'] = df['Start_Time'].dt.day_name
    df['hour'] = df['Start_Time'].dt.hour

# Filter by the relevant month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    if months != 'all':
            month_index = months.index(month) + 1
            df = df[df['month'] == month_index]
        
# Filter by relevant day
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all')
    if days != 'all':
            df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    # Calculate the mode for the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: ', common_month)     

    # TO DO: display the most common start day
    
    # Calculate the mode for the most commonm day
    common_day = df['day'].mode()[0]
    print('The most common day is: ', common_day)  
    
    # Display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is: ', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: ', Start_Station)


    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: ', End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combo_Station = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display the total travel time
    total_travel_time = df['Trip Duration'].sum()/60/60/24
    print ("The total travel time is: ", total_travel_time)

    # Display the mean travel time
    mean_travel_time = (df['Trip Duration'].mean())/60
    print ("The mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display the counts of user types
    try:
        User_Types = df['User Type'].value_counts()
        print ("The count of user types is:", User_Types)
    except:
        print("There is no user types data available for this selection.")

    # Display the counts of gender
    try:
        gender = df['Gender'].value_counts()
        print ("The gender of user types is:", gender)
    except:
        print("There is no gender data available for this selection.")

    # Display earliest, most recent, and most common year of birth
    # Earliest Year of Birth
    try:
        earliest_yob = df['Birth Year'].min()
        print ("The earliest year of birth is:", earliest_yob)
    except:
        print("There is no birth year data available for this selection.")
    
    # Most Recent Year of Birth
    try:
        recent_yob = df['Birth Year'].max()
        print ("The most recent year of birth is:", recent_yob)
    except:
        print("There is no birth year data available for this selection.")
    
    # Most Common Year of Birth
    try:
        common_yob = df['Birth Year'].mode()[0]
        print ("The most common year of birth is:", common_yob)
    except:
        print("There is no birth year data available for this selection.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

## Display first 5 rows of data if requested
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data.lower() == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input('Do you wish to continue?: Enter yes or no.\n' ).lower()               
        if view_display.lower() != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
      
            
if __name__ == "__main__":
	main()


# In[ ]:




