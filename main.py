import numpy as np
import pandas as pd
files = {'chicago':'chicago.csv','washington':'washington.csv','new york city':'new_york_city.csv'}
cities = ['chicago','washington','new york city']
monthsdict = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6}
months=['january','february','march','april','may','june']
days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
global city,day,month


def user_cityrequest(): #Extracts  city of choice
    global city
    """This is a function that extracts the city that the user wants the data for."""
    while True:

        city = input("Which city do you want to know about? (Chicago/Washington/New York City), type q to exit") #Asks the user for the city
        if city=='q': #closes the program when the user enters q
            break
        if city.lower() == 'nyc' or city.lower() == 'new york': #This guarantees the name is going to be read matching the name in the dict regardless of how he types new york
            city='new york city'
        if city.lower() not in cities:
            print("This city is not available, the available cities are chicago,washington and nyc")
        else:
            city=city.lower() #Ensures lower case for all cities
            print(f"The city you chose is {city.title()}!")
            break
    return city


def user_monthrequest():
    """#Extracts the month of choice"""
    global month
    monthsint = [int(i) for i in range(1, 7)]

    while True:

        month = input(
            "Which month do you want to know about?, type q to exit")  # Prompts user for a month in numbers or name, idc
        if month == 'q':
            break
        if month == 'all':
            break

        try: #The try-except block ensures that both values string and integers are accepted e.g January and 1
            if int(month) not in monthsint:
                print("No data available for the entered month")

            else:
                month=int(month)
                if month in monthsint:
                    print(f"The month chosen is {month}")
                    break

                else:
                    print("No data available for the entered month")

        except ValueError: #Reaching this exception means the month entered is a string

            if month not in months:
                print("No data available for the entered month. months available are 1~6")

            else:
                print(f"The month you chose is {month}")
                month=monthsdict[month.lower()] #Ensuring that the returned value is still a number to be used in dataframe
                break

    return month



def user_dayrequest():
    """#Extracts the day of user's choice"""
    global day
    while True:
        day = input("Which day? type q to exit")
        if day == 'q':
            break
        if day == 'all':
            break
        if day.lower() not in days:
            print("This is not a day, check ur spelling!")
        else:
            day = day.lower()  # ensures lowercase.
            print(f"The day you chose is {day.title()}!")
            break

    return day


def get_data(city,month,day):
    """Loads the data for the given city,month,day"""
    df= pd.read_csv(files[city])


    df['Start Time']=pd.to_datetime(df['Start Time']) #Converts to date ytba3bas
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['Months']=pd.DatetimeIndex(df['Start Time']).month #Creates a new column that has all the months
    df['Weekdays']=(df['Start Time']).dt.day_name() #Creates new column that has all the weekdays
    df['Hours']=pd.DatetimeIndex(df['Start Time']).hour #New column with hours


    if month != 'all':
        df= df[df['Months']==month] ##slices the data frame so that it contains data for only the chosen month
    if day != 'all':
        df=df[df['Weekdays']==day.title()] #slices the data frame so that it contains data for only the chosen weekdays


    def commontimes():
        """Gives us the most common months,hours,day of week and hour"""
        if month != 'all':
            print(f"The most common month is {df['Months'].mode().sum()} !")
        if day != 'all':
            print(f"The most common day of the week is {df['Weekdays'].mode().sum()} !")
        print(f"The most common hour is {df['Hours'].mode().sum()} !\n")
    commontimes()

    def commonstations():
        """Prints the most common start stations, most common end stations, and the most common start to end trip"""
        print(f"The most common start station is {df['Start Station'].mode().sum()}")
        print(f"The most common end station is {df['End Station'].mode().sum()}")
        df['StartToEnd']=df['Start Station']+" to " + df['End Station'] ##Combining the Start to end station
        print(f"The most common start to end trip: ({df['StartToEnd'].mode()[0]})\n")

    commonstations()

    def usertypecount():
        """Prints the count of the number of each user type 'Customer' and 'Subscriber' """
        number_of_subscribers= (df['User Type'].value_counts().Subscriber) #counts the value 'subscriber in the column user type'
        number_of_customers=(df['User Type'].value_counts().Customer)  #counts the value customer in the column user type

        print(f"Number of Subscribers is {number_of_subscribers}")
        print(f"Number of Customers is {number_of_customers}\n")
    usertypecount()

    def gendercount():
        """Counts the number of each gender if the chosen city is NYC or Chicago"""
        if city != 'washington':
            number_of_males=(df['Gender'].value_counts().Male)
            number_of_females = (df['Gender'].value_counts().Female)
        print(f"Number of males is {number_of_males}")
        print(f"Number of females is {number_of_females}")
    gendercount()

    def birthyeardata():
        """Gets some birthyear data if the chosen city is NYC or Chicago"""
        if city!= 'washington':
            earliestbirthyear=int(df['Birth Year'].min().sum()) #Maximum birth year means the minimum #int to get rid of the .0 in the end
            mostrecentbirthyear=int(df['Birth Year'].max().sum()) #Maximum birth year means most recent!
            mostcommonbirthyear=int(df['Birth Year'].mode().sum()) #Mode is the most occurred!
        print(f"Earliest birthyr is {earliestbirthyear}")
        print(f"Most recent birthyear is {mostrecentbirthyear}")
        print(f"Most common birth year is {mostcommonbirthyear}")
    birthyeardata()

if __name__ == '__main__':
    while True:

        user_cityrequest()
        if city == 'q':
            break
        user_monthrequest()
        if month == 'q':
            break
        user_dayrequest()
        if day =='q':
            break
        get_data(city,month,day)
        eh_nzamk=input("3ayz tany? q to exit")
        if eh_nzamk=='q':
            break












