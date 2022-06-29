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
    print()
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Would you like to see data for Chicago, New York, or Washington?')
    city=input()
    city = city.lower()
    while(city != 'chicago' and  city != 'new york' and city != 'washington'):
              print('Please enter one of the three cites:\nChicago, New York, or Washington')
              city = input()
              city = city.lower()
              print()

    month = '0'
    day = '0'
    print ('Would you like to filter the data by month, day, or not at all?')
    choice = input()
    choice = choice.lower()
    while(choice != 'month' and choice != 'day' and choice != 'not at all'):
          print('Please enter a choice to filter by:\nmonth, day, or not at all')
          choice = input()
          choice = choice.lower()
          print()
          
    if (choice == 'month'):
        # get user input for month (all, january, february, ... , june)
        day = 'all'
        print('Which month to filter by - January, February, March, April, May, or June?')
        month = input()
        month = month.lower()
        while(month != 'january' and  month != 'february' and month != 'march' and  month != 'april' and month != 'may' and month != 'june'):
              print('Please Enter valid month:\nJanuary, February, March, April, May, or June')
              month = input()
              month = month.lower()
              print()
              
    elif(choice == 'day'):
        # get user input for day of week (all, monday, tuesday, ... sunday)
        month = 'all'
        print('Which day to filter by - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')
        day = input()
        day = day.lower()
        while(day != 'monday' and  day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day !='friday' and day != 'saturday' and day != 'sunday'):
                      print('Please Enter valid day:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')
                      day=input()
                      day = day.lower()
                      print()
    else:
      month = 'all'
      day = 'all'                      
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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    if(city=='new york' or city =="New York"):
            city = 'new york city'
    elif(city =='Chicago' or city =='chicago'):
            city = 'chicago'
    else:
        city = 'washington'
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time']) 

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day
        
        
    # filter by month if applicable
    if month != 'all':
        month = month.lower()
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    print('What is the most popular month for traveling?')
    print(df['month'].mode()[0])

    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    print('What is the most popular day for traveling?')
    print(df['day'].mode()[0])


    # display the most common start hour
    print('What is the most popular start hour for traveling?')
    print(df['Start Time'].mode()[0])

    # extract hour from the Start Time column to create an hour column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', start_station)
    print()

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', end_station)
    print()


    # display most frequent combination of start station and end station trip
    popular_comb = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most Popular combination of start station and end station trip', popular_comb)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print('Total travel time: ', total)

    # display mean travel time
    avr = df['Trip Duration'].mean()
    print('Average travel time: ', avr)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n')
    print(user_types)
    if "Gender" in df.columns:
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('Counts of gender:\n')
        print(gender_counts)

    if 'Birth Year' in df.columns:

        # Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()

        print('Earliest year of birth:', earliest)
        print()
        print('Most recent year of birth:', most_recent)
        print()
        print('Most common year of birth:', most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        time.sleep(3)
        station_stats(df)
        time.sleep(3)
        trip_duration_stats(df)
        time.sleep(3)
        user_stats(df)
        time.sleep(3)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
