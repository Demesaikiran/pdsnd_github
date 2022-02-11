import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('ENTER THE CITY NAME: ')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Choose the city from [1. Chicago, 2. New york city, 3. Washington]: ")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the month: ")
    while month not in ('all', 'january', 'february' , 'march', 'april', 'may', 'june'):
        month = input("Choose the month from 'january', 'february' , 'march', 'april', 'may', 'june: ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day: ").lower()

    while day not in ('all', 'monday', 'tuesday', 'wednesday','thursday',' friday','saturday','sunday'):
        day = input("Enter the day from 'monday', 'tuesday', 'wednesday','thursday',' friday','saturday','sunday': ").lower()

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
    df = pd.read_csv('{}.csv'.format(city))
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time']   = pd.to_datetime(df['End Time'])
    df['month']      = df['Start Time'].dt.month
    
    # Filtering by month
    
    if month != 'all':
        months = ['january', 'february' , 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Filetring by day if it is applied to it
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].value_counts().idxmax())


    # TO DO: display the most common day of week
    print("The most common day is: ", df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour is: ", df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: ", df['Start Station'].value_counts().idxmax())


    # TO DO: display most commonly used end station
    print("The most common end station is: ", df['End Station'].value_counts().idxmax())


    # TO DO: display most frequent combination of start station and end station trip
    combo_start_end = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most frequent combination of start station and end station is: ", combo_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum() / 3600.0
    print("Total travel time in hours is: ", total_time)


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean() / 3600.0
    print("Mean travel time is: ", mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        
    except:
        print("There is no data regarding gender")
    else:
        print(gender_count)
    
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        
        most_recent_year_of_births = int(df['Birth Year'].max())
        most_common_year_of_births = int(df['Birth Year'].value_counts().idxmax())
    except:
        print("There is no data regarding Birth year")
    else:
        print("The earliest year of birth is: {}, most recent one is: {} and the most common one is: {}".format(earliest_year_of_birth, most_recent_year_of_births, most_common_year_of_births))
        print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def raw_data(df):
    """Displays the data due filteration such that 5 rows will be added in each press"""

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()

    while view_data not in ('yes', 'no'):
        view_data = input("You have entered invalid input. Please enter 'yes' or 'no': ")

    count = 0
    while view_data != 'no':
        count += 5
        print(df.head(count))
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        while view_data not in ('yes', 'no'):
            view_data = input("You have entered invalid input. Please enter 'yes' or 'no': ")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
